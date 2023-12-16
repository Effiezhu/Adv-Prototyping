# main.py
# main.py
import os, sys, io
import M5
from M5 import *
from bleuart import *
import time
from hardware import *

pwm_peltier = None
peltier_timer = None

ble_client = BLEUARTClient()
ble_client.connect('ble-uart', timeout=2000)

def setup():
  global pwm_peltier
  # initialize M5 board:
  M5.begin()
  
  # initialize PWM on pin 1 with default settings:
  pwm_peltier = PWM(Pin(1))
  pwm_peltier.duty(0)
  
  
def loop():
  global pwm_peltier, peltier_timer
  data = ble_client.read()
  
  if(data != ''):
    print('data =', data)
    peltier_timer = time.ticks_ms()
    print('peltier timer', peltier_timer)
    
    control_peltier(True)  # Turn on the Peltier module
#     print('turn on PWM..')
#     pwm_peltier.duty(100) # When 500, can feel the heat from two layers of fabric
  if peltier_timer and time.ticks_ms() >= peltier_timer + 15000:
    print('turn off time is:', time.ticks_ms())
    control_peltier(False)  # Turn off the Peltier module
    peltier_timer = None  # Reset the timer
    
  time.sleep_ms(100)
    
    
def control_peltier(turn_on):
    global pwm_peltier
    if turn_on:
        print('Turning on Peltier...')
        # Set a duty cycle to start heating
        pwm_peltier.duty(300)  # Adjust the duty cycle as needed
    else:
        print('Turning off Peltier...')
        pwm_peltier.duty(0)  # Set duty cycle to 0 to turn off

        
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
