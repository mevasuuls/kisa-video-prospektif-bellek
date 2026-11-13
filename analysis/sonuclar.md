# Ön Analiz Sonuçları: Prospektif Bellek (PM)

> **Durum:** Ön analiz raporu. Bu belge nihai makale sonuçları değildir. Analiz, DaRUS veri setindeki `acc.csv` dosyasının yalnızca `task == "PM"` satırlarına dayanır. Lexical Decision (LD) sonuçları ana analize dahil edilmemiştir.

## 1. Analiz kapsamı

- **Araştırma odağı:** Kesinti koşulunun prospektif bellek doğruluğundaki ön test–son test değişimiyle ilişkisi.
- **Koşullar:** Rest, TikTok, YouTube ve Twitter.
- **Örneklem:** 60 katılımcı; her koşulda 15 katılımcı.
- **Birincil sonuç değişkeni:** PM doğruluk oranı (`accuracy`).
- **Değişim puanı:** Son test doğruluğu − ön test doğruluğu.
- **Birim:** Değişim, yüzde puan olarak raporlanmıştır.

Bu analiz ikincil veri analizidir. Yeni katılımcı verisi toplanmamıştır.

## 2. Betimsel istatistikler

| Koşul | Ön test ortalaması | Son test ortalaması | Ortalama değişim |
|---|---:|---:|---:|
| Rest | %89,62 | %94,34 | +4,72 yüzde puan |
| TikTok | %80,13 | %48,70 | −31,42 yüzde puan |
| YouTube | %82,91 | %82,86 | −0,05 yüzde puan |
| Twitter | %86,56 | %97,62 | +11,06 yüzde puan |

TikTok koşulunda ortalama PM doğruluğu yaklaşık 31,42 yüzde puan azalmıştır. Diğer koşullarda aynı ölçekte bir düşüş gözlenmemiştir.

## 3. Varsayım kontrolleri

### 3.1. Shapiro–Wilk normallik testi

Normallik, her katılımcının son test − ön test değişim puanları üzerinden ve koşul bazında incelenmiştir.

| Koşul | p | Değerlendirme |
|---|---:|---|
| Rest | 0,00757 | Normallikten sapma |
| TikTok | 0,35105 | Normallikten sapmaya ilişkin kanıt yok |
| YouTube | 0,00023 | Normallikten sapma |
| Twitter | 0,01578 | Normallikten sapma |

Dört koşulun üçünde normallik varsayımına ilişkin sorun görülmüştür.

### 3.2. Levene varyans homojenliği testi

- Levene istatistiği: 4,0988
- p: 0,01063

Sonuç, koşulların değişim puanları varyanslarının eşit olduğu varsayımını desteklememektedir.

Bu nedenle sonuçlar yalnızca klasik tek yönlü ANOVA'ya dayandırılmamış; parametrik olmayan ve eşit olmayan varyanslara dayanıklı ek karşılaştırmalar da raporlanmıştır.

## 4. Koşullar arası genel karşılaştırma

Değişim puanları koşullar arasında karşılaştırılmıştır.

| Test | İstatistik | p | Sonuç |
|---|---:|---:|---|
| Alexander–Govern | 25,6515 | 0,00001128 | Anlamlı |
| Kruskal–Wallis | H = 24,6706 | 0,00001809 | Anlamlı |
| Klasik tek yönlü ANOVA (varsayım sorunları nedeniyle temkinli) | F(3,56) = 16,2329 | 0,0000001035 | Anlamlı |

**Önemli yöntem notu:** Önceki taslakta p = 0,0000113 sonucu “Welch ANOVA” olarak adlandırılmıştı. Bu değer, kullanılan hesaplamada **Alexander–Govern testine** aittir; dolayısıyla burada doğru test adıyla düzeltilmiştir. Alexander–Govern testi, eşit olmayan varyanslara karşı dayanıklı genel grup karşılaştırmalarından biridir. Kruskal–Wallis sonucu da gruplar arasında fark bulunduğuna işaret etmektedir.

## 5. İkili karşılaştırmalar

Mann–Whitney U testleriyle yapılan altı ikili karşılaştırmada Holm çoklu karşılaştırma düzeltmesi uygulanmıştır.

| Karşılaştırma | Holm-düzeltilmiş p | Sonuç |
|---|---:|---|
| Rest – TikTok | 0,00116 | Anlamlı |
| Rest – YouTube | 0,39772 | Anlamlı değil |
| Rest – Twitter | 0,02017 | Anlamlı |
| TikTok – YouTube | 0,01100 | Anlamlı |
| TikTok – Twitter | 0,00019 | Anlamlı |
| YouTube – Twitter | 0,39772 | Anlamlı değil |

TikTok koşulunun değişim puanı dağılımı diğer üç koşulun her birinden anlamlı biçimde farklıdır. Ayrıca Rest ve Twitter koşulları arasında da anlamlı fark bulunmuştur.

## 6. Koşul içi ön test–son test karşılaştırmaları

