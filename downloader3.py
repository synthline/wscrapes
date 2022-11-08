import requests
import shutil

url="https://cdn.fs.teachablecdn.com/4w1ZgXURcuzea8j0LDVh"

def download_file(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename