---
title: "Scalar's Keyboard"
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

# July 3rd 
Now that all parts have arrived, i began soldering the board. i started small by just soldering a couple of diodes for today.


# July 4th
I wanted to test some components before soldering them onto the PCB. I tested the pico, and once that was secured to the PCB, I worked on getting some of the firmware to work. All components work as intended thus far. It took me quite some time to get the hang of uploading firmware to the pico by way of adding the files to the circuitpy drive. etc. 

# July 5th and 6th 
I spent the last two days just soldering all of the remaining kalih hotswap sockets and diodes. Other than that, I soldered some small components such as the rotary encoder and the OLED panel. 

# July 7th and 8th. 
I worked on the firmware of the keyboard for these two days. I quickly realized that my original code was completely broken because it was untested and would not work. Due to this, I needed to completely make my code from scratch (fortunately it wasnt many lines). I discovered something odd with either my keyboard or KMK- for some reason the code wouldnt work when I added any keys to the next row but if I just kept adding keys to the first line they would register. At least the code works, although it might be pretty unsightly (check screenshot). I also started printing the case.


<img width="1586" height="375" alt="image" src="https://github.com/user-attachments/assets/5f9a4459-43a7-41c8-84ab-34183750f18e" />

# July 17th
After undercity, I got back to work on the case of the keyboard. After printing a number of failed top plate designs, I realized that I could print one that fits inside the case, flush with the top of the case. After spending around 1-2 hours modelling the top plate, I printed a plate that actually fit properly. I then spent a few hours removing all of the keycaps and keyswitches, inserting them into the top plate, and securing them to the pcb again. This essentially concludes the build process.
