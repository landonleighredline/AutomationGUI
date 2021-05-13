from Settings import *
from pix_pics import *
import re
import glob
import os
import pyautogui as gui
import time
from time import sleep

screen_center = (gui.size()[0] / 2, (gui.size()[1] / 2) - 50)

def start():
    os.startfile(pix_path)
    time.sleep(2)

def new_project():
    gui.hotkey('ctrl','n')
    #gui.write(job[0] + '_' + job[2])
    gui.write('J8804' + '_' + 'Land Rover')
    gui.press('tab')
    gui.press('enter')

def load_pics():
    check_for_image(pixLoadLogo)
    gui.click()
    check_for_image(pixSelectFolder)
    gui.click()
    time.sleep(1)
    gui.press('tab', presses=6)
    gui.press('enter')
    gui.write(r'C:\Users\LandonLeigh\Desktop\J8804\Drone\Drone\Land Rover')
    gui.press('enter')
    gui.press('tab', presses=7)
    gui.press('enter')

def process_images():
    check_for_image(pixBlueCog)
    gui.click()
    check_for_image(pixCalibrate)
    gui.click()
    check_for_image(pixDensify)
    gui.click()
    check_for_image(pixDSM)
    gui.click()
    check_for_image(pixOrtho)
    gui.click()
    check_for_image(pixQualityReport)
    gui.click()
    check_for_image(pixDensePoint)
    gui.click()
    check_for_image(pixDSMGeo)
    gui.click()
    check_for_image(pixOrthoGeo)
    gui.click()
    check_for_image(pixStartButton)
    gui.click()

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
#new_project()
#load_pics()
#process_images()
close_pix()
