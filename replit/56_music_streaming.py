"""
Music Streaming Service
Today is a project day where you will be using your newly acquired csv reading and file management powers to work with data about a music streaming service.

Now head over to the challenge page for the details.

👉 Day 56 Challenge
I've included a csv file ('100MostStreamedSongs.csv') in this repl that contains data from a music streaming service.

Your program should:
1. Read in the data.
2. Categorize the songs by artist, like this:
    i. Create one empty folder per artist.
    ii. Create one blank text file per song by that artist in the relevant folder. The file name of the text file should be the name of the song.

Hints:
* For each artist, check the directory to see if they already have a folder. If they do, use it. If not, create it.
"""

import os, time, csv

# Special Characters
special_char = [
    "!",
    '"',
    "#",
    "$",
    "%",
    "&",
    "'",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "`",
    "{",
    "|",
    "}",
    "~",
    "”",
]

print("MUSIC SORTING SYSTEM")

time.sleep(1)
print("Your files are beeng sorted...")

# Creates a folder for '56_Music_Striming'
main_folder = "56_Music_Striming"

if main_folder not in os.listdir():
    os.mkdir(main_folder)

try:
    with open("100MostStreamedSongs.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:

            # Creates a folder per Artist
            artist = row["Artist(s)"]
            artist_folder = os.path.join(main_folder, artist)

            if artist not in os.listdir(main_folder):
                os.mkdir(artist_folder)

            # Creates an empty text file per song within that folder
            song = row["Song"]
            for char in special_char:
                song = song.replace(char, "")

            filename = os.path.join(artist_folder, f"{song}.txt")
            if filename not in os.listdir(artist_folder):
                f = open(filename, "w")
                f.write(f"{song}")
                f.close()
    time.sleep(1)
    print("Your files have been sorted successfully.")

except Exception as err:
    time.sleep(1)
    print("An error has occured: ", err)
