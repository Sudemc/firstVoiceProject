# 🎵 Müzik Enstrüman Ayrıştırma ve Görselleştirme

Bu proje, bir müzik parçasını **Spleeter** kullanarak enstrüman ve vokal bileşenlerine ayırır. Ayrıştırılan ses bileşenleri **Librosa** ile analiz edilir ve **Matplotlib** kullanılarak görselleştirilir.

## 🚀 Özellikler
- **Spleeter** ile müzik dosyasını **vokal** ve **enstrümantal** parçalara ayırma
- **Librosa** ile ses sinyali analizi (zaman, frekans ve spektral analiz)
- **Matplotlib** ile ses dalga formlarını, spektrumları ve pitch grafiğini görselleştirme
- Kullanıcıdan enstrüman seçimi yapmasını isteyen interaktif terminal arayüzü

## 📂 Veri Seti
Bu projede, belirli müzik veri setleri kullanılmıştır. Eğer kendi veri setinizi kullanmak isterseniz, `.wav` formatında dosyaları `music_dataset/` klasörüne yerleştirebilirsiniz.

Eğer veri setini paylaşmak isterseniz, büyük dosyalar için **Google Drive, Kaggle veya Zenodo** gibi platformlara yükleyerek bağlantıyı burada belirtebilirsiniz.

## 🔧 Kurulum
Projeyi çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1️⃣ Gerekli Kütüphaneleri Yükleyin
```bash
pip install spleeter librosa matplotlib numpy
```

### 2️⃣ Spleeter Modelini İndirin (İlk Kullanım İçin Gerekli)
```bash
spleeter separate -i example.mp3 -o output/ -p spleeter:2stems
```

### 3️⃣ Projeyi Çalıştırın
```bash
python main.py
```

## 🎮 Kullanım
1. Terminalde çalıştırdıktan sonra, size **müzik veri setinizdeki enstrümanları** listeleyen bir seçenek sunulacaktır.
2. Bir enstrüman seçtiğinizde, bu enstrümana ait ilk `.wav` dosyası işlenecektir.
3. Spleeter, ses dosyasını **vokal** ve **arka plan** olarak ikiye ayıracaktır.
4. **Librosa** ile ayrıştırılan sesler analiz edilecek ve **Matplotlib** ile görselleştirilecektir.
5. Ayrıştırılan ses bileşenleri `output/` klasörüne kaydedilecektir.

## 📊 Görselleştirmeler
Proje, ses sinyallerini analiz etmek için çeşitli grafikler üretir:
- **Dalga formu (Waveform)**: Sesin zaman içindeki değişimi
- **Mel Spektrogramı**: Frekansların zaman içinde nasıl değiştiğini gösterir
- **Fourier Dönüşümü**: Frekans spektrumlarını çıkarır
- **Zaman Zarfı (Envelope)**: Sesin dinamiklerini görselleştirir
- **Pitch Grafiği**: Vokal ve enstrüman sesinin temel frekanslarını belirler


## 💡 Gelecek Geliştirmeler
- Daha fazla enstrüman ayrıştırma (Spleeter:4stems veya 5stems modeli kullanılarak)
- Gerçek zamanlı analiz ve canlı grafik gösterimi
- Kullanıcı dostu bir **GUI arayüzü** ekleme

## 🏆 Katkıda Bulunma
Eğer bu projeye katkıda bulunmak isterseniz:
1. Projeyi **fork** edin.
2. Yeni bir **branch** oluşturun: `git checkout -b yeni-ozellik`
3. Değişikliklerinizi ekleyin ve commit yapın: `git commit -m 'Yeni özellik eklendi'`
4. GitHub üzerinden bir **pull request** oluşturun.

## 📄 Lisans
Bu proje **MIT Lisansı** ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına göz atabilirsiniz.

---
🎼 **Bu proje hakkında geri bildirim veya önerileriniz varsa, lütfen GitHub üzerinden paylaşın!** 🚀

