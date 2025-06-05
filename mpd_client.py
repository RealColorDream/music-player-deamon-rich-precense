from mpd import MPDClient

class Interface:
    def __init__(self, host: str = "localhost", port: int = 6600):
        self.client = MPDClient()
        self.client.timeout = 10
        self.client.connect(host, port)

    def get_song(self) -> str:
        status = self.client.status()
        song = self.client.currentsong()

        if song:
            elapsed_time = float(status["elapsed"])
            duration = float(status["duration"])
            elapsed_minutes = int(elapsed_time // 60)
            elapsed_seconds = int(elapsed_time % 60)

            duration_minutes = int(duration // 60)
            duration_seconds = int(duration % 60)

            elapsed_time_formatted = f"{elapsed_minutes}:{elapsed_seconds:02}"
            duration_time_formatted = f"{duration_minutes}:{duration_seconds:02}"

            return f"[{song['title']} | {song['album']} ({elapsed_time_formatted} / {duration_time_formatted})] by {song['artist']}"
        else:
            return "No song is currently playing."