from aiortc.contrib.media import MediaBlackhole

class CustomMediaBlackhole(MediaBlackhole):
    def __init__(self):
        super().__init__()

    def simulate_recording(self, track):
        self.addTrack(track)

