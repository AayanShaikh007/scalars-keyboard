---
title: "keyboard"
author: "@Scalar on slack"
description: "A TKL Keyboard made fully in house"
created_at: "2025-06-09"
---
✅ : implemented already
# June 9th, 12:06 PM - First Update Since Project Start
I have been thinking of this project for a while but was delayed due to some setbacks with my hackpad, which means I will need to accelerate work on this project. I began by doing some research of various aspects/qualities of keyboards, and decided which ones I wanted to implement in my final design. 

In my final design, I really want ...
- Hotswappable keys. This will be achieved by using Kalih Hot-swappable sockets, which are fortunately compatible with all MX style switches.
- ✅ OLED Display for mode display (probably SSD1306)
- ❎ ~~Customizable RGB screen/display, for showing custom animations (SSD1331 perhaps).~~ After further research, this has proven too difficult to implement in in a keyboard, and I will implement this in my other custom project. 

Some more standard features ...
- ✅ RGB lighting. Ideally, I want to have a led strip on the rim of the keyboard with a plastic covering so that they are not within line of sight, and provide a cool backlight. I could also just place a singular strip on the backside of the keyboard.
- ✅ Mode setting keys.
- Macros powered by a custom software where display settings, etc can be controlled.
- Either a built in kickstand or some attachment/feature to increase the angle of the keyboard.
- A foam/soft touch wristpad. 

# June 9th, 11:59 AM - Finalizing Project Goals

Before starting work on the schematic, I performed further research on some other aspects of the keyboard I wanted in my final design. I was thinking of using the Sparkfun Pro Micro rp2040 chip as my microcontroller, but I decided against it and will be using a Pico (v1) instead. The only con i can think of with regards to this is that I wont have USB-C connectivity, but that can be fixed by replacing the microcontroller with a clone from alibaba after highway is complete (I only want parts that can be shipped + recieved within 7 days). 
- ✅ The microcontroller will be a Raspberry Pi Pico
- ✅ I will be using MX Brown switches (ideally)

# June 10th ~1:00 AM
Continued working on the schematic. I have finished the key matrix and will be using the Adafruit MCP23017 to increase pinouts. 
https://www.digikey.ca/en/products/detail/adafruit-industries-llc/5346/15913270
I will also be adding a rotary encoder, it should be helpful for volume/mode settings.
https://www.sparkfun.com/rotary-encoder.html

# June 10th 5:33 AM 
Completed Schematic. It was somewhat tedious and took longer than expected but everything looks good at the end at least. Will begin work on PCB now.
Low Res Preview of Schematic: 

![image](https://github.com/user-attachments/assets/adca0cd6-aaca-46dd-8a35-3622b7d13c3c)

# June 10th ~5:30 PM
- Completed PCB. My experience with hackpad helped in this quite a bit. For some reason the keys didnt line up properly but I think I got everything in the right place (measured to confirm).

Preview of PCB.
