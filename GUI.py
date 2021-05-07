import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()

def createFile():
    f = open("myfile.txt", "x")

#def startScript():


canvas = tk.Canvas(root, height=500, width=700, bg='#465061')
canvas.pack()

createFileButton = tk.Button(root, text="Create File", padx=10, pady=5, fg='white', bg='#465061')
createFileButton.pack()

startScriptButton = tk.Button(root, text="Start Script", padx=10, pady=5, fg='white', bg='#465061')
startScriptButton.pack()

root.mainloop()
