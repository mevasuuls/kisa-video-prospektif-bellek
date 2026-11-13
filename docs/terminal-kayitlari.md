# Terminal İşlem Kayıtları

Bu dosyada araştırma projesi kapsamında kullanılan PowerShell, Python ve Git komutları ile analiz sürecinin önemli çıktıları yer almaktadır.

## 1. Proje klasörlerinin oluşturulması

PowerShell üzerinden proje klasörleri oluşturulmuştur.

```powershell
mkdir data
mkdir data\raw
mkdir data\processed
mkdir docs
mkdir analysis
mkdir references
```

Çalışma dizinini kontrol etmek için:

```powershell
pwd
```

## 2. Python sürümünün kontrol edilmesi

```powershell
py list
py --version
```

Kullanılan Python sürümü: **Python 3.15.2**

## 3. Gerekli Python kütüphanelerinin kurulması

Veri analizi ve grafik oluşturma işlemleri için aşağıdaki kütüphaneler kurulmuştur.

```powershell
py -m pip install pandas
py -m pip install scipy
py -m pip install statsmodels
py -m pip install matplotlib
```

Kullanılan kütüphaneler:

- **Pandas:** CSV verilerini okuma, düzenleme ve analiz etme.
- **SciPy:** İstatistiksel testleri uygulama.
- **Statsmodels:** Çoklu karşılaştırmalarda Holm düzeltmesini uygulama.
- **Matplotlib:** Analiz grafiklerini oluşturma.

## 4. Veri setinin Python ile açılması

Kullanılan veri dosyası:

`data/raw/data/acc.csv`

Python ortamında kullanılan komutlar:

```python
import pandas as pd

veri = pd.read_csv("data/raw/data/acc.csv")

print(veri.head())
print(veri.shape)
```

Çıktı:

```text
(240, 5)
```

Veri setinde 240 satır ve 5 sütun bulunmaktadır.

Sütunlar:

- folder_id
- task
- interrupt
- measure
- accuracy

## 5. Prospektif bellek verilerinin ayrılması

```python
pm = veri[veri["task"] == "PM"]
print(pm.shape)
```

Çıktı:

```text
(120, 5)
```

Prospektif bellek verisi 120 gözlemden oluşmaktadır.

## 6. Ön test ve son test değişiminin hesaplanması

```python
pm_genis = pm.pivot(
    index="folder_id",
    columns="measure",
    values="accuracy"
)

pm_genis["degisim"] = (
    pm_genis["post"] - pm_genis["pre"]
)
```

Bu işlemle her katılımcının ön test ve son test performansı eşleştirilmiş ve değişim puanı hesaplanmıştır.

Değişim puanı:

**Son test − Ön test**

Pozitif değer performans artışını, negatif değer performans düşüşünü ifade eder.

## 7. Deney koşullarının ayrılması

```python
kosullar = pm[["folder_id", "interrupt"]].drop_duplicates()
kosullar = kosullar.set_index("folder_id")

pm_genis = pm_genis.join(kosullar)
```

Dört deney koşulu bulunmaktadır:

- Rest
- TikTok
- YouTube
- Twitter

Her koşulda 15 katılımcı yer almaktadır.

## 8. İstatistiksel analizlerin çalıştırılması

Analizlerde kullanılan temel kütüphaneler:

```python
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
```

Uygulanan testler:

- Shapiro-Wilk: Normal dağılımın incelenmesi.
- Levene: Varyans homojenliğinin incelenmesi.
- Alexander-Govern: Gruplar arasındaki farkın incelenmesi.
- Kruskal-Wallis: Grupların sıralama dağılımlarının karşılaştırılması.
- Mann-Whitney U: İkili grupların karşılaştırılması.
- Wilcoxon: Ön test ve son test ölçümlerinin karşılaştırılması.
- Holm düzeltmesi: Çoklu karşılaştırmalarda hata oranının kontrol edilmesi.

İkili karşılaştırmalarda kullanılan örnek kod:

```python
test = stats.mannwhitneyu(
    grup1,
    grup2,
    alternative="two-sided"
)
```

Holm düzeltmesi:

```python
duzeltme = multipletests(
    p_degerleri,
    method="holm"
)

print(duzeltme[1])
print(duzeltme[0])
```

## 9. Analiz dosyasının çalıştırılması

Tüm analiz işlemleri Python betiği üzerinden tekrar çalıştırılabilir hâle getirilmiştir.

PowerShell komutu:

```powershell
py analysis/pm_on_analiz.py
```

Analiz dosyası:

`analysis/pm_on_analiz.py`

## 10. Analiz sonuçları

| Deney koşulu | Ön test (%) | Son test (%) | Değişim |
|---|---:|---:|---:|
| Rest | 89.62 | 94.34 | +4.72 |
| TikTok | 80.13 | 48.70 | -31.42 |
| YouTube | 82.91 | 82.86 | -0.05 |
| Twitter | 86.56 | 97.62 | +11.06 |

Genel grup karşılaştırmalarında:

- Alexander-Govern p = 0.00001128
- Kruskal-Wallis p = 0.00001809

Bu sonuçlar deney koşullarının performans değişimleri bakımından birbirinden farklılaştığına işaret etmektedir.

TikTok grubunda performans düşüşü gözlenmiştir. Ancak bulgular, kısa video formatının tek başına etkisini değil, araştırmadaki TikTok kesintisi koşulunun etkisini göstermektedir.

## 11. Grafiklerin oluşturulması

Matplotlib kullanılarak iki grafik oluşturulmuştur:

```text
analysis/grafikler/pm_pre_post.png
analysis/grafikler/pm_degisim.png
```

Grafikler analiz betiği çalıştırıldığında otomatik olarak kaydedilmektedir.

## 12. Git ve GitHub işlemleri

Git deposunun durumunu kontrol etmek için:

```powershell
git status
```

Dosyaları takibe eklemek için:

```powershell
git add analysis/pm_on_analiz.py
git add analysis/sonuclar.md
git add analysis/grafikler/pm_pre_post.png analysis/grafikler/pm_degisim.png
```

Commit oluşturmak için:

```powershell
git commit -m "PM analiz grafikleri eklendi"
```

GitHub'daki değişiklikleri yerel depoya almak için:

```powershell
git pull --rebase origin main
```

Değişiklikleri GitHub'a göndermek için:

```powershell
git push origin main
```

## 13. Proje deposu

GitHub: https://github.com/mevasuuls/kisa-video-prospektif-bellek

Bu kayıtlar araştırmanın veri hazırlama, istatistiksel analiz, grafik oluşturma ve sürüm kontrolü aşamalarını belgelemek amacıyla hazırlanmıştır.