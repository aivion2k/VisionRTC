import os
import cv2
from datetime import datetime

class DatasetRecorder:
    def __init__(self, output_dir="dataset"):
        self.output_dir = output_dir
        self.frame_counter = 0

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def save_frame(self, img, label=None):
        self.frame_counter += 1
        frame_datetime = datetime.now()
        img_filename = os.path.join(self.output_dir, f"frame_{frame_datetime}.jpg")
        cv2.imwrite(img_filename, img)

        if label:
            label_filename = os.path.join(self.output_dir, f"frame_{frame_datetime}.txt")
            with open(label_filename, 'w') as label_file:
                label_file.write(label)
