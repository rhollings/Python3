"""
Different urls for certain data
url = https://animechan.vercel.app/api/random = calls a random quote
url = https://animechan.vercel.app/api/quotes = calls ten random quotes
url = https://animechan.vercel.app/api/quotes/anime?title=naruto = quotes by anime title
url = https://animechan.vercel.app/api/quotes/character?name=saitama = quotes by character 
url = https://animechan.vercel.app/api/available/anime = all available anime
"""
#lets allow options for different outputs
#ask for who/what anime/character

import urllib.request, json

url = "https://animechan.vercel.app/api/random"
url2 = "https://animechan.vercel.app/api/available/anime"


response = urllib.request.urlopen(url)
data = json.loads(response.read())
name = data["character"]
anime = data["anime"]
quote = data["quote"]


#print("In the anime", anime, ",", name, "said", quote)

