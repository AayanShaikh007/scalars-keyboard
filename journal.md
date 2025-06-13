---
title: "keyboard"
author: "@Scalar on slack"
description: "A TKL Keyboard made fully in house"
created_at: "2025-06-09"
---
Estimated Total Time: 27 hours

✅ : implemented already

# June 9th, 12:06 PM - First Update Since Project Start - 3h
I have been thinking of this project for a while but was delayed due to some setbacks with my hackpad, which means I will need to accelerate work on this project. I began by doing some research of various aspects/qualities of keyboards, and decided which ones I wanted to implement in my final design. 

In my final design, I really want ...
- Hotswappable keys. This will be achieved by using Kalih Hot-swappable sockets, which are fortunately compatible with all MX style switches.
- ✅ OLED Display for mode display (probably SSD1306)
- ❎ ~~Customizable RGB screen/display, for showing custom animations (SSD1331 perhaps).~~ After further research, this has proven too difficult to implement in in a keyboard, and I will implement this in my other custom project. 

Some more standard features ...
- ✅ RGB lighting. Ideally, I want to have a led strip on the rim of the keyboard with a plastic covering so that they are not within line of sight, and provide a cool backlight. I could also just place a singular strip on the backside of the keyboard.
- ✅ Mode setting keys.
- ✅ Macros powered by a custom software where display settings, etc can be controlled.
- ✅ Either a built in kickstand or some attachment/feature to increase the angle of the keyboard (3d printable after assembly).
- ✅ A foam/soft touch wristpad. (will order from amazon after project completion)

# June 9th, 11:59 AM - Finalizing Project Goals - 1h

Before starting work on the schematic, I performed further research on some other aspects of the keyboard I wanted in my final design. I was thinking of using the Sparkfun Pro Micro rp2040 chip as my microcontroller, but I decided against it and will be using a Pico (v1) instead. The only con i can think of with regards to this is that I wont have USB-C connectivity, but that can be fixed by replacing the microcontroller with a clone from alibaba after highway is complete (I only want parts that can be shipped + recieved within 7 days). 
- ✅ The microcontroller will be a Raspberry Pi Pico
- ✅ I will be using MX Brown switches (ideally)

# June 10th ~1:00 AM - 3h
- Continued working on the schematic. ~~I have finished the key matrix and will be using the Adafruit MCP23017 to increase pinouts.~~ Decided to remove this
- https://www.digikey.ca/en/products/detail/adafruit-industries-llc/5346/15913270
- ✅ I will also be adding a EC11 rotary encoder, it should be helpful for volume/mode settings.

# June 10th 5:33 AM - 4h
- Completed Schematic. It was somewhat tedious and took longer than expected but everything looks good at the end at least. Will begin work on PCB now.

Low Res Preview of Schematic: 

![image](https://github.com/user-attachments/assets/adca0cd6-aaca-46dd-8a35-3622b7d13c3c)

# June 10th ~5:30 PM, ~6h
- Completed PCB. My experience with hackpad helped in this quite a bit. For some reason the keys didnt line up properly but I think I got everything in the right place (measured to confirm).

Preview of PCB:

![image](https://github.com/user-attachments/assets/e1bad259-8ecc-49dd-96f6-f23124d82013)

# June 11th
Instead of wiring the PCB, once I had arranged the switches/parts and was satisfied with they position, I worked on the 3D files of the keyboard so I could make changes to the structure while I still had the chance. I used the hackpad guide for this and it helped me greatly. Once this was finished I began wiring the PCB.

# June 12th 10:49 PM, ~10h
- Finally, after probably 10 hours of work, I have finished wiring the PCB. This was so unbelievably complicated and strenuous, but it has left me feeling really proud of what I made- this project may even be the most challenging thing I have done.

![image](https://github.com/user-attachments/assets/1f7c892b-70d2-49d4-b0b0-6b262a3bdd02)

This should conclude the project! I will add updates as I assemble the actual parts. 
