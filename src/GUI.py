from downloader import *
from tkinter import *

class GUI(Tk):
    def __init__(self):
        super(GUI, self).__init__()
        self.title("Downloader")
        self.minsize(100, 100)
        self.line = Label(self ,text="URL:")
        self.line.grid(row=0, column=0)
        self.url = Entry(self ,width=50)
        self.url.grid(row=1, column=0)
        self.button = Button(self, text="Run", command=self.run_command)
        self.button.grid(row=2, column=0)
        self.line2 = Label(self, text="")
        self.line2.grid(row=3, column=0)

    def run_command(self):
        self.line2["text"] = ""
        url = self.url.get()
        format = 'bestaudio/best'
        result = download(url, format)
        self.line2["text"] = result

