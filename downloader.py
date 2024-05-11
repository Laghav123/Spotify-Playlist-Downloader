import yt_links
from pytube import YouTube

def download(id):
    links = yt_links.give_yt_links(id)

    for link in links:
        yt = YouTube(link)
        print("Downloading " + yt.title + " from " + link)
        stream = yt.streams.filter(only_audio=True).first()

        stream.download("./downloads")
        print("Downloaded " + yt.title)

    print("Find all successful downloads in './downloads' folder. Enjoy ✔️✔️✔️✔️✔️✔️")