Her koşulda ön test ve son test puanları Wilcoxon işaretli sıralar testiyle karşılaştırılmış; dört test için Holm düzeltmesi uygulanmıştır.

| Koşul | Holm-düzeltilmiş p | Sonuç |
|---|---:|---|
| Rest | 0,05626 | Anlamlı değil |
| TikTok | 0,00695 | Anlamlı düşüş |
| YouTube | 0,24316 | Anlamlı değil |
| Twitter | 0,00371 | Anlamlı artış |

Rest koşulundaki artış, düzeltme sonrasında 0,05 anlamlılık eşiğini geçmemektedir. Bu nedenle istatistiksel olarak anlamlı kabul edilmemiştir.

## 7. Hipotezlerin mevcut bulgularla değerlendirilmesi

- **H1:** TikTok koşulunda PM doğruluğu ön testten son teste düşer. **Desteklenmiştir.** TikTok grubunda düşüş anlamlıdır (Holm-düzeltilmiş p = 0,00695).
- **H2:** PM doğruluğundaki değişim deney koşullarına göre farklılaşır. **Desteklenmiştir.** Genel koşullar arası karşılaştırmalar anlamlıdır.
- **H3:** TikTok koşulundaki değişim Rest koşulundakinden daha olumsuzdur. **Desteklenmiştir.** İki koşulun değişim puanları arasındaki ikili karşılaştırma anlamlıdır (Holm-düzeltilmiş p = 0,00116).

Bu değerlendirmeler mevcut veri ve analiz planı kapsamında ön bulgulardır. Nihai raporda hipotezlerin yönü, test seçimi ve çoklu karşılaştırma yaklaşımı yöntem bölümünde önceden tanımlanmış biçimde açıklanmalıdır.

## 8. Yorum ve sınırlılıklar

1. Her koşulda yalnızca 15 katılımcı bulunmaktadır. Küçük grup büyüklükleri tahminlerin belirsizliğini artırabilir.
2. Doğruluk oranları 0 ile 1 arasında sınırlı ölçümlerdir. Bu nedenle oran verilerinin dağılım özellikleri ve olası tavan/taban etkileri dikkate alınmalıdır.
3. Katılımcılar orijinal çalışmada 19–34 yaş aralığında, Almanca konuşan kişilerden oluşmaktadır. Örneklem Türkiye'deki genel nüfusu temsil etmez.
4. Yalnızca TikTok koşulunun kısa video akışı içermesi, kısa video biçiminin etkisini hızlı içerik/bağlam değişiminden ayırmayı mümkün kılmaz. Bulgular tüm kısa video platformlarına genellenmemelidir.
5. Bu rapor ikincil veri analizidir. Bulgular, veri setinin deneysel koşulları ve özgün çalışma tasarımı bağlamında yorumlanmalıdır.
6. Aykırı veya düşük doğruluk değerleri yalnızca istatistiksel olarak sıra dışı oldukları için otomatik biçimde çıkarılmamalıdır. Olası veri giriş/ölçüm sorunları kaynak dosyalarla kontrol edilmelidir.

## 9. Ön sonuç

Ön analiz, TikTok kesinti koşulunda PM doğruluğunun ön testten son teste belirgin biçimde azaldığını ve bu değişimin diğer koşullardan farklılaştığını göstermektedir. YouTube koşulunda ortalama değişim sıfıra yakındır. Rest ve Twitter koşullarında ortalama artış görülmüş; Wilcoxon testinde Twitter artışı anlamlı, Rest artışı ise Holm düzeltmesinden sonra anlamlı bulunmamıştır.

Bu bulgular, kısa video akışı ve hızlı içerik değişiminin prospektif bellek performansıyla ilişkisini incelemek açısından dikkat çekicidir. Ancak mevcut tasarım, kısa video biçiminin etkisini içerik değiştirme hızından bağımsız biçimde belirleyemediği için sonuçlar bu sınırlılık açıkça belirtilerek sunulmalıdır.

## 10. Veri kaynağı

- DaRUS veri seti, DOI: [10.18419/DARUS-3327](https://doi.org/10.18419/DARUS-3327)
- Veri seti sayfası: [DaRUS – DOI 10.18419/DARUS-3327](https://darus.uni-stuttgart.de/dataset.xhtml?persistentId=doi:10.18419/DARUS-3327)

## 11. Tekrarlanabilirlik

Bu raporla birlikte verilen `analysis/pm_on_analiz.py` betiği, `acc.csv` dosyasını okuyarak PM satırlarını filtreler ve betimsel istatistikleri, varsayım kontrollerini, genel grup testlerini, Holm-düzeltilmiş ikili karşılaştırmaları ve koşul içi Wilcoxon testlerini yeniden hesaplar.

Ham veri dosyasını herkese açık GitHub deposuna yüklemeyin. Betiği yerel bilgisayarınızda, ham veri dosyasının bulunduğu konumdan çalıştırın. Gerekli Python paketleri: `pandas`, `scipy`, `statsmodels`.
