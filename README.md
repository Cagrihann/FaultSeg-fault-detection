# FaultSeg-fault-detection
Bu proje, FaultSeg veri seti ile tren tekerleği kusurlarını YOLOv11 kullanarak tespit etmektedir.
Veri seti: https://universe.roboflow.com/zakir-shaikh/wheel-defect-detecion-faultseg

##  Kullanılan Yöntem
- Model: YOLOv11 (Ultralytics)
- Eğitim: Roboflow'dan indirilen etiketli görseller kullanılarak gerçekleştirilmiştir.
- Sınıflar: Wheel, Shelling, Cracks-Scratches, Discoloration

##  Örnek Tahmin Sonucu
Aşağıda modelin test sırasında ürettiği örnek bir tahmin görseli yer almaktadır:


![test](https://github.com/user-attachments/assets/9dc30af0-82c3-406f-a9ee-0c6412969a7e)
