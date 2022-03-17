import pyautogui
import time

from PIL import Image
from pytesseract import pytesseract
import sys
from random import randint
def print_file(path):
    f = open(path, 'r')
    content = f.read()
    return(content)
    f.close()

def write_id(path,x):
    f = open(path, "a")
    f.write(str(x))
    f.close

def qtake_screen():
    im2 = pyautogui.screenshot('rino.png' , region = (215,556,200,100))  # image name will be as per parameter
    for i in range(0,20):
        for j in range(99):
            x = im2.getpixel((i, j))
            pyautogui.press("space")
            #time.sleep(0.1)
            #pyautogui.press("down")
            y = randint(1,100)
            time.sleep(y/100)
            take_screen()   
            if x == (8111113,83,83):
                pyautogui.press("space")
                #time.sleep(0.1)
                #pyautogui.press("down")
                y = randint(1,10)
                time.sleep(y/100)
                take_screen()   
            else:
                print(x)
def get_pos_str(s):
    idx = 0
    for i in range(len(s)):
        if s[i] == "1":
            return (idx)
        idx = idx + 1
    return (0)
#while True:

def main_func():
    print("Start")
    width = 200
    height = 100
    while True:
        take_screen()
        #time.sleep(1)
        im = Image.open('dino.png', 'r')
        width, height = im.size
        pixel_values = list(im.getdata())
        p = pixel_values
        #print(len(p))
        l = []
        s = ""
        for i in range(len(p)):
            if i % width == 0:
                if p[i] == (83,83,83):
                    s = s + "1"
                    l.append(s)
                else:
                    s = s + "0"
                    l.append(s)
                s = ""
            else:
                if p[i] == (83,83,83):
                    s = s + "1"
                else:
                    s = s + "0"
        for i in range(len(l)):
            #print(l[i].count("1"))
            num = l[50].count("1")
            x = get_pos_str(l[50])
            if num > 50 and x < 30:
                if num > 65:
                    time.sleep(1)
                elif num < 35:
                    time.sleep(1)
                else:
                    time.sleep(1)
                pyautogui.press("space")
                time.sleep(0.05)
                pyautogui.press("down")
                print("Taille du bail " + str(num) + " sa pos " + str(x))
                #print("------------")
                #print(l[i])
                #print("------------")
            else:
                print("Taille du bail " + str(num) + " sa pos " + str(x))


def take_screen(idx):
    val = int(idx)
    im2 = pyautogui.screenshot('rino.png' , region = (215 + val,556,225,100))  # image name will be as per parameter
    width = 215 + val
    height = 100
    width, height = im2.size
    pixel_values = list(im2.getdata())
    p = pixel_values
    if (83,83,83) in p:
        pyautogui.press("space")
        #time.sleep(0.05)
        #pyautogui.press("down")
time.sleep(5)
print("Start")
idx = 10
while True:
    idx = idx + 0.25
    take_screen(idx)