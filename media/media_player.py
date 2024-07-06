from aiortc.contrib.media import MediaPlayer

class CustomMediaPlayer(MediaPlayer):
    def __init__(self, source, options=None):
        super().__init__(source, options)

    def play_audio(self, audio_file):
        self.audio = MediaPlayer(audio_file).audio

