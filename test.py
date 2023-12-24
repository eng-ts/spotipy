from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import spotipy

def get_all_tracks(uri):
    results = sp.playlist_tracks(uri)
    tracks = results['items']
    
    # Paginate through the tracks
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    
    return tracks


load_dotenv()

scope = "playlist-read-private playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

playlist_uri = 'spotify:playlist:20374KDziRjZ81OP16ydtc'

all_tracks = get_all_tracks(playlist_uri)

# Filter tracks released in 2023
filtered_tracks = []
for item in all_tracks:
    track = item['track']
    release_date = track['album'].get('release_date', '')
    if release_date and release_date.startswith('2023'):
        filtered_tracks.append(track['id'])

# Create a new playlist with the filtered tracks
user_id = sp.me()['id']
new_playlist = sp.user_playlist_create(user_id, name='2023 Releases Playlist', public=False)

# Add the filtered tracks to the new playlist
sp.playlist_add_items(new_playlist['id'], filtered_tracks)

print("New playlist '2023 Releases Playlist' has been created with the filtered tracks.")
