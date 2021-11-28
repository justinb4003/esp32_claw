# A Wifi enabled Claw

![Plastic claw, about 10" in total height, red body, grey arms with jagged teeth, connected to ESP32, voltage regulator, battery pack, and USB to a computer](https://github.com/justinb4003/esp32_claw/blob/main/images/theclaw.jpg?raw=true)

This is the claw device from the MDFBot project published on Chief Delphi: https://www.chiefdelphi.com/t/introducing-mdfbot/395694

I wanted to build the claw first and do a quick test of it but may have gotten carried away. I added a quick webserver to the project and made an Angular app that can be hosted elsewhere (like your local machine) to make calls back to the esp32.  It can be found here: https://github.com/justinb4003/claw-app/

Positioning of the servo is rather crude but gets the job done. Servo on the project is an MG 996R with an MT3608 bumping the 3V from the battery pack up to 7.2V for the servo. There are probably better ways of powering it, but this is what I had handy, and it mostly works fine.

