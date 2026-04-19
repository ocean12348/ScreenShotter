from pynput.keyboard import Key, Controller
from PIL import ImageGrab
import time

keyboard = Controller()

pages = 1600 # Num of pages.
pps = 3 #Pages per second
t = 1/pps #Seconds per page

time.sleep(2)

for i in range(pages):
    time.sleep(0.3*t)
    print(i)
    img = ImageGrab.grab(bbox=(1148,163,1766,1070)) #HERE GOES THE COORDINATES !!!!!
    img.save(f"{i:05d}.jpg")
    time.sleep(0.2*t)
    keyboard.press(Key.right)
    time.sleep(0.5*t)
    


