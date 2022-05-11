import numpy as np
from skimage import io
from scipy.ndimage import gaussian_filter
from tifffile import imsave
import os
import time


def wait_until1(timeout, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout
    while time.time() < mustend:
        if len(os.listdir(os.getcwd() + '\\Image to Process'))  > 0: return True
        time.sleep(period)
    return print('Please add an image and relaunch the program.')

def wait_until2(timeout, period=0.25, *args, **kwargs):
    mustend = time.time() + timeout
    while time.time() < mustend:
        if len(os.listdir(os.getcwd() + '\\Image to Process'))  == 1: return True
        time.sleep(period)
    return print("Please remove all but 1 image from the 'Image to Process' folder and relaunch the program.")

def gaussian_filterer (image, sigma):
    filtered_image = gaussian_filter(stack_image, sigma = sigma)
    return filtered_image



#Make the directories that you want to see in the world...
os.makedirs(os.getcwd() + '\\Image to Process',exist_ok=True)
os.makedirs(os.getcwd() + '\\Filtered Images', exist_ok=True)


#Check to make sure that we only have 1 image in the image folder so that we can tell the user
if len(os.listdir(os.getcwd() + '\\Image to Process')) == 0:
    print("Please add an image to the 'Image to Process' folder to continue!")
    wait_until1(30)
elif len(os.listdir(os.getcwd() + '\\Image to Process')) > 1:
    print("Please remove all but 1 image from the 'Image to Process' folder.")
    wait_until2(30)

    
#Create the image to process directory and the stack tiff array
image_to_process = os.listdir(os.getcwd()+'\\Image to Process\\')[0]
stack_image = io.imread(os.getcwd() + '\\Image to Process\\' + image_to_process)


#Gather the necessary information from the user about how to filter
result = 'bad'
while result == 'bad':
    try:
        user_input = float(input('Please enter the value you want to use as your Sigma value (typically, use 0.25-2): '))
        result = 'good'
    except ValueError:
        pass

#Save filtered image off in the directory that we made from the get go
imsave(os.getcwd() + f'\\Filtered Images\\ Filtered {image_to_process}.tif', gaussian_filterer(stack_image, user_input))

print("Check the 'Filtered Images' folder to see your newly filtered tif image stack! How neat!")