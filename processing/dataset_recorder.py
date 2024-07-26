import os
import cv2
from datetime import datetime


class DatasetRecorder:
    """
    The DatasetRecorder class saves image frames to a designated directory at regular time intervals.

    :param output_dir: Directory where images and labels will be saved.
    :param save_interval_ms: Time interval in milliseconds that determines how often frames should be saved.
    """

    def __init__(self, output_dir="dataset", save_interval_ms=1000):
        self.output_dir = output_dir
        self.frame_counter = 0
        self.save_interval_ms = save_interval_ms
        self.last_save_time = None

        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def save_frame(self, img, label=None):
        """
        Saves an image frame to the directory if the specified time interval has elapsed since the last save.

        :param img: The image to be saved.
        :param label: Optional label to be saved along with the image.
        """
        current_time = datetime.now()

        # Check if the required time interval has passed since the last save
        if self.last_save_time is None or (current_time - self.last_save_time).total_seconds() * 1000 >= self.save_interval_ms:
            self.frame_counter += 1
            timestamp = current_time.strftime("%Y%m%d_%H%M%S")
            img_filename = os.path.join(self.output_dir, f"frame_{timestamp}.jpg")
            cv2.imwrite(img_filename, img)

            if label:
                label_filename = os.path.join(self.output_dir, f"frame_{timestamp}.txt")
                with open(label_filename, 'w') as label_file:
                    label_file.write(label)

            self.last_save_time = current_time

