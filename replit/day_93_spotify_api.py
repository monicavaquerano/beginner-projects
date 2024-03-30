import json, os, requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load .env
load_dotenv()

# Access secret keys
clientID = os.environ.get("CLIENT_ID")
clientSecret = os.environ.get("CLIENT_SECRET")

url = "https://accounts.spotify.com/api/token"

# Get Authentication
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret)

response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]
headers = {"Authorization": f"Bearer {accessToken}"}
# print(response.ok)
# print(response.json())
# print(response.status_code)

db = {}
"""
<iframe style="border-radius:12px" 
    src="https://open.spotify.com/embed/track/6tNQ70jh4OwmPGpYy6R2o9?utm_source=generator" 
    width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; 
    encrypted-media; fullscreen; picture-in-picture" loading="lazy">
</iframe>

<iframe style="border-radius:12px" 
    src="https://open.spotify.com/embed/track/6tNQ70jh4OwmPGpYy6R2o9?utm_source=generator&theme=0" 
    width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; 
    encrypted-media; fullscreen; picture-in-picture" loading="lazy">
</iframe>

"""


# Seach Year
def search_year(year, offset):
    url_search = "https://api.spotify.com/v1/search"
    try:
        offset = db[year]
        if offset > 200:
            db[year] = 0
        db[year] += 10
    except:
        db[year] = 10
    search = f"?q=year%3A{year}&type=track&limit=10&offset={offset}"
    fullURL = f"{url_search}{search}"
    return fullURL


# Search Artist
def search_artist(artist, offset):
    artist = artist.replace(" ", "%20")
    try:
        offset = db[artist]
        if offset > 200:
            db[artist] = 0
        db[artist] += 10
    except:
        db[artist] = 10
    url_search = "https://api.spotify.com/v1/search"
    search = f"?q=artist%3A{artist}&type=track&limit=10&offset={offset}"
    fullURL = f"{url_search}{search}"
    return fullURL


# Read JSON
def read_search(data):
    for track in data["tracks"]["items"]:
        track_name = track["name"]
        artists = track["artists"][0]["name"]
        album_name = track["album"]["name"]
        release_date = track["album"]["release_date"]
        preview_url = track["preview_url"]
        print(
            f"- Song: {track_name}\n- Artist: {artists}\n- Album: {album_name}\n- Preview URL: {preview_url if preview_url != None else 'No preview available'}\n- Release Date: {release_date}\n"
        )


# Top 50 Global
def get_top_50():
    fullURL = "https://api.spotify.com/v1/playlists/37i9dQZEVXbMDoHDwVN2tF"
    return fullURL


while True:
    title = f"{'Spotify API':~^30}"
    print(title)
    choice = (
        input("Look by:\n(y)ear, (a)rtist, (t)op 50 global, (e)xit\n> ").strip().lower()
    )
    os.system("clear")
    if choice[0] == "y":
        # For songs by year
        title = f"{'Songs by year':~^30}"
        print(title)
        year = input("Year: ")
        offset = 0
        response = requests.get(search_year(year, offset), headers=headers)
        data = response.json()
        read_search(data)
    elif choice[0] == "a":
        # For songs by artist
        title = f"{'Songs by artist':~^30}"
        print(title)
        artist = input("Artist(s): ").strip().lower()
        offset = 0
        response = requests.get(search_artist(artist, offset), headers=headers)
        data = response.json()
        read_search(data)
    elif choice[0] == "t":
        # For Top 50 Global
        title = f"{'Top 50 Global':~^30}"
        print(title)
        response = requests.get(get_top_50(), headers=headers)
        data = response.json()
        songs = data["tracks"]["items"]
        top = 0
        for song in songs:
            top += 1
            track_name = song["track"]["name"]
            artists = song["track"]["artists"][0]["name"]
            album_name = song["track"]["album"]["name"]
            release_date = song["track"]["album"]["release_date"]
            preview_url = song["track"]["preview_url"]
            print(
                f"TOP {top:>5}\n- Song: {track_name}\n- Artist: {artists}\n- Album: {album_name}\n- Preview URL: {preview_url if preview_url != None else 'No preview available'}\n- Release Date: {release_date}\n"
            )
    elif choice[0] == "e":
        print(f"\n{'Bye':~^30}")
        break
