import time
from mpd_client import Interface
from pypresence import Presence
from dotenv import dotenv_values

config = dotenv_values(".env")

client_mpd = Interface()

client_id = config.get("CLIENT_ID")
RPC = Presence(client_id)
RPC.connect()

while True:
    current_song = client_mpd.get_song()
    RPC.update(
        large_image=(
            "image"
        ),
        details="Currently playing:",
        state=current_song,
    )

    print(current_song)
    time.sleep(13)
