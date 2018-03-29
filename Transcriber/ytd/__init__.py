import pafy

def start():
    url = input("ENTER VIDEO URL\n")
    video = pafy.new(url)
    streams = video.streams
    for i in streams:
        print(i)
    best = video.getbest()
    return best

def save(best):
    print("SAVING VIDEO AS ", best.title, "PLEASE WAIT")
    print("VIDEO RESOLUTION = ", best.resolution, "VIDEO FORMAT = ", best.extension)
    best.download()


