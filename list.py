from spotipy.oauth2 import SpotifyOAuth
import spotipy

# Load environment variables and set up Spotipy client
scope = "playlist-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Fetch the current user's playlists
playlists = sp.current_user_playlists()

# List playlists and their IDs
print("Your Playlists:")
while playlists:
    for playlist in playlists["items"]:
        print(f"Name: {playlist['name']}, ID: {playlist['id']}")
    if playlists["next"]:
        playlists = sp.next(playlists)
    else:
        playlists = None
