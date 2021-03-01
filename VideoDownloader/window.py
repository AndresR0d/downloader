#!/usr/bin/env python
import tkinter
import pytube
#creating window
window = tkinter.Tk()
#making window size
window.geometry("300x200")

#downloading video as mp4
def videoDownload():
    url = textbox.get()
    print("Your url is: " + url)
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download('./Downloads/Videos')
    return True

#downloading video as mp3
def audioDownload():
    url = textbox.get()
    print("Your url is: " + url)
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_audio_only()
    video.download('./Downloads/Music')
    return True

#getting the url of the video
def urlText():
    url = textbox.get()
    print(url)


#creating textbox
textbox=tkinter.Entry(window, width = 30)
#creating label
label = tkinter.Label(window, text="----------PROGRAMA DE DESCARGA DE VIDEO/AUDIO----------")
#creating both buttons for audio and video
button1 = tkinter.Button(window, text="Descargar Video", command=videoDownload)
button2 = tkinter.Button(window, text="Descargar Audio", command=audioDownload)
#Adding the elements to de window
label.pack()
textbox.pack()
button1.pack()
button2.pack()
#running window
window.mainloop()