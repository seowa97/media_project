from requests import post, get
import json

watched_list = []

api_key = "0d23500f316d7c4006e4f5405f795c8d"
url = "https://api.themoviedb.org/3/movie/343611?api_key=" + api_key


res = get(url)
res.raise_for_status()



