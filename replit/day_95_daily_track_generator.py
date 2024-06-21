"""
👉 Day 95 Challenge
Today's challenge is to create a daily track generator.

Your program should:

1. Pull in 5 of the most recent news stories in your area. (You could also specify a category here to avoid all the depressing stuff out there.)
2. Ask openai to summarise each story in two to three words.
3. Pass those words to Spotify in a search. Show and give a sample of each song.
4. No need to build this in Flask today. A command line program is just fine. The console should display:
    i. The name of each track (five tracks)
    ii. The prompt words used for the search
    iii. The URL to get the sample

Hints:
* Don't forget your secrets.
* You can ask openai to summarize in pretty much plain text. 
  Try this prompt = (f'''Summarize {article["url"]} in no more than four words.''')
"""

# WIP - RENOVAR LA LICENCIA DE OPENAI

import json, os, requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

# Load .env
load_dotenv()

# Spotify
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


# News and OpenAI
"""
import json, os, requests
from dotenv import load_dotenv

# from openai import OpenAI

# import openai

load_dotenv()

# Secret Keys
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
ORGANIZATION_ID = os.environ.get("ORGANIZATION_ID")


headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
# client = OpenAI(
#     organization=ORGANIZATION_ID,
# )

# country = "us"  # USA
country = "mx"  # Mexico
# country = "sv"  # El Salvador
# country = "de"  # Deutschland

url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={NEWS_API_KEY}"

resuls = requests.get(url)
data = resuls.json()


for article in data["articles"]:
    print(article["title"], end="\n")
    print(article["url"], end="\n")
    print(article["content"], end="\n")
    print()

print(json.dumps(data, indent=2))

# response = client.chat.completions.create(
#     model="gpt-3.5-turbo-0125",
#     response_format={"type": "json_object"},
#     messages=[
#         {
#             "role": "system",
#             "content": "You are a helpful assistant designed to output JSON.",
#         },
#         {"role": "user", "content": "Who won the world series in 2020?"},
#     ],
# )
# print(response.choices[0].message.content)

"""
