from tkinter import *
from tkinter import filedialog
import pygame
import os

window = Tk()
window.title('Music App')
window.geometry("800x500")

pygame.mixer.init()

menubar = Menu(window)
window.config(menu=menubar)

songs = []
curr = ""
pause = False

def loadmusic():
    global curr
    window.directory = filedialog.askdirectory()

    songs.clear()
    list.delete(0, END)

    for song in os.listdir(window.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        list.insert("end", song)

    list.selection_set(0)
    curr = songs[list.curselection()[0]]

def play():
    global curr, pause
    if not pause:
        pygame.mixer.music.load(os.path.join(window.directory, curr))
        pygame.mixer.music.play()  
    else:
        pygame.mixer.music.unpause()
        pause = False

def paused():
    global pause
    pygame.mixer.music.pause() 
    pause = True

def forw():
    global curr, pause
    try:
        list.select_clear(0, END)
        next_index = songs.index(curr) + 1
        if next_index < len(songs):
            list.selection_set(next_index)
            curr = songs[list.curselection()[0]]
            play()
    except IndexError:
        pass

def back():
    global curr, pause
    try:
        list.select_clear(0, END)
        prev_index = songs.index(curr) - 1
        if prev_index >= 0:
            list.selection_set(prev_index)
            curr = songs[list.curselection()[0]]
            play()
    except IndexError:
        pass

organise = Menu(menubar, tearoff=False)
organise.add_command(label='Select Folder', command=loadmusic)
menubar.add_cascade(label='Organise', menu=organise)

list = Listbox(window, bg="white", fg="black", width=800, height=25)
list.pack()

backbutton = PhotoImage(file='C:/Users/Hp/.vscode/python/CodexCueintern/backward button.png').subsample(3, 3)
playbutton = PhotoImage(file='C:/Users/Hp/.vscode/python/CodexCueintern/play button.png').subsample(8, 8)
pausebutton = PhotoImage(file='C:/Users/Hp/.vscode/python/CodexCueintern/pause button.png').subsample(8, 8)
forbutton = PhotoImage(file='C:/Users/Hp/.vscode/python/CodexCueintern/next.png').subsample(3, 3)

frame = Frame(window)
frame.pack()

backbun = Button(frame, image=backbutton, borderwidth=0, command=back)
playbun = Button(frame, image=playbutton, borderwidth=0, command=play)
pausebun = Button(frame, image=pausebutton, borderwidth=0, command=paused)
forbun = Button(frame, image=forbutton, borderwidth=0, command=forw)

backbun.grid(row=0, column=0, padx=5, pady=5)
playbun.grid(row=0, column=1, padx=5, pady=5)
pausebun.grid(row=0, column=2, padx=5, pady=5)
forbun.grid(row=0, column=3, padx=5, pady=5)

window.mainloop()
