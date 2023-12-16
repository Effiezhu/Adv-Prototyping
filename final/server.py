import os, sys, io
import M5
from M5 import *
from bleuart import *
from umqtt import *
from hardware import *
import time

ble_server = BLEUARTServer(name='ble-uart')
adc = None
adc_val = None
mqtt_client = None

def setup():
  global mqtt_client
  global adc, adc_val
  # initialize M5 board:
  M5.begin()
  
  adc = ADC(Pin(1), atten=ADC.ATTN_11DB)

  mqtt_client = MQTTClient(
      'testclient',
      'io.adafruit.com',
      port=1883,
      user='Effieee',
      password='aio_ndal57GtWeLTl5ENLNCTdpGo54rj',
      keepalive=0
  )
  mqtt_client.connect(clean_session=True)

def loop():
  global mqtt_client
  global adc, adc_val
  
  message = 'Turn on peltier'

  # update M5 board:
  M5.update()
  # read 12-bit analog value (0 - 4095 range):
  adc_val = adc.read()
  adc_val_8bit = map_value(adc_val, in_min = 0, in_max = 4095,
                           out_min = 0, out_max = 255)
  print('adc value', adc_val_8bit)
  
  if adc_val_8bit < 130:
    print('adc value low')
    ble_server.write('low')
    print('write to bleuart..', message)
    time.sleep_ms(2000)
    
  
  if BtnA.wasPressed():
    print('button pressed...')
    mqtt_client.publish('Effieee/feeds/button-feed', 'Love you', qos=0)
  
  time.sleep_ms(500)
    

def map_value(in_val, in_min, in_max, out_min, out_max):
  v = out_min + (in_val - in_min) * (out_max - out_min) / (in_max - in_min)
  if (v < out_min): 
    v = out_min 
  elif (v > out_max): 
    v = out_max
  return int(v)

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


