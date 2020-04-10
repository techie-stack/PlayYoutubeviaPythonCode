#Playing YouTube videos in Python#
"""
Pafy is a Python library that can play content from YouTube in your chosen media player.
To play that URL with the Python 3 VLC library...
"""

import pafy
import vlc
#Run the code and it will ask for the YouTube URL,
url= input("Please input your URL::>>>")
#Lets tell pafy about the URL.
video= pafy.new(url)
#to find out the best URL that we can use to stream with VLC
best = video.getbest()
media=vlc.MediaPlayer(best.url)
#Play url
media.Play()
#if you want to stop video
media.stop
