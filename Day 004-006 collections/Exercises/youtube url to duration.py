import csv
from pytube import YouTube


path = "watch-history  to pycharm.csv"
file = open(path, newline='')  # Depending on the system strings will end with \n or \r
reader = csv.reader(file)

data = []
for line in reader:
    data.append(line[0])

time_spent_on_youtube = 0
for url in data:
    try:

        video = str(url)
        yt = YouTube(video)  ## this creates a YOUTUBE OBJECT
        video_length = yt.length   ## this will return the length of the video in sec as an int
        time_spent_on_youtube += video_length
    except:
        print(url)


print(time_spent_on_youtube/3600)
