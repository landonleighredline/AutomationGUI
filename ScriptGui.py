import tkinter as tk
from tkinter import *
from datetime import date
import ctypes, threading, sys, re, os
from ENTRY_FILE import *
from Settings import *
from PIL import Image, ImageTk

#Get list of jobs from text file
def find_jobs():
    today = date.today()
    tdate = today.strftime("%m-%d-%y")
    text_file = open(text_path + tdate + '.txt', 'r')
    list = text_file.read().split()

    list_o_jobs = []
    scene_jobs = []
    pix4d_jobs = []

    for job in list:
        job2 = job.split(',')
        list_o_jobs.append(job2)

    for job in list_o_jobs:
        job[0] = job[0].upper()
    for job in list_o_jobs:
        if job[1] == 'CLT':
            job[1] = CLT
        elif job[1] == 'DEN':
            job[1] = DEN
        elif job[1] == 'ATL':
            job[1] = ATL
        elif job[1] == 'NAS':
            job[1] = NAS
    for job in list_o_jobs:
        job[2] = job[2].lower()
    for job in list_o_jobs:
        if job[3] == 'Scene':
            scene_jobs.append(job)
        if job[3] == 'Pix4D':
            pix4d_jobs.append(job)
        if job[3] == 'Both':
            scene_jobs.append(job)
            pix4d_jobs.append(job)

    return list_o_jobs, scene_jobs, pix4d_jobs

#Passes list of jobs that are checked by user
def confirmList():
    fullRunList = []
    for n in range(len(check)):
        if (var[n].get() == 1):
            fullRunList.append(jobs[n])
    automate(fullRunList)

#Various declarations
job_list, scene_list, pix4d_list = find_jobs()
check = []
var = []
jobs = []
i = 0
z = 50

#create GUI
gui = Tk()
gui.title('Automation Script')
#gui.geometry('355x160')
gui.geometry('803x800')
gui.configure(bg='#292d34')
windowWidth = gui.winfo_reqwidth()
windowHeight = gui.winfo_reqheight()
positionRight = int(gui.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(gui.winfo_screenheight()/3 - windowHeight/2)
gui.geometry("+{}+{}".format(positionRight, positionDown))
gui.resizable(False, False)

#Logo Image
logo_img = PhotoImage(file=r'C:\Users\LandonLeigh\Documents\GitHub\AutomationGUI\pics\DeltaV_logo.png')
img = ImageTk.PhotoImage(Image.open(r'C:\Users\LandonLeigh\Documents\GitHub\AutomationGUI\pics\DeltaV_logo.png'))
panel = tk.Label(gui, image = img)
panel.pack(side = "top")

#Title for program
programLabel = Label(gui, text='Automation Script')
programLabel.configure(bg='#302c34', fg='#fafafa', font=('Aerial', 20, 'bold'))
programLabel.pack()
programLabel.place(y=240, x=275)

#Start Script Button
addFileButton = tk.Button(gui, text='Start', padx=10, pady=5, fg='black', bg='#889099', command=confirmList, font=('Aerial', 14, 'bold'))
addFileButton.pack()
addFileButton.place(y=300, x=355)

#Create check boxes
for job in job_list:
    jobs.append(job)
    var.append(str(i))
    var[i] = tk.IntVar()
    box = tk.Checkbutton(gui, text=job[0] + ' ' + job[2] + ' ' + job[3], variable=var[i], onvalue=1, offvalue=0)
    box.configure(bg='#292d34', fg='#fafafa', font=('Aerial', 12, 'bold'), selectcolor='black')
    check.append(box)
    check[i].pack()
    check[i].place(y=370+z*i, x=300)
    i+=1

gui.mainloop()
