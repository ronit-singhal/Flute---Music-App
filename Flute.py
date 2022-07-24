from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os

flute = Tk()
flute.title("Flute")
flute.geometry("920x670+290+85")
flute.configure(bg = "#0f1a2b")
flute.resizable(False, False)

mixer.init()

music_frame = Frame(flute, bd = 2, relief=RIDGE)
music_frame.place(x = 300, y = 350, width = 560, height = 250)

scroll = Scrollbar(music_frame)

playlist = Listbox(music_frame,
                   width=100,
                   font=("arial", 10),
                   bg="#333333",
                   fg="gray",
                   selectbackground="lightblue",
                   cursor="hand2",
                   bd=0,
                   yscrollcommand=scroll.set)

def open_folder():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                playlist.insert(END, song)


def play_song():
    music_name = playlist.get(ACTIVE)
    mixer.music.load(playlist.get(ACTIVE))
    mixer.music.play()
    music.config(text = music_name[0:-4])

image_icon = PhotoImage(file = "C:/Users/ASUS/Downloads/Flute/logo.png")
flute.iconphoto(False, image_icon)

Top = PhotoImage(file = "C:/Users/ASUS/Downloads/Flute/top.png")
Label(flute, image = Top, bg = "#0f1a2b").pack()

Logo = PhotoImage(file = "C:/Users/ASUS/Downloads/Flute/logo.png")
Label(flute, image = Logo, bg = "#0f1a2b").place(x = 65, y = 115)

play_button = PhotoImage(file = "C:/Users/ASUS/Downloads/Flute/play.png")
Button(flute, image = play_button, bg = "#0f1a2b", bd = 0, command=play_song).place(x = 100, y = 400)

stop_button = PhotoImage(file = "C:/Users/ASUS/Downloads/Flute/stop.png")
Button(flute, image = stop_button, bg = "#0f1a2b", bd = 0, command=mixer.music.stop).place(x = 30, y = 500)

resume_button = PhotoImage(file = "C:/Users/ASUS/Downloads/Flute/resume.png")
Button(flute, image = resume_button, bg = "#0f1a2b", bd = 0, command=mixer.music.unpause).place(x = 115, y = 500)

pause_button = PhotoImage(file = "C:/Users/ASUS/Downloads/Flute/pause.png")
Button(flute, image = pause_button, bg = "#0f1a2b", bd = 0, command=mixer.music.pause).place(x = 200, y = 500)

music = Label(flute,
              text = "",
              font=("arial", 15),
              fg="white",
              bg="#0f1a2b")
music.place(x=150, y=340, anchor="center")

Button(flute,
       text = "Open Folder",
       width=15,
       height=2,
       font=("arial", 10),
       fg="white",
       bg="#21b3de",
       command=open_folder).place(x=330,
                                  y=300)
                                  
scroll.config(command=playlist.yview)
scroll.pack(side=RIGHT, fill=Y)
playlist.pack(side=LEFT, fill=BOTH)

flute.mainloop()