import tkinter as tk
from tkinter import *
from datetime import date
import ctypes, threading, sys, re, os
from ENTRY_FILE import *
from Settings import *
from PIL import Image, ImageTk



class ScrollableFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(side='right', fill="y",  expand="false")
        self.canvas = tk.Canvas(self,bg='#444444', bd=0, height=350, highlightthickness=0, yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side="left", fill="both", expand="true")
        self.vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = tk.Frame(self.canvas, **kwargs)
        self.canvas.create_window(0, 0, window=self.interior, anchor="nw")

        self.bind('<Configure>', self.set_scrollregion)


    def set_scrollregion(self, event=None):
        """ Set the scroll region on the canvas"""
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


if __name__ == '__main__':
    root = tk.Tk()
    checkbox_pane = ScrollableFrame(root, bg='#444444')
    checkbox_pane.pack(expand="true", fill="both")

    job_list, scene_list, pix4d_list = find_jobs()
    check = []
    var = []
    jobs = []
    i = 0
    z = 50

    for job in job_list:
        jobs.append(job)
        var.append(str(i))
        var[i] = tk.IntVar()
        box = tk.Checkbutton(checkbox_pane.interior, text=job[0] + ' ' + job[2] + ' ' + job[3], variable=var[i], onvalue=1, offvalue=0)
        box.configure(bg='#292d34', fg='#fafafa', font=('Aerial', 12, 'bold'), selectcolor='black')
        #check.append(box)
        box.pack()
        #check[i].pack()
        #check[i].place(y=170+z*i, x=300)
        #for item in check:
            #checkbox_pane.insert(END, job)
        i+=1

    root.mainloop()
