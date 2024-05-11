import requests
import spotify_api

API_KEY = 'AIzaSyBfPAf_SBQIQ3NwHd0aHCgYuY7laWeps54'

endpoint = 'https://www.googleapis.com/youtube/v3/search'



def give_yt_links(spotify_playlist_id):
    yt_queries = spotify_api.giveSongQueries(spotify_playlist_id)
    yt_links = []

    for query in yt_queries:
        params = {
            'part': 'snippet',
            'q': query,
            'key': API_KEY
        }

        response = requests.get(endpoint, params=params)
        
        if response.status_code == 200:

            data = response.json()
            item = data['items'][0]
            video_id = item['id']['videoId']
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            
            yt_links.append(video_url)
            print("Link for " + query + " received ✔️")
        else:
            print("Failed to retrieve youtube link for " + query)
    
    print("All Links Fetched ✔️✔️✔️")
    return yt_links
    
    