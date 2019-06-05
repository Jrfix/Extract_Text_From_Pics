#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image

from pytesseract import image_to_string

import sys
import os
import time
from time import sleep


print("Example --> /root/Desktop/")

image_path = raw_input("Image path: ")

print("Example --> picture.png")

image_name = raw_input("Image name: ")

os.system("clear")



img = Image.open(image_path+image_name)


try:
	text = image_to_string(img)
	#text = image_to_string(img,lang="eng")
except:
	print("[-]Uncompleted")



for i in range(50):
    sys.stdout.write('\r')
    
    sleep(0.12)


os.system("clear||cls")

print("[+]Completed")

file = open(image_path+image_name + ".txt","w") 
file.write(text) 


file.close()
