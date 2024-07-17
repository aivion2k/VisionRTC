import cv2
from aiortc import MediaStreamTrack
from aiortc.contrib.media import MediaRelay
from av import VideoFrame
from processing.dataset_recorder import DatasetRecorder
from processing.image_processor import ImageProcessor, cartoon_method

relay = MediaRelay()


class VideoTransformTrack(MediaStreamTrack):
    kind = "video"

    def __init__(self, track, transform, create_dataset):
        super().__init__()
        self.track = track
        self.method = transform
        self.create_dataset = create_dataset
        self.dataset_recorder = DatasetRecorder("dataset")
        self.processor = ImageProcessor()
        self.processor.register_method("cartoon", cartoon_method)

    def prepare_img(self, frame):
        return frame.to_ndarray(format="bgr24")

    def prepare_frame(self, img, frame):
        new_frame = VideoFrame.from_ndarray(img, format="bgr24")
        new_frame.pts = frame.pts
        new_frame.time_base = frame.time_base
        return new_frame

    def process_frame(self, img):
        return self.processor.apply_method(img, self.method)

    async def recv(self):
        frame = await self.track.recv()
        img = self.prepare_img(frame)
        img = self.process_frame(img)
        frame = self.prepare_frame(img, frame)

        # Convert VideoFrame to numpy array and save the image
        if self.create_dataset:
            label = "bbox: (0, 0, 100, 100)"  # Placeholder for actual label generation
            self.dataset_recorder.save_frame(img, label)

        return frame