# PicoLoad

Picoload is a script to upload FW files to a Raspberrypi-Pico on a Linux system.
By time of the first relase, I was not able to upload a FW to the Pico using PlatformIOs built-in tool.
So I wrote picoload.py script.

To use in PlatformIO copy picoload.py in the same folder as platformio.ini and change the upload section of the environment:

*********************************

[env:pico]

platform = raspberrypi

board = pico

framework = arduino

upload_protocol = custom

upload_port = /media/$$USER/RPI-RP2

upload_command  = ./picoload.py $SOURCE $UPLOAD_PORT 

*********************************
Change <upload_port> if the above is not matching to your system!

Don't forget to make the script executable
