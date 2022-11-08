import requests


chunk_size = 256

# https://cdn.fs.teachablecdn.com/4w1ZgXURcuzea8j0LDVh

# https://cdn.fs.teachablecdn.com/hGDvx8kiSDKjgma6vAgq

url = "https://cdn.fs.teachablecdn.com/4w1ZgXURcuzea8j0LDVh"

r = requests.get(url, stream=True)

with open("name", "wb") as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)