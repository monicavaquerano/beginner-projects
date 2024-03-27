"""
# JaSON
👉 Day 90 Challenge
Today's challenge is to use the code you've just seen to pull in data for 10 users using randomuser.me again.
Your program should:
1. Save the medium quality version of the profile pic as a local file named {firstName} {lastName}.jpg.
2. Each picture should be saved to a different file.
Hints:
* Use a for loop to send 10 requests, eg: for person in user["results"]:
"""

import json, os, requests

folder = "day_90_users_pics"

if folder not in os.listdir():
    os.mkdir(folder)

x = 0
print("Your files are being created...")

while x < 10:
    # Call to API
    result = requests.get("https://randomuser.me/api/")

    if result.status_code != 200:
        print("Error: Couldn't get API")
        break
    else:
        # Get user information
        user = result.json()

        for person in user["results"]:
            first_name = person["name"]["first"].lower()
            last_name = person["name"]["last"].lower()
            image = person["picture"]["large"]

        filename = f"{first_name}_{last_name}.jpg"

        if filename in os.listdir(folder):
            pass
        else:
            print(f"Saved {filename}")
            filename = os.path.join(folder, filename)
            picture = requests.get(image)

            # Create user image
            with open(filename, "wb") as f:
                f.write(picture.content)

        x += 1
print("Done!")
