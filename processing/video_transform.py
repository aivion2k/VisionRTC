from aiortc import MediaStreamTrack
from aiortc.contrib.media import MediaRelay
from av import VideoFrame
from processing.dataset_recorder import DatasetRecorder
from processing.image_processor import ImageProcessor, cartoon_method

relay = MediaRelay()


class VideoTransformTrack(MediaStreamTrack):
    """
    The VideoTransformTrack class extends MediaStreamTrack to apply transformations to video frames and optionally save them as a dataset.

    :param track: The original media track to transform.
    :param transform: The name of the transformation method to apply.
    :param if_create_dataset: A boolean indicating whether to create a dataset by saving frames.
    :param save_interval_ms: Time interval in milliseconds for saving frames to the dataset.
    """

    kind = "video"

    def __init__(self, track, transform, if_create_dataset, save_interval_ms=1000):
        super().__init__()
        self.track = track
        self.method = transform
        self.create_dataset = if_create_dataset
        self.dataset_recorder = DatasetRecorder("dataset", save_interval_ms)
        self.processor = ImageProcessor()

        """
        Register your image processing methods/models below
        """
        self.processor.register_method("cartoon", cartoon_method)

    def prepare_img(self, frame):
        """
        Convert a video frame to a NumPy array.

        :param frame: The input video frame.
        :return: The frame as a NumPy array in BGR format.
        """
        return frame.to_ndarray(format="bgr24")

    def prepare_frame(self, img, frame):
        """
        Convert a NumPy array back to a video frame.

        :param img: The processed image as a NumPy array.
        :param frame: The original video frame.
        :return: A new VideoFrame with the processed image data.
        """
        new_frame = VideoFrame.from_ndarray(img, format="bgr24")
        new_frame.pts = frame.pts
        new_frame.time_base = frame.time_base
        return new_frame

    def process_frame(self, img):
        """
        Apply the registered transformation method to an image.

        :param img: The input image as a NumPy array.
        :return: The processed image.
        """
        return self.processor.apply_method(img, self.method)

    async def recv(self):
        """
        Receive a video frame, apply the transformation, optionally save it, and return the processed frame.

        :return: The transformed video frame.
        """
        frame = await self.track.recv()
        if self.method == "none":
            return frame

        img = self.prepare_img(frame)
        img = self.process_frame(img)
        frame = self.prepare_frame(img, frame)

        if self.create_dataset:
            label = "bbox: (0, 0, 100, 100)"  # Placeholder for actual label generation
            self.dataset_recorder.save_frame(img, label)

        return frame
