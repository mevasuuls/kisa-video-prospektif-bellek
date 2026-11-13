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


GROUP_ORDER = ["rest", "tiktok", "youtube", "twitter"]


def main():
    default_path = Path("data/raw/acc.csv")
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
    print((desc * 100).round(2).to_string())

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
