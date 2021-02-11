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

    analytics = "<!-- Global site tag (gtag.js) - Google Analytics --> \
        <script async src='https://www.googletagmanager.com/gtag/js?id=G-5S9053QREN'></script> \
        <script>window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);} gtag('js', new Date());gtag('config', 'G-5S9053QREN');</script>"
    meta = "<meta name='description' content='The aim of betr.tv is to take videos on the web (youtube, vimeo, et... ) and collect them in one place.\
        These videos are videos such as Impact Theory, Mindvalley, Jay Shetty, Tim Ferris, etc... videos that empower \
        and inform. It is intended to be stripped of all of the banal shit that is out there. All of the popular \
        platforms are dragged to the lowest common denominator. This is intended to be a place people can go to not\
        have to endure the barrage of shit they get eslewhere. Instead they will be exposed to empowering content./>'\
        <meta name='robots' content='index, follow' />"

    html = '<html><head><title>Empowerment on Demand</title>%s%s<head/><body><link href="https://fonts.googleapis.com/css?family=Gugi"\
        + rel="stylesheet"><h1 style="color: grey; font-family: Gugi; font-size: \
        + 20px;">BetrTV... Empowerment on Demand</h1>\
        <iframe %s></iframe></body></html>' %(analytics, meta, video)

    return HttpResponse(html)
