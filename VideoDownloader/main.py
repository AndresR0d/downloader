import pytube
print("---------------PROGRAMA DE DESCARGA DE VIDEO/AUDIO-------------")
print("Eligue la opcion acorde a lo que quieres realziar: ")
print("1.- Descargar video 2.- Descargar audio")

x = int(input())


if x == 1:
    print("Dime la URL: ")
    url = input()

    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download('/Downloads')
else:
    print("Dime la URL: ")
    url = input()
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_audio_only()
    video.download('~/Music')
