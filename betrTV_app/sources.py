
def video():
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

    return sources

video()
