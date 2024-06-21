"""👉 Day 94 Challenge
Today's challenge is to combine the two APIs to make something cool.

Your program should:

1. Get all the news stories for the day from NewsAPI.
2. Send off a request to openai to summarize the stories.
3. Make a simple command line program that gives you 5 top news stories for the day whenever you click run.

Hints:
Send off a prompt to openai that says 'summarize' and includes the URL of the story to be summarized.

https://newsapi.org/
https://openai.com/

https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes
"""

# WIP - Se me venció la OpenAI access :(


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
