import torch
from pathlib import Path
import cv2
import pandas as pd
import matplotlib.pyplot as plt

class YOLODetection:
    def __init__(self, image_folder, output_folder='../scripts/photos/detection_results/'):
        self.image_folder = Path(image_folder)
        self.output_folder = Path(output_folder)
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        self.output_folder.mkdir(parents=True, exist_ok=True)
    
    def filter_images(self, channel_name='lobelia4cosmetics'):
        # Filter images by channel name
        image_paths = list(self.image_folder.glob(f'*{channel_name}*.jpg'))
        return image_paths
    
    def run_detection(self, img_path):
        # Run YOLO detection on a single image
        img = cv2.imread(str(img_path))
        results = self.model(img)
        return results
    
    def save_detection_results(self, img_path, results):
        # Save detection results as CSV
        detections = results.pandas().xyxy[0]
        output_file = self.output_folder / f"{img_path.stem}_detections.csv"
        detections.to_csv(output_file, index=False)
        print(f"Saved detection results for {img_path.name} to {output_file}")
    
    def visualize_detection(self, results):
        # Visualize detection results
        img_with_detections = results.render()[0]
        plt.imshow(cv2.cvtColor(img_with_detections, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.show()
    
    def detect_and_save(self, channel_name='lobelia4cosmetics', max_images=50):
        # Filter and run detection on the first specified number of images from the channel
        image_paths = self.filter_images(channel_name)
        print(f"Number of images from @{channel_name}: {len(image_paths)}")
        
        for idx, img_path in enumerate(image_paths):
            if idx >= max_images:  # Process only the first 'max_images' images
                break
            
            results = self.run_detection(img_path)
            self.save_detection_results(img_path, results)
            print(f"Detection completed for {img_path.name}")
    
    def detect_and_visualize(self, channel_name='lobelia4cosmetics', max_images=50):
        # Detect and visualize detection results for the first image from the specified channel
        image_paths = self.filter_images(channel_name)
        if len(image_paths) > 0:
            for idx, img_path in enumerate(image_paths):
                if idx >= max_images:  # Process only the first 'max_images' images
                    break
                
                results = self.run_detection(img_path)
                self.visualize_detection(results)
        else:
            print(f"No images found for @{channel_name}")


