import tkinter as tk

from FW import loadImagesFromInput
from instasave import saveImageFromIG

root = tk.Tk()
root.geometry("450x300")

def callSaveImage():
    url = urlEntery.get()
    print(url)
    templateName = templateNameEntery.get()
    saveImageFromIG(url, templateName)

def callInputFolder():
    loadImagesFromInput()

cullInputFolderButton = tk.Button(root, width=10, text="Input", command=callInputFolder).place(x=150, y=10)

urlLabel = tk.Label(root, text="URL").place(x=40, y=60)
urlEntery = tk.Entry(root, width=30)
urlEntery.place(x=110, y=60)

templateNameLabel = tk.Label(root, text="AT / FW").place(x=40, y=100)
templateNameEntery = tk.Entry(root, width=30)
templateNameEntery.place(x=110, y=100)

getUrlButton = tk.Button(root, width=10, text="GO", command=callSaveImage).place(x=150, y=130)

root.mainloop()