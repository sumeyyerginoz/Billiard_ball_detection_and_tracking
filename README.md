# Billiard_ball_detection_and_tracking


Bu Python kodu, bir video akışındaki bilardo toplarının hareketini izlemek için OpenCV kütüphanesini kullanır. Betiğimiz kırmızı bir topun izini sürerken aynı zamanda beyaz topun hareketini de tespit eder. Ayrıca, kırmızı topun hızını izlediği yol üzerinden hesaplar.

## Gereksinimler

Sisteminizde Python kurulu olduğundan emin olun. Ayrıca aşağıdaki kütüphanelere ihtiyacınız olacak:

OpenCV (cv2)
NumPy
## Kurulum

Gerekli kütüphaneleri pip kullanarak yükleyebilirsiniz:
pip install opencv-python numpy
## Kullanım

Bu depoyu klonlayın veya billiard_ball_tracking.py adlı kodu indirin.
Bir bilardo topu hareketini içeren bir video dosyanızın olduğundan emin olun. Ayrıca bir canlı kamera akışını da kullanabilirsiniz.
Betiği video dosyanızın yolunu parametre olarak vererek çalıştırın:

python billiard_ball_tracking.py /path/to/your/video/file.avi
kod, algılanan kırmızı topun izini gösteren bir pencere açacaktır. Kırmızı topun hızı terminalde yazdırılacaktır.
Video akışından çıkmak için 'q' tuşuna basın.
## Çıktı

kod, algılanan kırmızı topun izini üzerine yerleştirilmiş video akışını gösterir.
Terminalde kırmızı topun hızını piksel/saniye cinsinden yazdırır.
Eğer beyaz top algılanırsa, vurulduğu zamanı ve durduğu zamanı, hareketin toplam süresiyle birlikte yazdırır.
Özelleştirme

detect_billiard_balls fonksiyonundaki min_area ve max_area değişkenlerini ayarlayarak gürültüyü filtreleyebilir ve farklı boyutlardaki bilardo toplarını doğru bir şekilde algılayabilirsiniz.
Kırmızı topları algılamak için renk aralıklarını (lower_red1, upper_red1, lower_red2, upper_red2) değiştirebilirsiniz.
calculate_speed fonksiyonundaki frame_rate parametresini değiştirerek hız hesaplamasını videonuzun kare hızına göre ayarlayabilirsiniz.
### Kırmızı topun hareketinin izlemesi
<img width="643" alt="Ekran Resmi 2024-04-24 13 42 17" src="https://github.com/sumeyyerginoz/Billiard_ball_detection_and_tracking/assets/112480236/38583af7-4f60-4127-b25e-e43c02d44463">
<img width="649" alt="Ekran Resmi 2024-04-24 13 41 51" src="https://github.com/sumeyyerginoz/Billiard_ball_detection_and_tracking/assets/112480236/d05205f2-5c0a-4272-8cda-069b75b36a2b">
<img width="645" alt="Ekran Resmi 2024-04-24 13 41 27" src="https://github.com/sumeyyerginoz/Billiard_ball_detection_and_tracking/assets/112480236/5a133c8f-83b0-4d77-aef5-7ba3903d19e7">
<br>
<img width="409" alt="Ekran Resmi 2024-04-24 13 44 23" src="https://github.com/sumeyyerginoz/Billiard_ball_detection_and_tracking/assets/112480236/0cbfe9b4-7dbd-49ef-a9fb-65c4eb5153db">
<img width="447" alt="Ekran Resmi 2024-04-24 13 44 47" src="https://github.com/sumeyyerginoz/Billiard_ball_detection_and_tracking/assets/112480236/50c23751-eb5d-47f2-ac05-eb4beed07ee0">
