"""
PM (Prospective Memory) pre/post exploratory analysis.

Default input: data/raw/acc.csv
Usage:
    python analysis/pm_on_analiz.py
    python analysis/pm_on_analiz.py "C:/path/to/acc.csv"

Required columns: folder_id, task, interrupt, measure, accuracy
Packages: pandas, scipy, statsmodels
"""

from pathlib import Path
import sys
import itertools

import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
import matplotlib.pyplot as plt


GROUP_ORDER = ["rest", "tiktok", "youtube", "twitter"]


def main():
    default_path = Path("data/raw/data/acc.csv")
    csv_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default_path

    if not csv_path.exists():
        raise FileNotFoundError(
            f"Dosya bulunamadı: {csv_path}\n"
            "acc.csv dosyasını data/raw/ klasörüne koyun veya dosya yolunu argüman olarak verin."
        )

    df = pd.read_csv(csv_path)
    required = {"folder_id", "task", "interrupt", "measure", "accuracy"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"CSV dosyasında eksik sütun(lar): {sorted(missing)}")

    # Yalnızca Prospective Memory (PM) satırları.
    pm = df[df["task"].astype(str).str.upper().eq("PM")].copy()
    pm["interrupt"] = pm["interrupt"].astype(str).str.lower()
    pm["measure"] = pm["measure"].astype(str).str.lower()
    pm["accuracy"] = pd.to_numeric(pm["accuracy"], errors="coerce")
    pm = pm.dropna(subset=["folder_id", "interrupt", "measure", "accuracy"])

    # Her katılımcı ve koşul için ön/son test değerlerini eşleştir.
    wide = pm.pivot_table(
        index=["folder_id", "interrupt"],
        columns="measure",
        values="accuracy",
        aggfunc="mean",
    )

    if not {"pre", "post"}.issubset(wide.columns):
        raise ValueError("PM verisinde hem 'pre' hem de 'post' ölçümü bulunmalı.")

    paired = wide.dropna(subset=["pre", "post"]).reset_index()
    paired["change"] = paired["post"] - paired["pre"]

    print("\n=== PM VERİSİ ===")
    print(f"Katılımcı sayısı: {paired['folder_id'].nunique()}")
    print(paired.groupby("interrupt")["folder_id"].nunique().reindex(GROUP_ORDER))

    print("\n=== BETİMSEL İSTATİSTİKLER (yüzde) ===")
    desc = paired.groupby("interrupt").agg(
        n=("folder_id", "count"),
        pre_mean=("pre", "mean"),
        post_mean=("post", "mean"),
        change_mean=("change", "mean"),
        change_sd=("change", "std"),
    ).reindex(GROUP_ORDER)
    print(
    desc.assign(
        pre_mean=desc["pre_mean"] * 100,
        post_mean=desc["post_mean"] * 100,
        change_mean=desc["change_mean"] * 100,
        change_sd=desc["change_sd"] * 100
    ).round(2).to_string()
)
    
    # Grafiklerin kaydedileceği klasör
    grafik_klasoru = Path("analysis/grafikler")
    grafik_klasoru.mkdir(parents=True, exist_ok=True)

    # 1. Ön test - Son test grafiği
    grafik_verisi = desc[["pre_mean", "post_mean"]].reindex(GROUP_ORDER) * 100

    ax = grafik_verisi.plot(
        kind="bar",
        figsize=(10, 6),
        width=0.7
    )

    ax.set_title("Gruplara Göre PM Ön Test ve Son Test Performansı")
    ax.set_xlabel("Deney Koşulları")
    ax.set_ylabel("PM Performansı (%)")
    ax.set_xticklabels(["Rest", "TikTok", "YouTube", "Twitter"], rotation=0)
    ax.legend(["Ön Test", "Son Test"])
    ax.set_ylim(0, 100)

    plt.tight_layout()
    plt.savefig(grafik_klasoru / "pm_pre_post.png", dpi=300)
    plt.close()

    # 2. PM değişim grafiği
    fig, ax = plt.subplots(figsize=(10, 6))

    degisim_verileri = [
        paired.loc[paired["interrupt"] == grup, "change"].dropna() * 100
        for grup in GROUP_ORDER
    ]

    ax.boxplot(
    degisim_verileri,
    tick_labels=["Rest", "TikTok", "YouTube", "Twitter"],
    showmeans=True
    )

    ax.axhline(0, linestyle="--", linewidth=1)
    ax.set_title("Gruplara Göre PM Performansındaki Değişim")
    ax.set_xlabel("Deney Koşulları")
    ax.set_ylabel("Performans Değişimi (Yüzde Puan)")

    plt.tight_layout()
    plt.savefig(grafik_klasoru / "pm_degisim.png", dpi=300)
    plt.close()

    print("\nGrafikler analysis/grafikler klasörüne kaydedildi.")


    groups = {
        g: paired.loc[paired["interrupt"].eq(g), "change"].dropna().to_numpy()
        for g in GROUP_ORDER
    }
    groups = {g: x for g, x in groups.items() if len(x) > 0}

    print("\n=== SHAPIRO-WILK (değişim puanları) ===")
    for g, values in groups.items():
        if len(values) >= 3:
            result = stats.shapiro(values)
            print(f"{g}: W={result.statistic:.4f}, p={result.pvalue:.8f}, n={len(values)}")
        else:
            print(f"{g}: test için yeterli gözlem yok (n={len(values)})")

    print("\n=== LEVENE (median merkezli) ===")
    levene = stats.levene(*groups.values(), center="median")
    print(f"W={levene.statistic:.4f}, p={levene.pvalue:.8f}")

    print("\n=== GENEL GRUP TESTLERİ ===")
    ag = stats.alexandergovern(*groups.values())
    kw = stats.kruskal(*groups.values())
    anova = stats.f_oneway(*groups.values())
    print(f"Alexander-Govern: statistic={ag.statistic:.4f}, p={ag.pvalue:.8g}")
    print(f"Kruskal-Wallis: H={kw.statistic:.4f}, p={kw.pvalue:.8g}")
    print(f"One-way ANOVA (varsayımlar sorunluysa temkinli yorumlayın): "
          f"F={anova.statistic:.4f}, p={anova.pvalue:.8g}")

    print("\n=== İKİLİ MANN-WHITNEY U + HOLM ===")
    comparisons, raw_p = [], []
    for a, b in itertools.combinations(GROUP_ORDER, 2):
        if a in groups and b in groups:
            test = stats.mannwhitneyu(groups[a], groups[b], alternative="two-sided")
            comparisons.append((a, b, test.statistic))
            raw_p.append(test.pvalue)

    adjusted = multipletests(raw_p, method="holm")[1]
    for (a, b, u), p_adj in zip(comparisons, adjusted):
        print(f"{a} – {b}: U={u:.3f}, Holm p={p_adj:.8f}")

    print("\n=== GRUP İÇİ WILCOXON + HOLM ===")
    raw_within = []
    within_names = []
    for g in GROUP_ORDER:
        sub = paired[paired["interrupt"].eq(g)]
        if len(sub) == 0:
            continue
        # Eşleştirilmiş ön/son test değerleri.
        result = stats.wilcoxon(
            sub["pre"], sub["post"],
            alternative="two-sided",
            zero_method="wilcox",
            method="auto",
        )
        within_names.append(g)
        raw_within.append(result.pvalue)

    adjusted_within = multipletests(raw_within, method="holm")[1]
    for g, p_adj in zip(within_names, adjusted_within):
        print(f"{g}: Holm p={p_adj:.8f}")

    print("\nNot: accuracy 0–1 aralığındaysa yüzdeye çevirmek için 100 ile çarpılır.")
    print("Bu betik keşifsel/ön analiz içindir; test seçimi ve varsayımlar raporda açıklanmalıdır.")


if __name__ == "__main__":
    main()
