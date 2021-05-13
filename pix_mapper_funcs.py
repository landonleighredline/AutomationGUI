from Settings import *
from pix_mapper_pics import *
import re
import glob
import os
import pyautogui as gui
import time
from time import sleep

screen_center = (gui.size()[0] / 2, (gui.size()[1] / 2) - 50)

job = ['J8804', 'CLT', 'land rover', 'Pix4D']

def start():
    os.startfile(pix_mapper_path)
    time.sleep(15)

def new_project(job):
    gui.hotkey('ctrl','n')
    gui.write(job[0] + '_' + job[2])
    gui.press('tab', presses=3)
    gui.press('enter')
    time.sleep(1)
    gui.press('tab')
    gui.press('enter')
    gui.press('tab', presses=5)
    gui.press('enter')

def load_pics(job):
    gui.write(r'C:\Users\LandonLeigh\Desktop\J8804\Drone\Drone\Land Rover')
    gui.press('enter')
    time.sleep(1)
    gui.press('tab')
    time.sleep(1)
    gui.press('tab')
    time.sleep(1)
    gui.press('tab')
    time.sleep(1)
    gui.press('tab')
    gui.hotkey('ctrl','a')
    gui.press('enter')
    time.sleep(1)
    gui.press('enter')
    time.sleep(5)
    gui.press('tab',presses=5)
    time.sleep(5)
    #gui.press('enter',presses=2)
    #time.sleep(3)
    gui.press('enter')
    time.sleep(1)
    gui.press('enter')
    time.sleep(7)
    if job[2] == 'site':
        pass
    else:
        gui.press('down')
    #gui.press('enter')


def process_images():
    pass


def close_pix():
    gui.hotkey('alt','f4')

def check_for_image(image):
    checking = True
    while checking:
        image_location = gui.locateCenterOnScreen(image)
        gui.moveTo(image_location)
        if gui.position() == image_location:
            checking = False

start()
new_project(job)
load_pics(job)
#process_images()
#close_pix()
