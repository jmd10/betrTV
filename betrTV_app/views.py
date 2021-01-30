from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from . source import video_source

# The intention here is to have the list of videos in "sources.py", and to have that list
    # processed such that id is provided here by calling the function. That will minimize
    # the burden of pulling the whole list here for processing. It should be done within the function



# pull random video from video_source function in 'source.py'. Just need the last 11 digits...
source = video_source()

def index(request):
    ''' The home page for betrTV_app '''

    video = 'class="video-frame" width="1200" height="600"\
        + src="https://www.youtube.com/embed/%s"\
        + frameborder="0" allow="accelerometer; autoplay; encrypted-media; \
        + gyroscope; picture-in-picture" allowfullscreen' %source


    html = '<html><body><link href="https://fonts.googleapis.com/css?family=Gugi"\
        + rel="stylesheet"><h1 style="color: grey; font-family: Gugi; font-size: \
        + 20px;">BetrTV... Empowerment on Demand</h1>\
        <iframe %s></iframe></body></html>' %video

    return HttpResponse(html)
