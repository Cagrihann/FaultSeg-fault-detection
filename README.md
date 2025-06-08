# FaultSeg-fault-detection

This project aims to detect train wheel defects with FaultSeg dataset and YOLOv11.

Dataset: https://universe.roboflow.com/zakir-shaikh/wheel-defect-detecion-faultseg

- Model: YOLOv11 (Ultralytics)
- Training data: Labeled images downloaded from Roboflow
- Classes: Wheel, Shelling, Cracks-Scratches, Discoloration

## Example Prediction Output

Below is a sample prediction result obtained during testing:

![test](https://github.com/user-attachments/assets/9dc30af0-82c3-406f-a9ee-0c6412969a7e)

## Library Versions Used

- Python: 3.10  
- Ultralytics (YOLOv11): 8.3.151  
- PyTorch: 2.7.1+cu118  
- OpenCV: 4.8.1  
- NumPy: 1.24.4  
- Pandas: 2.3.0
