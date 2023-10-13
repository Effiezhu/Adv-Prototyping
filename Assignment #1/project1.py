"""
Project Overview:

Contains four states: 'START', 'OPEN', 'CLOSED', and 'FINISH'

'START' -- 1 second after the program starts, RGB led strip initial color is green.
'OPEN' -- Input is open, RGB led strip fades in red and fades out.
'CLOSED' -- Input is closed, RGB led strip turns into rainbow color.
'FINISH' -- After 'CLOSED' states continues for 8 seconds, RGB led strip color fades out.
"""


import os, sys, io
import M5
from M5 import *
from hardware import *
import time
from driver.neopixel import NeoPixel

rgb = None
state = 'START'
state_timer = 0
pixel = None

rainbow = [
  (126 , 1 , 0),(114 , 13 , 0),(102 , 25 , 0),(90 , 37 , 0),(78 , 49 , 0),(66 , 61 , 0),(54 , 73 , 0),(42 , 85 , 0),
  (30 , 97 , 0),(18 , 109 , 0),(6 , 121 , 0),(0 , 122 , 5),(0 , 110 , 17),(0 , 98 , 29),(0 , 86 , 41),(0 , 74 , 53),
  (0 , 62 , 65),(0 , 50 , 77),(0 , 38 , 89),(0 , 26 , 101),(0 , 14 , 113),(0 , 2 , 125),(9 , 0 , 118),(21 , 0 , 106),
  (33 , 0 , 94),(45 , 0 , 82),(57 , 0 , 70),(69 , 0 , 58),(81 , 0 , 46),(93 , 0 , 34),(105 , 0 , 22),(117 , 0 , 10)]

def setup():
  global rgb, input_pin
  global pixel
  M5.begin()
  
  # custom RGB setting using pin G35 (M5 AtomS3 built-in LED):
  #rgb = RGB(io=35, n=1, type="SK6812")
  
  # custom RGB setting using pin G2 (M5 AtomS3 bottom connector) and 30 LEDs:
  rgb = RGB(io=2, n=30, type="SK6812")
  
  # initialize pin G41 (M5 AtomS3 built-in button) as input:
  #input_pin = Pin(41)
  
  # initialize pin G39 (M5 PortABC Extension red connector) as input:
  input_pin = Pin(39, mode=Pin.IN, pull=Pin.PULL_UP)
  
  # initialize neopixel strip on pin G2 with 30 pixels:
  pixel = NeoPixel(pin=Pin(2), n=30)
  
  # turn on RGB green and wait 2 seconds:
  if (state == 'START'):
    print('Initial RGB green')
    rgb.fill_color(get_color(0, 255, 0))
    time.sleep(1)  
    check_input()


def loop():
    global state, state_timer
    global pixel, rainbow
    M5.update()
        
    if (state == 'OPEN'):
        print('Fade in red, no input')
        # fade in RGB red:
        for i in range(50):
            rgb.fill_color(get_color(i, 0, 0))
            time.sleep_ms(20)
        # fade out RGB red:
        for i in range(50):
            rgb.fill_color(get_color(50-i, 0, 0))
            time.sleep_ms(20)
        check_input()
        
    elif (state == 'CLOSED'):
        # Check if the input is open during the rainbow cycle
        if input_pin.value() == 1:
            state = 'OPEN'
            state_timer = time.ticks_ms()
            print('change to', state)
            return
        
        # if less than 5 seconds passed since change to 'CLOSED':
        if(time.ticks_ms() < state_timer + 5000):
            # cycle the list of rainbow colors:
            rainbow = rainbow[-1:] + rainbow[:-1]
            for i in range(30):
                # set pixel i to color i of rainbow:
                pixel[i] = rainbow[i]
            # update neopixel strip:
            pixel.write()
            time.sleep_ms(50)
        else:
            state = 'FINISH'
            print('change to', state)
            state_timer = time.ticks_ms()
        
    elif (state == 'FINISH'):
        
        # Blinking 5 times
        for j in range(5):
            for i in range(30):
                pixel[i] = rainbow[i]
                
            pixel.write()
            time.sleep_ms(100)

            pixel.fill((0, 0, 0))
            pixel.write()
            time.sleep_ms(100)
        
        # Fading out the rainbow
        for intensity in range(100, 0, -1):
            pct = intensity / 100.0
            for i in range(30):
                r, g, b = rainbow[i]
                pixel[i] = (int(r * pct), int(g * pct), int(b * pct))
            pixel.write()
            time.sleep_ms(5)
        
        time.sleep(1)
        check_input()


# check input pin and change state to 'OPEN' or 'CLOSED'
def check_input():
    global state, state_timer
    if (input_pin.value() == 0):
        if(state != 'CLOSED'):
            print('change to CLOSED')
        state = 'CLOSED'
        # save current time in milliseconds:
        state_timer = time.ticks_ms()
    else:
        if(state != 'OPEN'):
            print('change to OPEN')
        state = 'OPEN'

    
# convert separate r, g, b values to one rgb_color value:  
def get_color(r, g, b):
  rgb_color = (r << 16) | (g << 8) | b
  return rgb_color

if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")

