import pyperclip
import pyshorteners
from tkinter import *


root = Tk()
root.geometry('500x500')
root.title("URL Shorteners")
root.configure(bg="#ffffe4")
url = StringVar()
url_address = StringVar()


def urlshorteners():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)


def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


Label(root, text="  My URL Shorteners  ", bg="#7f7fff",
      font="poppins", borderwidth="2", relief="ridge", width="40").pack(pady=10)
text1 = Entry(root, textvariable=url, borderwidth="1",
              relief="solid", width="50").pack(pady=5)
Button(root, text="  Generate Short URL  ", command=urlshorteners,
       borderwidth="4", foreground="white", bg="#000000", relief="raised", width="30").pack(pady=7)
Entry(root, textvariable=url_address,
      borderwidth="1", relief="solid", width="50").pack(pady=5)
Button(root, text="  copy URL  ", command=copyurl,
       borderwidth="4", foreground="white", relief="raised", bg="#000000", width="30").pack(pady=5)

root.mainloop()
