
  # Banknot OCR Tanıma Projesi (Banknote Recognition)
## 🚀 Temel Özellikler
    Real-time Detection: Kameradan gelen görüntüyü anlık olarak işler.

    Performance Optimization: Görüntü boyutlandırma (resize) ve kare atlama (skip_frames) teknikleriyle işlemci yükü azaltılmıştır.

    Data Cleaning: Regex (düzenli ifadeler) kullanılarak OCR hataları (O -> 0, I -> 1 gibi) otomatik düzeltilir.

    Filter System: Sadece geçerli Türk Lirası değerlerini (5, 10, 20, 50, 100, 200) filtreler.

 ## 🛠 Kullanılan Teknolojiler
    Python 3.s10

    EasyOCR: Derin öğrenme tabanlı metin tanıma motoru.

    OpenCV (cv2): Görüntü işleme ve kamera yönetimi.

    NumPy: Matris ve dizi işlemleri.

    Regular Expressions (re): Metin içinden sayısal verilerin ayıklanması.

  ## 📋 Kurulum (Installation)
    Projeyi çalıştırmak için aşağıdaki kütüphanelerin yüklü olduğundan emin olun:

    Bash
    pip install easyocr opencv-python numpy
    Not: Eğer görüntü penceresi açılırken hata alırsanız, opencv-python-headless sürümünün yüklü olmadığından emin olun.

  ## 💻 Çalıştırma
    Kodu çalıştırmak için terminale şu komutu yazın:

    Bash
    python banknot_ocr.py
    Uygulamadan çıkmak için klavyeden 'q' tuşuna basın.

  ## 🔍 Kodun Çalışma Mantığı
    Reader Initialization: EasyOCR, Türkçe ve İngilizce dilleri için başlatılır. gpu=False parametresi ile CPU üzerinden çalışması optimize edilmiştir.

    Video Capture: cv2.VideoCapture(0) ile varsayılan kameradan görüntü alınır.

    Pre-processing: Görüntü 480x360 boyutuna küçültülerek işlem hızı artırılır.

    Recognition: Her 10 karede bir metin taraması yapılır.

    Heuristic Filter: Bulunan metinler içindeki rakamlar temizlenir ve possible_values listesindeki banknot değerleriyle karşılaştırılır.

  ## 👤 Geliştirici
    İsim: Nur Arven

    Departman: Information Technology and Software (BT ve Yazılım)
