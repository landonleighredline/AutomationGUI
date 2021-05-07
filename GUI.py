import tkinter as tk
from tkinter import *
import os
from datetime import date
import sys

#create GUI
gui = Tk()
gui.geometry('300x500')
gui.configure(bg='#292d34')

#Get todays date
today = date.today()
date = today.strftime("%m-%d-%y")

jobInput = ''
assetInput = ''
locationInput = ''
programInput = ''

#Array of options for location dropdown
locationOptions = [
    'ATL',
    'DEN',
    'NAS',
    'CLT'
]

#Array of options for program dropdown
programOptions = [
    'Scene',
    'Pix4D',
    'Both'
]

#Function to add jobs to text file
def addFile():
    jobInput = jobBox.get("1.0",'end-1c')
    locationInput = locationPlaceholder.get()
    assetInput = assetBox.get("1.0",'end-1c')
    programInput = programPlaceholder.get()

    fileInfo = jobInput + ',' + locationInput + ',' + assetInput + ',' + programInput + ' '
    filename = date + '.txt'
    f = open(filename, 'a+')
    f.write(fileInfo)
    f.close()

#Function to start the script
def startScript():
    print('hi')

#Job Number Text Box
jobLabel = Label(gui, text='Job Number')
jobLabel.configure(bg='#302c34', fg='white')
jobBox = Text(gui, bg='white', height=1, width=10, padx=5, pady=5)
jobLabel.pack()
jobLabel.place(y=20, x=115)
jobBox.pack()
jobBox.place(y=40, x=105)

#Job Location Dropdown
locationLabel = Label(gui, text='Job Location')
locationLabel.configure(bg='#302c34', fg='white')
locationPlaceholder = StringVar()
locationPlaceholder.set('ATL')
locationDrop = OptionMenu(gui, locationPlaceholder,  *locationOptions)
locationLabel.pack()
locationLabel.place(y=100, x=112)
locationDrop.pack()
locationDrop.place(y=120, x=115)

#Vehicle Text Box
assetLabel = Label(gui, text='Asset Name')
assetLabel.configure(bg='#302c34', fg='white')
assetBox = Text(gui, bg='white', height=1, width=10, padx=5, pady=5)
assetLabel.pack()
assetLabel.place(y=180, x=115)
assetBox.pack()
assetBox.place(y=200, x=105)

#Program Dropdown
programLabel = Label(gui, text='Program')
programLabel.configure(bg='#302c34', fg='white')
programPlaceholder = StringVar()
programPlaceholder.set('Scene')
programDrop = OptionMenu(gui, programPlaceholder,  *programOptions)
programLabel.pack()
programLabel.place(y=260, x=120)
programDrop.pack()
programDrop.place(y=280, x=110)

#Add to File Button
addFileButton = tk.Button(gui, text='Add Job', padx=10, pady=5, fg='black', bg='#889099', command=addFile)
addFileButton.pack()
addFileButton.place(y=400, x=115)

gui.mainloop()
