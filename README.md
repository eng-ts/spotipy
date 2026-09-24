# spotipy-pakite

Small scripts against the Spotify Web API via [spotipy](https://spotipy.readthedocs.io/).

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```sh
uv sync
```

Create a `.env` with your Spotify app credentials:

```
SPOTIPY_CLIENT_ID=...
SPOTIPY_CLIENT_SECRET=...
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

## Usage

```sh
uv run list.py     # export a playlist starting with "magiciens" to magiciens.txt
uv run filter.py   # create a private "LikedIn2024" playlist from liked songs released in 2024
```

The first run opens a browser for OAuth; the token is cached in `.cache` (git-ignored).
