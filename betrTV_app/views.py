from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

''' returns a dict of unique video identifiers (last 11 chars)'''

original = ["https://www.youtube.com/embed/jeOWjeY7XOM",
    "https://www.youtube.com/embed/MRuJCLbOAeA",
    "https://www.youtube.com/embed/h-F0uJC10Js",
    "https://www.youtube.com/embed/Lo3769VtgHM",
    "https://www.youtube.com/embed/dIM7E8e9JKY",
    "https://www.youtube.com/embed/crjXflAi8mg",
    "https://www.youtube.com/embed/k7iq2Z2D1Zs",
    "https://www.youtube.com/embed/GXoErccq0vw",
    "https://www.youtube.com/embed/7Jye1ZwgxaM",
    "https://www.youtube.com/embed/1-go0xQZ89w",
    ]

sources = []
# strip out all except the unique source code
for i in range(len(original)):
    source = original[i]
    source = source[30:]
    sources.append(source)

# Checked out... print(sources)

# create day of week to pull video
day = date.today()
num = str(day)[9]

# pull source from list by using 'num' from 'day'
source = sources[int(num)]

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
