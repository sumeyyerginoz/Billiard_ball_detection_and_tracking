import cv2
import numpy as np
from datetime import datetime

# Önceki top merkezlerini ve zaman detaylarını tutmak için 
red_ball_trajectory = []
prev_time = None
white_trajectory = []
white_start = None
white_stop = False
white_stopped_time = None

def detect_billiard_balls(frame):
    global red_ball_trajectory, prev_time, white_trajectory, white_start, white_stop, white_stopped_time

    # Kareyi HSV renk uzayına dönüştürün
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı top için renk aralığı
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([5, 255, 255])
    lower_red2 = np.array([160, 100, 100])
    upper_red2 = np.array([179, 255, 255])
    
    # Kırmızı renk maskesi oluşturun
    red_mask = cv2.inRange(hsv_frame, lower_red2, upper_red2) 

    # Kırmızı renk maskesini kullanarak tespit edilen nesnelerin konturlarını bulun
    contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Belirli bir boyut aralığındaki nesneleri tespit etmek için filtreleyin
    min_area = 77  # En küçük kabul edilebilir kontur alanı
    max_area = 777  # En büyük kabul edilebilir kontur alanı

    for contour in contours:
        area = cv2.contourArea(contour)

        if min_area < area < max_area:
            # Konturun etrafına sığdırılmış dikdörtgen al
            x, y, w, h = cv2.boundingRect(contour)

            # Merkezi hesapla
            centroid_x = x + w // 2
            centroid_y = y + h // 2
            center = (centroid_x, centroid_y)

            # Merkezi takip listesine ekle
            red_ball_trajectory.append(center)

            # Beyaz topun vurulma anını bulmak için
            white_center = (centroid_x, centroid_y)
            white_trajectory.append(white_center)

            if not white_start:
                white_start = datetime.now()

            # Beyaz topun durma anını tespit et
            if len(white_trajectory) >= 2:
                last_center = white_trajectory[-1]
                second_last_center = white_trajectory[-2]
                distance = np.linalg.norm(np.array(last_center) - np.array(second_last_center))

                if distance < 5:  # Eğer beyaz top durduysa
                    if not white_stop:
                        white_stop = True
                        white_stopped_time = datetime.now()

            # Kırmızı topun etrafına dikdörtgen çiz
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

def calculate_speed(prev_pos, current_pos, frame_rate=30):
    # İki nokta arasındaki mesafeyi hesapla
    distance = np.linalg.norm(np.array(current_pos) - np.array(prev_pos))
    # Hızı kareler arası zamanla çarp
    speed = distance * frame_rate
    return speed

# Video dosyasını açın veya kamera bağlantısını başlatın
camera = cv2.VideoCapture("/Users/sumeyye/Desktop/imageProcesswork/vid_2.avi")

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Görüntü üzerinde kırmızı top tespiti işlemlerini gerçekleştir
    detected_frame = detect_billiard_balls(frame)

    # Şu anki zamanı al
    current_time = datetime.now()

    # Eğer ilk zaman damgası yoksa veya listemiz boşsa, zamanı güncelle ve devam et
    if prev_time is None or len(red_ball_trajectory) == 0:
        prev_time = current_time
        continue

    # Son iki merkez noktasını al
    # Çünkü iki merke arasındaki piksel sayısını geçen zamana böldüğümüzde istediğimiz hız değeri elde ediliyor
    last_center = red_ball_trajectory[-1]
    second_last_center = red_ball_trajectory[-2]

    # İki konum arasındaki mesafeyi hesapla (Piksel cinsinden)
    distance_pixels = np.linalg.norm(np.array(last_center) - np.array(second_last_center))

    # İki zaman damgası arasındaki geçen süreyi hesapla (saniye cinsinden)
    time_difference = (current_time - prev_time).total_seconds()

    # Kırmızı topun hızını hesapla (Piksel/saniye)
    if time_difference > 0:
        speed_pixels_per_second = calculate_speed(second_last_center, last_center, frame_rate=30)
        speed_text = f"Hiz: {speed_pixels_per_second:.2f} piksel/s"
        print("Kırmızı Topun Hızı (Piksel/saniye):", speed_pixels_per_second)

        # Hız bilgisini topun etrafına yazdır
        cv2.putText(detected_frame, speed_text, (last_center[0] - 50, last_center[1] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Önceki zaman damgasını güncelle
    prev_time = current_time

    # Kırmızı topun hareket izini çiz
    for i in range(1, len(red_ball_trajectory)):
        cv2.line(detected_frame, red_ball_trajectory[i - 1], red_ball_trajectory[i], (0, 0, 255), 2)

    # İşlenmiş kareyi ekranda göster
    cv2.imshow("Detected Red Ball", detected_frame)

    # 'q' tuşuna basıldığında çıkış yap
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Video yakalama nesnesini serbest bırak
camera.release()

# Tüm pencereleri kapat
cv2.destroyAllWindows()

if white_start and white_stopped_time:
    time_difference = (white_stopped_time - white_start).total_seconds()
    print(f"Beyaz top vurulma anı: {white_start}")
    print(f"Beyaz topun durma anı: {white_stopped_time}")
    print(f"Toplam süre (saniye): {time_difference:.2f}")
