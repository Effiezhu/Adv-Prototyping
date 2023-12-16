# COUPLINK

## Introduction 

Couplink is a pair of smart bracelets designed for couples in long-distance relationships. With simple interactions, such as pressing pressure sensor to send thermal feedback and pressing button to send text message and vibration signal, the bracelets aim to bridge the physical gap by facilitating a more intimate and immediate connection between partners, regardless of the distance. For the final design, I removed the vibration motor because it works similarly as the peltier module and will be redundant if I used both. Aside from that, I also designed a more handcraft style fabric bracelet instead of a traditional smartwatch look, so it feels more intimate and warm.

![IMG_1331](https://github.com/Effiezhu/Adv-Prototyping/assets/123921938/d73d632d-986d-4c10-ad10-7d66e63013ef)


  
### Formatting Tips  
   
To format text into separate lines or paragraphs with [markdown syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), include at least 2 spaces at the end.  The extra spaces act as line breaks.  

Links can be inserted with [link text in square brackets] followed by (link URL in parantheses).  For example, the markdown for [link to this page](../assignment04/) on GitHub Pages is: 
`[link to this page](../assignment04/)`  

Note the use of relative paths in links.  The dot slash `./` in link path means the file is in the current directory, `../` means that it is in parent directory, `../../` is one more directory up and so on.  
  
To insert images, the syntax is almost the same with the addition of exclamation point `!` before [image description in square brackets] followed by (image link in parentheses).  The image below is included with:  
`![led blink circuit](../class02/led_blink_bb.png)` syntax.  

![blink led circuit](../class02/led_blink_bb.png) 

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

Provide a link to your MicroPython code and explain a few important parts that make your prototype work.  Most likely you should explain the inputs/outputs used in your code and how they affect the behavior of the prototype.

To include code snippets, you can use the code block markdown, like this:

``` Python  
if(input_val > 1000):  # sensor value higher than threshold
   led_pin.on()  # turn on LED
```

### Software   

If applicable, explain the important software components of your project with relevant code snippets and links.  

### Integrations   

Include a link to and/or screenshots of other functional components of your project, like Adafruit IO feeds, dashboards, IFTTT applets, etc.  In general, think of your audience as someone new trying to learn how to make your project and make sure to cover anything helpful to explain the functional parts of it.

### Enclosure / Mechanical Design   

Explain how you made the enclosure or any other physical or mechanical aspects of your project with photos, screenshots of relevant files such as laser-cut patterns, 3D models, etc. (it’s great if you’re willing to share the editable source files too!)

## Project outcome  

Summarize the results of your final project implementation and include at least 2 photos of the prototype and a video walkthrough of the functioning demo.

## Conclusion  

As you wrap up the project, reflect on your experience of creating it.  Use this as an opportunity to mention any discoveries or challenges you came across along the way.  If there is anything you would have done differently, or have a chance to continue the project development given more time or resources, it’s a good way to conclude this section.

## Project references  

Please include links to any online resources like videos or tutorials that you may have found helpful in your process of implementing the prototype. If you used any substantial code from an online resource, make sure to credit the author(s) or sources.
