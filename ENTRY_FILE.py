from Settings import *
from deltav_functions import *

scene_list = []
pix4d_list = []
job_list = []


def automate(job_list):
    ############ COPY FILES FROM SERVER ############
    create_local_files(job_list)

    ################# RUN JOBS #####################
    for job in job_list:
        if job[3] == 'Scene':
            run_scene(job)
        elif job[3] == 'Pix4D':
            pass
        else:
            run_scene(job)
