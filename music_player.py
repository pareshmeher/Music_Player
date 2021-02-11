import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry('450x350')

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font ="Helvetica 12 bold", bg="#F5B301",selectmode= tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos+1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(playlist.get( tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def ExitMusicPlayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

Button1 = tkr.Button(musicplayer, width=3, height=1, font="helvetica   12  bold", text= "Play" ,command =play, bg="#3B3F46", fg ="white" )
Button2 = tkr.Button(musicplayer, width=3, height=1, font="helvetica   12  bold", text= "Stop" ,command =ExitMusicPlayer, bg="#3B3F46", fg ="white" )
Button3 = tkr.Button(musicplayer, width=3, height=1, font="helvetica   12  bold", text= "Pause" ,command =pause, bg="#3B3F46", fg ="white" )
Button4 = tkr.Button(musicplayer, width=3, height=1, font="helvetica   12  bold", text= "Unpause" ,command =unpause, bg="#3B3F46", fg ="white" )

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="helvetica   12  bold", textvariable = var)

songtitle.pack()
Button1.pack(fill= "x")
Button2.pack(fill= "x")
Button3.pack(fill= "x")
Button4.pack(fill= "x")
playlist.pack(fill = "both", expand = "yes")

musicplayer.mainloop()