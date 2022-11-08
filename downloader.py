import urllib

video_links= 'https://cdn.fs.teachablecdn.com/4w1ZgXURcuzea8j0LDVh'

def download_video_series(video_links): 

for link in video_links: 

    '''iterate through all links in video_links 
    and download them one by one'''

    # obtain filename by splitting url and getting  
    # last string 
    file_name = link.split('/')[-1]    

    print "Downloading file:%s"%file_name 

    # create response object 
    r = requests.get(link, stream = True) 

    # download started 
    with open(file_name, 'wb') as f: 
        for chunk in r.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk) 

    print "%s downloaded!\n"%file_name 

print "All videos downloaded!"
return