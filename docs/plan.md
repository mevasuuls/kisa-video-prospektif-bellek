# Araştırma Planı

## 1. Proje Başlığı

**Kısa Video İçeriklerine Maruz Kalmanın Prospektif Bellek Performansı Üzerindeki Etkisinin İncelenmesi**

## 2. Araştırmanın Amacı

Bu araştırmanın amacı, farklı dijital içerik koşullarına maruz kalmanın bireylerin prospektif bellek performansı üzerindeki etkisini incelemektir.

Prospektif bellek, gelecekte yapılması planlanan bir işi veya belirli bir zamanda gerçekleştirilmesi gereken bir görevi hatırlama becerisidir.

Araştırmada özellikle TikTok gibi kısa video içeriklerinin, bireylerin prospektif bellek performansında bir değişime neden olup olmadığı incelenecektir.

## 3. Araştırma Soruları

### 3.1. Temel Araştırma Sorusu

- Farklı dijital içerik koşullarına maruz kalmak, katılımcıların prospektif bellek doğruluk oranlarında müdahale öncesinde ve sonrasında nasıl bir değişim oluşturmaktadır?

### 3.2. Alt Araştırma Soruları

- TikTok koşulunda bulunan katılımcıların prospektif bellek performansındaki değişim, dinlenme koşulundaki katılımcılardan farklı mıdır?
- TikTok koşulunun prospektif bellek performansı üzerindeki etkisi YouTube ve Twitter koşullarıyla karşılaştırıldığında nasıl farklılaşmaktadır?
- Farklı dijital içerik koşulları, prospektif bellek görevlerinin tepki sürelerinde nasıl bir değişim oluşturmaktadır?
- Prospektif bellek performansındaki değişim ile karar verme sürecini açıklayan Drift Diffusion Model (DDM) parametreleri arasında bir ilişki var mıdır?

## 4. Araştırma Hipotezleri

- **H1:** TikTok koşulundaki katılımcıların müdahale sonrası prospektif bellek doğruluk oranları, müdahale öncesine göre düşecektir.
- **H2:** Prospektif bellek doğruluk oranlarındaki müdahale öncesi ve sonrası değişim, deney koşullarına göre farklılık gösterecektir.
- **H3:** TikTok koşulundaki prospektif bellek doğruluk oranı değişimi, dinlenme koşulundaki değişimden daha olumsuz olacaktır.
- **H4:** Prospektif bellek tepki sürelerindeki müdahale öncesi ve sonrası değişim, deney koşullarına göre farklılık gösterecektir.
- **H5:** Prospektif bellek doğruluk oranındaki değişim ile DDM parametrelerindeki değişim arasında ilişki bulunacaktır.

*Not: H4 ve H5 ikincil ve keşfedici analizler kapsamında değerlendirilecektir.*

## 5. Araştırmanın Yöntemi

### 5.1. Araştırma Türü

Araştırma, nicel araştırma yaklaşımına dayalı ikincil veri analizi olarak yürütülecektir.

İkincil veri analizi, daha önce başka bir araştırma kapsamında toplanmış verilerin yeni araştırma soruları doğrultusunda yeniden incelenmesidir.

### 5.2. Veri Seti

Araştırmada Stuttgart Üniversitesi'nin DaRUS veri deposunda yayımlanan mevcut deneysel veri seti kullanılacaktır.

- **Veri seti:** Prospektif bellek ve dijital içerik koşullarına ilişkin deneysel veriler
- **Veri deposu:** DaRUS
- **DOI:** 10.18419/DARUS-3327
- **Bağlantı:** https://darus.uni-stuttgart.de/dataset.xhtml?persistentId=doi:10.18419/darus-3327
- **Katılımcı sayısı:** 60
- **Deney koşulları:** 4 grup
- **Grup başına katılımcı:** 15

Veri setinde katılımcılar dört farklı koşula ayrılmıştır:

1. **Rest:** Dinlenme koşulu; herhangi bir dijital içerik izlenmemesi.
2. **TikTok:** TikTok kısa video akışına maruz kalma.
3. **YouTube:** YouTube videosu izleme.
4. **Twitter:** Twitter içerik akışına maruz kalma.

Deneyde katılımcılar, kesinti öncesinde ve sonrasında bilişsel görevleri tamamlamıştır. Dijital içerik veya dinlenme koşulu yaklaşık 10 dakika sürmüştür.

### 5.3. Veri Setinin Dosyaları

Veri setinde bulunan dosyalar ve araştırmada kullanım amaçları:

| Dosya | İçerik | Kullanım Amacı |
| `acc.csv` | Doğruluk oranları | Temel analiz |
| `rt.csv` | Tepki süreleri ve görev düzeyindeki veriler | İkincil analiz |
| `q.csv` | Anket verileri | Keşfedici analiz |
| `ddm.csv` | Drift Diffusion Model parametreleri | Keşfedici analiz |

Araştırmanın temel analizinde `acc.csv` dosyasındaki prospektif bellek (PM) doğruluk oranları kullanılacaktır.

### 5.4. Araştırma Değişkenleri

**Bağımsız değişkenler:**

- Deney koşulu: Rest, TikTok, YouTube ve Twitter.
- Ölçüm zamanı: Müdahale öncesi (pre) ve müdahale sonrası (post).

**Bağımlı değişkenler:**

- Prospektif bellek doğruluk oranı.
- Prospektif bellek tepki süresi (ikincil değişken).

**Keşfedici değişkenler:**

- Drift Diffusion Model parametreleri: drift, noise, bound ve nondectime.

## 6. Veri Analizi Planı

Veri analizinde aşağıdaki aşamalar izlenecektir:

1. Veri setinin incelenmesi ve analiz için hazırlanması.
2. Eksik verilerin ve olası aykırı değerlerin kontrol edilmesi.
3. Deney koşullarına göre tanımlayıcı istatistiklerin hesaplanması.
4. Müdahale öncesi ve sonrası prospektif bellek doğruluk oranlarının karşılaştırılması.
5. Deney koşulu ile ölçüm zamanının ortak etkisinin incelenmesi.
6. Gerekli görülmesi durumunda tepki süreleri ve DDM parametreleri üzerinden ikincil analizlerin yapılması.

Temel analizde, deney koşulu ve ölçüm zamanı arasındaki etkileşim incelenecektir.

Verilerin yapısına ve istatistiksel varsayımlara göre karma desenli ANOVA veya karma etkili model kullanılacaktır. Doğruluk verilerinin yapısı uygun olduğunda binom dağılımlı karma etkili model de değerlendirilecektir.

## 7. Araştırmanın Sınırlılıkları

- Veri setindeki katılımcı sayısı 60 kişi ile sınırlıdır.
- Katılımcılar 19–34 yaş aralığındadır.
- Katılımcılar Almanca dil yeterliliğine sahip kişilerden oluşmaktadır.
- Araştırmada TikTok koşulu kullanılmıştır; bu nedenle sonuçlar tüm kısa video platformlarına genellenemez.
- TikTok koşulunun etkisi, kısa video formatından ve hızlı içerik değişiminden tamamen bağımsız olarak değerlendirilemeyebilir.
- Araştırma mevcut bir veri setine dayandığından yeni katılımcılardan veri toplanmayacaktır.

## 8. Beklenen Katkı

Bu araştırmanın, kısa video içeriklerine maruz kalma ile prospektif bellek performansı arasındaki ilişkinin deneysel veriler üzerinden incelenmesine katkı sağlaması beklenmektedir.

Ayrıca farklı dijital içerik koşullarının bilişsel görev performansıyla nasıl ilişkili olabileceğine yönelik karşılaştırmalı bir değerlendirme sunması amaçlanmaktadır.

## 9. Kaynakça

- DaRUS. (n.d.). *Prospective memory and digital interruption experimental dataset*. https://doi.org/10.18419/DARUS-3327

- Araştırmanın orijinal makalesi: Veri setinin yayımlandığı CHI 2023 çalışması. Tam bibliyografik bilgiler kaynakça düzenlemesi sırasında eklenecektir.