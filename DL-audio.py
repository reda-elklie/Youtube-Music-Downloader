from pafy import new
url = input("Enter Youre Link Here : ")
video = new(url)
audio =video.audiostreams
audio[0].download()