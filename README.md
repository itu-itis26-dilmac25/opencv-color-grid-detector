# opencv-color-grid-detector
Real-time green colored square detection and 3x3 grid localization using OpenCV

## Özellikler

- Webcam üzerinden gerçek zamanlı görüntü alma
- Görüntüyü 3x3'lük grid'e bölme
- BGR renk uzayından HSV renk uzayına dönüşüm
- HSV renk aralığı kullanarak yeşil nesneyi algılama
- Contour (kontur) tespiti ve en büyük konturun seçilmesi
- Image moments kullanarak nesnenin merkez koordinatlarını hesaplama
- Algılanan nesnenin etrafına bounding rectangle çizme
- Nesnenin bulunduğu grid hücresini 1-9 arasında belirleme
- Nesne algılanmadığında ekranda "Kare araniyor" mesajını gösterme

## Kurulum

Öncelikle projeyi bilgisayarınıza indirin:

```bash
git clone https://github.com/itu-itis26-dilmac25/opencv-color-grid-detector.git
cd opencv-color-grid-detector
```

Gerekli kütüphaneyi yükleyin:

```bash
pip install opencv-python
```

## Çalıştırma

Proje klasöründe aşağıdaki komutu çalıştırın:

```bash
python opencv_color_grid/main.py
```

Webcam'inizin bağlı ve erişilebilir olduğundan emin olun.

Uygulamayı kapatmak için `q` tuşuna basın.

## Grid Numaralandırması

Grid hücreleri soldan sağa ve yukarıdan aşağıya numaralandırılır:

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |
