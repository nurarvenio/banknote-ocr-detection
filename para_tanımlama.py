# -*- coding: utf-8 -*-
import cv2
import easyocr
import numpy as np
import re

reader = easyocr.Reader(['tr', 'en'], gpu=False)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Hata: Webcam açılamadı!")
    exit()

cv2.namedWindow("Banknot OCR Tanima", cv2.WINDOW_NORMAL)


frame_count = 0
skip_frames = 10  
detected_value = None
best_conf = 0.0

print("OCR çalışıyor. Çıkmak için 'q'.")

while True:
    ret, frame = cap.read()
    if not ret: break

    frame_count += 1
    display_frame = frame.copy()

    # Sadece belirlenen aralıklarla OCR yapması sağlandı.
    if frame_count % skip_frames == 0:
        # Görüntüyü daha da küçülterek hız artırıldı.
        small_frame = cv2.resize(frame, (480, 360))
        results = reader.readtext(small_frame, detail=1, paragraph=False, low_text=0.4) 

        detected_value = None
        best_conf = 0.0
        possible_values = ["5", "10", "20", "50", "100", "200"]

        for (bbox, text, conf) in results:
            clean_text = text.replace("O", "0").replace("o", "0").replace("I", "1").replace("l", "1")
            numbers = re.findall(r'\d+', clean_text)
            
            for num in numbers:
                num = num.lstrip("0") or "0"
                if num in possible_values:
                    if conf > best_conf:
                        best_conf = conf
                        detected_value = num

    # Sonucu ekrana yazdırıldı. (Son okunan değeri ekranda tutar)
    if detected_value:
        cv2.putText(display_frame, f"{detected_value} TL", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
        cv2.putText(display_frame, f"Guven: {best_conf:.2f}", (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    else:
        cv2.putText(display_frame, "Araniyor...", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 2)

    # Görüntüyü göster
    cv2.imshow("Banknot OCR Tanima", display_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()