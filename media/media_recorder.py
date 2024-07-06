from aiortc.contrib.media import MediaRecorder

class CustomMediaRecorder(MediaRecorder):
    def __init__(self, file, options=None):
        super().__init__(file, options)

    def start_recording(self, track):
        self.addTrack(track)
        self.start()

    def stop_recording(self):
        self.stop()
