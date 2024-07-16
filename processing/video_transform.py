import cv2
from aiortc import MediaStreamTrack
from aiortc.contrib.media import MediaRelay
from av import VideoFrame

relay = MediaRelay()


class VideoTransformTrack(MediaStreamTrack):
    kind = "video"

    def __init__(self, track, transform):
        super().__init__()
        self.track = track
        self.transform = transform

    def process_frame(self, frame):
        img = frame.to_ndarray(format="bgr24")

        if self.transform == "cartoon":
            img_color = cv2.pyrDown(cv2.pyrDown(img))
            for _ in range(6):
                img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
            img_color = cv2.pyrUp(cv2.pyrUp(img_color))
            img_edges = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            img_edges = cv2.adaptiveThreshold(
                cv2.medianBlur(img_edges, 7),
                255,
                cv2.ADAPTIVE_THRESH_MEAN_C,
                cv2.THRESH_BINARY,
                9,
                2,
            )
            img_edges = cv2.cvtColor(img_edges, cv2.COLOR_GRAY2RGB)
            img = cv2.bitwise_and(img_color, img_edges)
        elif self.transform == "edges":
            img = cv2.cvtColor(cv2.Canny(img, 100, 200), cv2.COLOR_GRAY2BGR)
        elif self.transform == "rotate":
            rows, cols, _ = img.shape
            M = cv2.getRotationMatrix2D((cols / 2, rows / 2), frame.time * 45, 1)
            img = cv2.warpAffine(img, M, (cols, rows))

        new_frame = VideoFrame.from_ndarray(img, format="bgr24")
        new_frame.pts = frame.pts
        new_frame.time_base = frame.time_base
        return new_frame

    async def recv(self):
        frame = await self.track.recv()
        frame = self.process_frame(frame)

        # Convert VideoFrame to numpy array and save the image
        img = frame.to_ndarray(format="bgr24")
        cv2.imwrite(f"media/image{frame.time_base}.jpg", img)

        return frame
