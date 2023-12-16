# COUPLINK

## Introduction 

Couplink is a pair of smart bracelets designed for couples in long-distance relationships. With simple interactions, such as pressing pressure sensor to send thermal feedback and pressing button to send text message and vibration signal, the bracelets aim to bridge the physical gap by facilitating a more intimate and immediate connection between partners, regardless of the distance. For the final design, I removed the vibration motor because it works similarly as the peltier module and will be redundant if I used both. Aside from that, I also designed a more handcraft style fabric bracelet instead of a traditional smartwatch look, so it feels more intimate and warm.

![IMG_1331](https://github.com/Effiezhu/Adv-Prototyping/assets/123921938/d73d632d-986d-4c10-ad10-7d66e63013ef)

## Implementation   

Explain your process of prototype development including all applicable aspects such as hardware (electronics), firmware (MicroPython code), software (HTML/CSS/JavaScript or other code), integrations (Adafruit IO, IFTTT, etc.), enclosure and mechanical design.  Use a separate subheader for each part:

### Hardware

* 2 of M5Stack ATOMS3 Lite Board
* 2 of M5Stack ATOM TailBat Battery
* 1 pressure sensor
* 1 transistor
* 1 peltier module

  
![Wiring Diagram](https://github.com/Effiezhu/Adv-Prototyping/assets/123921938/b5639cc5-2c88-44e4-a13a-16227d5f9f15)
![IMG_0159](https://github.com/Effiezhu/Adv-Prototyping/assets/123921938/835d2810-65b8-4a67-93dc-7fe93306fa51)
![IMG_0158](https://github.com/Effiezhu/Adv-Prototyping/assets/123921938/bab497bf-ddb5-4a67-b3f3-fbfc069dc28a)

### Firmware   

[Server code](https://github.com/Effiezhu/Adv-Prototyping/blob/main/final/server.py)  
[Client code](https://github.com/Effiezhu/Adv-Prototyping/blob/main/final/client.py)

To make the two individual Atoms3 Lite boards communicate with each other, I used one of them as a server and the other board as a client and connected them with bluetooth. I wrote the code in the main.py, so the server board will constantly broadcasting and send the data to the client board. When the client board is connected to the server board, it will constantly looking for data from the server. 

For the server script, it had two input: one is ADC and one is button. Whenever the pressure sensor value is pressed, the server will write a message to the client.  
``` 
  adc_val = adc.read()
  adc_val_8bit = map_value(adc_val, in_min = 0, in_max = 4095,
                           out_min = 0, out_max = 255)
  print('adc value', adc_val_8bit)
  
  # When pressure sensor is pressed, write a message to client
  if adc_val_8bit < 130:
    print('adc value low')
    ble_server.write('low')
    print('write to bleuart..', message)
    time.sleep_ms(2000)
```

When the client receive the message, it will turns on the peltier module for 15 seconds before turning it off.  
``` 
  if(data != ''):
    print('data =', data)
    peltier_timer = time.ticks_ms()
    print('peltier timer', peltier_timer)
    
    control_peltier(True)  # Turn on the Peltier module
  if peltier_timer and time.ticks_ms() >= peltier_timer + 15000:
    print('turn off time is:', time.ticks_ms())
    control_peltier(False)  # Turn off the Peltier module
    peltier_timer = None  # Reset the timer
    
  time.sleep_ms(100)
```

And when the button was pressed, the board will send the data to Adafruit, and IFTTT will send the message to Telegram through Wifi.  
``` 
if BtnA.wasPressed():
    print('button pressed...')
    mqtt_client.publish('Effieee/feeds/button-feed', 'Love you', qos=0)
```


### Integrations   
[Adafruit](https://io.adafruit.com/Effieee/feeds/button-feed)  
<img width="1117" alt="feed" src="https://github.com/Effiezhu/Adv-Prototyping/assets/123921938/1929cd3f-4f17-4f85-9736-d993131d6849">
[IFTTT Telegram Integration](https://ifttt.com/applets/rrFpRwTj-press-button-to-send-a-message-to-telegram)
<img width="1512" alt="applet" src="https://github.com/Effiezhu/Adv-Prototyping/assets/123921938/de763ebc-5a6b-4d0b-831a-829d366c4c8f">
<img width="911" alt="applet activity" src="https://github.com/Effiezhu/Adv-Prototyping/assets/123921938/d4cab135-11a6-47b1-b088-54dab087b70a">




Include a link to and/or screenshots of other functional components of your project, like Adafruit IO feeds, dashboards, IFTTT applets, etc.  In general, think of your audience as someone new trying to learn how to make your project and make sure to cover anything helpful to explain the functional parts of it.

### Enclosure / Mechanical Design   

Explain how you made the enclosure or any other physical or mechanical aspects of your project with photos, screenshots of relevant files such as laser-cut patterns, 3D models, etc. (it’s great if you’re willing to share the editable source files too!)

## Project outcome  

Summarize the results of your final project implementation and include at least 2 photos of the prototype and a video walkthrough of the functioning demo.

## Conclusion  

As you wrap up the project, reflect on your experience of creating it.  Use this as an opportunity to mention any discoveries or challenges you came across along the way.  If there is anything you would have done differently, or have a chance to continue the project development given more time or resources, it’s a good way to conclude this section.

## Project references  

Please include links to any online resources like videos or tutorials that you may have found helpful in your process of implementing the prototype. If you used any substantial code from an online resource, make sure to credit the author(s) or sources.
