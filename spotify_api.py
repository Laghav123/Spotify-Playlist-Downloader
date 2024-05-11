import requests


client_id = "16a01dd4d29846739ea27d79e865e547"
client_secret = "1fe4f651aa6c4eed8321345bc3d091e3"

def getBearer():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()["access_token"]

def handleResponse(response):
    yt_queries = []
    items = response.json()['items']
    for item in items:
        song_name = item['track']['name']
        artists = ""
        for artist in item['track']['artists']:
            artists += artist['name'] + ' '
        query = song_name + " " + artists
        yt_queries.append(query)
    
    return yt_queries


def giveSongQueries(arg):
    # %28  =  (
    # %29  =  )
    # %2C  =  ,
    fields = "fields=items%28track%28name%2C+artists%28name%29%29%29'"
    # limit = "limit=10"
    url = "https://api.spotify.com/v1/playlists/" + arg + "/tracks" + "?" + fields 
    auth = "Bearer " + getBearer()
    headers = { "Authorization" : auth}
    response = requests.get(url, headers=headers)
    
    print("Playlist Fetched ✔️✔️✔️")
    return handleResponse(response)

