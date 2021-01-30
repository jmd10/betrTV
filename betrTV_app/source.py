import random

# This page is to act as a repository for all of the youtube videos to rotate through
    # and to feed the list to views.py for processing

# list of all videos for BetrTV
videos = [
    "https://www.youtube.com/embed/jeOWjeY7XOM",
    "https://www.youtube.com/embed/MRuJCLbOAeA",
    "https://www.youtube.com/embed/h-F0uJC10Js",
    "https://www.youtube.com/embed/Lo3769VtgHM",
    "https://www.youtube.com/embed/dIM7E8e9JKY",
    "https://www.youtube.com/embed/crjXflAi8mg",
    "https://www.youtube.com/embed/k7iq2Z2D1Zs",
    "https://www.youtube.com/embed/GXoErccq0vw",
    "https://www.youtube.com/embed/7Jye1ZwgxaM",
    "https://www.youtube.com/embed/1-go0xQZ89w",
    "https://www.youtube.com/embed/bIacYjZHcs4",
    "https://www.youtube.com/embed/xWMjEBkgAy8",
    "https://www.youtube.com/embed/78I9dTB9vqM",
    ]

# create function to feed a random video ID to the views page
def video_source():
    ''' returns unique video identifier (last 11 chars)'''

    num = random.randint(0, len(videos)-1)
    source = videos[num]
    video_id = source[-11:]

    return video_id
