# A Wifi enabled Claw

![Plastic claw, about 10" in total height, red body, grey arms with jagged teeth, connected to ESP32, voltage regulator, battery pack, and USB to a computer](https://github.com/justinb4003/esp32_claw/blob/main/images/theclaw.jpg?raw=true)

This is the claw device from the MDFBot project published on Chief Delphi: https://www.chiefdelphi.com/t/introducing-mdfbot/395694

I wanted to build the claw first and do a quick test of it but may have gotten carried away. I added a quick webserver to the project and made an Angular app that can be hosted elsewhere (like your local machine) to make calls back to the esp32.  It can be found here: https://github.com/justinb4003/claw-app/

Positioning of the servo is rather crude but gets the job done. Servo on the project is an MG 996R with an MT3608 bumping the 3V from the battery pack up to 7.2V for the servo. There are probably better ways of powering it, but this is what I had handy, and it mostly works fine.

## Build

### Tools

You'll need a soldering iron to attach headers to your ESP32 and attach wires to the voltage regulator. 

A volt meter is needed to calibrate the output of the MT3608.

A 3D printer is needed to build the claw parts.

### Parts

The 3D printed parts you'll have to pull from the STP published above at the MDFBot project, that is if you want the servo to even control that. There's no reason you can't hook it to anything else you want.

Everything else you can grab off Amazon.

https://smile.amazon.com/gp/product/B013GNC08C

Battery holders for 2 AA batteries (Less than $1 each)

https://smile.amazon.com/gp/product/B089JYBF25

DC-DC MT3608 step up voltage reulator

https://smile.amazon.com/gp/product/B07GD2BWPY

Just a few male-to-female jumper wires are needed, but I'm linking a large pack that I found handy. The whole thing is $5.99 currently.

https://smile.amazon.com/gp/product/B07MFK266B

The servo to actually move stuff around will be needed. These are around $6 each and struggle a bit with the claw arm right now but that's most likely due to battery supply than the servo itself.

https://smile.amazon.com/gp/product/B08DQQ8CBP

And then the ESP32 controller. There are many out there but this is the particular one I used, run about $8 each.

### Physical Build

Wire the positive and negative leads out of the battery pack into the MT3608 on the VIN+ and VIN- terminals. While the iron is hot split a male-to-female jumper cable in half and strip the ends, solder one each to the VOUT terminals on the voltage regulator.

The servo has three wires coming out of it: orange, red, and brown. Red and brown are your positive and common lines for the motor. Hook them to the male leads coming out of the voltage regulator that you just soldered on. Once wired up add batteries to the pack and measure output voltage on the MT3608. You want it to be between 5.0V and 7.2V when you're done. I found performance better at the higher end.

The orange line is for the PWM (Pulse Width Modulation) signal to tell the servo where to go. Hook that into the D13 pin of the ESP32 or whatever pin you want to use. The posted code uses D13 currently.

The ESP32 itself will be powered by the micro-USB port for now but we need to jump a common ground between the servo and the board, so one of the female leads coming off VIN- on the MT3608 need to go into a GND plug on the ESP32.

### Software

The app is built to run on MicroPython, so essentially load MicroPython firmware onto your ESP32 of choice and them drop the code in there. There's no special libraries that you need to install for this project.






