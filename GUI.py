import tkinter as tk
from tkinter import *
import os

#create GUI
gui = tk.Tk()
gui.geometry('600x300')

#Array of options for location dropdown
locationOptions = [
    'Atlanta',
    'Denver',
    'Nashville',
    'Charlotte'
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

#Function to create text file for jobs
def createFile():
    f = open('myfile.txt', 'w')

#Function to add jobs to existing file
def addFile():
    f = open('myfile.txt', 'a')
    f.write()
    f.close()

#Function to start the script
def startScript():
    print('hi')

#Job Number Text Box
jobLabel = Label(gui, text='Job Number')
jobLabel = Label(gui, text='Job Number')
jobBox = Text(gui, bg='white', height=1, width=10, padx=5, pady=5)
jobBox = Text(gui, bg='white', height=1, width=10, padx=5, pady=5)
jobLabel.pack()
jobBox.pack()

#Job Location Dropdown
locationLabel = Label(gui, text='Job Location')
locationLabel = Label(gui, text='Job Location')
locationPlaceholder = StringVar()
locationPlaceholder.set('Atlanta')
locaionDrop = OptionMenu(gui, locationPlaceholder,  *locationOptions)
locaionDrop = OptionMenu(gui, locationPlaceholder,  *locationOptions)
locationLabel.pack()
locaionDrop.pack()

#Vehicle Text Box
assetLabel = Label(gui, text='Asset Name')
assetLabel = Label(gui, text='Asset Name')
assetBox = Text(gui, bg='white', height=1, width=10, padx=5, pady=5)
assetBox = Text(gui, bg='white', height=1, width=10, padx=5, pady=5)
assetLabel.pack()
assetBox.pack()

#Program Dropdown
programLabel = Label(gui, text='Program Used')
programPlaceholder = StringVar()
programPlaceholder.set('Scene')
programDrop = OptionMenu(gui, programPlaceholder,  *programOptions)
programLabel.pack()
programDrop.pack()

#Create File Button
createFileButton = tk.Button(gui, text='Create File', padx=10, pady=5, fg='white', bg='#465061', command=createFile)
createFileButton.pack()

#Add to File Button
addFileButton = tk.Button(gui, text='Add to File', padx=10, pady=5, fg='white', bg='#465061', command=addFile)
addFileButton.pack()

#Start Script Button
startScriptButton = tk.Button(gui, text='Start Script', padx=10, pady=5, fg='white', bg='#465061', command=startScript)
startScriptButton.pack()

gui.mainloop()
