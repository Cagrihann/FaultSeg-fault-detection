import pandas as pd
import cv2 as cv
import os 
from ultralytics import YOLO

def test_visualize():
    test_annotations_path = "annotations/test_annotations.csv"
    df = pd.read_csv(test_annotations_path)
    test_images = "data/test/images"
    for filename in df["filename"].unique():
        image_path = os.path.join(test_images, filename)
        img = cv.imread(image_path)
        results = trained_model(image_path)
        results[0].show()
        boxes = df[df["filename"] == filename]
        for _, row in boxes.iterrows():
            xmin, ymin, xmax, ymax = int(row["xmin"]), int(row["ymin"]), int(row["xmax"]), int(row["ymax"])
            class_name = row["class"]
            
            cv.rectangle(img, (xmin,ymin), (xmax, ymax), (0,255,0), 2)
            cv.putText(img, class_name, (xmin, ymin + 10), cv.FONT_HERSHEY_TRIPLEX, 0.3, (0, 0, 255), 1)
        cv.imshow(f"Real Faults For {filename}", img)
        cv.waitKey(0)
    cv.destroyAllWindows()



trained_model = YOLO("runs/detect/train/weights/best.pt")

if __name__ == "__main__":         
    metrics = trained_model.val()
    print(f"\n\n\n{metrics}")
    test_visualize()