from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotipy


load_dotenv()

scope = "playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlists_dict: dict = sp.current_user_playlists()

playlists = {}
while playlists_dict:
    for nomade_pl in playlists_dict["items"]:
        playlists[nomade_pl["name"]] = nomade_pl
    if playlists_dict["next"]:
        playlists_dict = sp.next(playlists_dict)
    else:
        playlists_dict = None

# %%

nomade = [name for name in playlists if name.startswith("Nomad")]
nomade_meta = playlists[nomade[0]]

nomade_pl = sp.playlist(nomade_meta["id"])

tracks = nomade_pl['tracks']['items']
with open('nomade.txt', 'w') as f:
    for track in tracks:
        artist_name = track['track']['artists'][0]['name']
        track_name = track['track']['name']
        f.write(f"{artist_name} {track_name}\n")