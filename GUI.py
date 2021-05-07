import tkinter as tk
from tkinter import *
import os
from datetime import date

#create GUI
gui = tk.Tk()
gui.geometry('600x300')
gui.configure(bg='#292d34')

#Get todays date
today = date.today()
date = today.strftime("%m-%d-%y")

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

#Function to get job number from text box
def retrieveJobInput():
    jobInput = self.jobBox.get("1.0",END)

#Function to get vehicle name from text box
def retrieveVehicleInput():
    vehicleInput = self.vehicleBox.get("1.0",END)


#Function to add jobs to text file
def addFile():
    filename = date + '.txt'
    #f = open(filename, 'w')
    #f.close()
    f = open(filename, 'a+')
    f.write('info')
    f.close()

#Function to start the script
def startScript():
    print('hi')

#Job Number Text Box
jobLabel = Label(gui, text='Job Number')
jobLabel.configure(bg='#302c34', fg='white')
jobBox = Text(gui, bg='white', height=1, width=10, padx=5, pady=5)
jobLabel.pack()
jobBox.pack()

#Job Location Dropdown
locationLabel = Label(gui, text='Job Location')
locationLabel.configure(bg='#302c34', fg='white')
locationPlaceholder = StringVar()
locationPlaceholder.set('ATL')
locationDrop = OptionMenu(gui, locationPlaceholder,  *locationOptions)
locationDrop.configure(bg='#889099')
locationLabel.pack()
locationDrop.pack()

#Vehicle Text Box
assetLabel = Label(gui, text='Asset Name')
assetLabel.configure(bg='#302c34', fg='white')
assetBox = Text(gui, bg='white', height=1, width=10, padx=5, pady=5)
assetLabel.pack()
assetBox.pack()

#Program Dropdown
programLabel = Label(gui, text='Program Used')
programLabel.configure(bg='#302c34', fg='white')
programPlaceholder = StringVar()
programPlaceholder.set('Scene')
programDrop = OptionMenu(gui, programPlaceholder,  *programOptions)
programDrop.configure(bg='#889099')
programLabel.pack()
programDrop.pack()

#Add to File Button
addFileButton = tk.Button(gui, text='Add Job', padx=10, pady=5, fg='black', bg='#889099', command=addFile)
addFileButton.pack()

#Start Script Button
startScriptButton = tk.Button(gui, text='Start Script', padx=10, pady=5, fg='black', bg='#889099', command=startScript)
startScriptButton.pack()

gui.mainloop()
