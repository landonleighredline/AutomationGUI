import os
import shutil
import glob

####### PATHS TO FILES #######
new_job_template = r'C:\Users\LandonLeigh\Desktop\TestTemplate'
new_job_folder = r'C:\Users\LandonLeigh\Desktop'

##########APP PATHS###############
scene_path = 'C:\Program Files\FARO\SCENE2\SCENE.exe'
pix_path = 'C:\Program Files\Pix4Dmatic\Pix4Dmatic.exe'
pix_mapper_path = 'C:\Program Files\Pix4Dmapper\pix4dmapper.exe'

#######SERVER PATHS#############
CLT = r'C:\Users\LandonLeigh\Desktop\Fake_Server\CLT'
ATL = r'C:\Users\LandonLeigh\Desktop\Fake_Server\ATL'
DEN = r'C:\Users\LandonLeigh\Desktop\Fake_Server\DEN'
NAS = r'C:\Users\LandonLeigh\Desktop\Fake_Server\NAS'

######## FOLDERS TO FETCH ################
drone_folder = r'\Drone'
scan_folder = r'\Scans'
processed_folder = r'\Processed'
scene_folder = r'\Scene'
pix4d_folder = r'\Pix4D'

#############Text File Path#####################
text_path = r'C:\Users\LandonLeigh\Desktop\Fake_Server\CLT\\'
