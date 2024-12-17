import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import spotipy


def get_liked_songs():
    results = sp.current_user_saved_tracks()
    liked_songs = results["items"]

    while results["next"]:
        results = sp.next(results)
        liked_songs.extend(results["items"])

    return liked_songs


load_dotenv()


# Set up Spotipy client
scope = "user-library-read playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Retrieve all liked songs
liked_songs = get_liked_songs()

# Filter songs released in 2024
filtered_tracks = []
for item in liked_songs:
    track = item["track"]
    release_date = track["album"].get("release_date", "")
    print(f"Track: {track['name']}, Release Date: {release_date}")
    if release_date and release_date.startswith("2024"):
        filtered_tracks.append(track["uri"])
        print(f"Added to playlist: {track['name']}")

if not filtered_tracks:
    print("No tracks released in 2024 found in your 'Liked Songs'.")
    exit()

# Create a new playlist with the filtered tracks
user_id = sp.me()["id"]
new_playlist = sp.user_playlist_create(user_id, name="LikedIn2024", public=False)

# Add tracks to the playlist in chunks of 100
chunk_size = 100
for i in range(0, len(filtered_tracks), chunk_size):
    chunk = filtered_tracks[i : i + chunk_size]
    sp.playlist_add_items(new_playlist["id"], chunk)

print("New playlist 'LikedIn2024' has been created with the filtered tracks.")
