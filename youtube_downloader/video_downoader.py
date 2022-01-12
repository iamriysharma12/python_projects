from tkinter import *
import os
from pytube import YouTube
from tkinter.ttk import *
from tkinter.messagebox import *

root = Tk()
root.geometry("600x700")
newpath = r"C:\Users\advoc\OneDrive\Desktop\youtube_download"
if not os.path.exists(newpath):
    od.makedirs(newpath)

def download():
    yt = YouTube(el.get())
    ytl = yt.streams.get_by_resolution(cl.get())
    showinfo("Notification" , "Downloading   the video")
    ytl.download(newapth)
    showinfo("Notification" , "Downloaded video in youtube_download")

root.title("yotube video bownloader")

l1 = Label(root, text = "enter Link")
l1.grid(row= 0, column = 0)
l2 = Label(root, text = "Resolution ")
l2.grid(row = 1 , column = 0)
el = Entry(root , width=35)
el.grid(row = 0 , column = 1)
cl = Combobox(root , values = ['360p','480p' , '720p'])
cl.grid(row = 1, column = 1)
b1 = Button(root , text = "Download Video" , command = download)
b1.grid(row=1 , column = 1)

root.mainloop( )
