# yart : Yet Another Raspberry Pi Telecine

## Changes:

 - Includes refactored GUI made by patsib: https://github.com/patsib/yart_gui
 - Support for TMC2209 UART with motor current control, use of stealthChop or spreadCycle: https://github.com/Chr157i4n/TMC2209_Raspberry_Pi
 - Uses stills port with JPEG Quality set to 100
 

## To-do:

 - Fix framerate get and test buttons (doesn't put the values in automatically, and also gives socket timeout error, otherwise seems to work)
 - Add support for RAW capturing and DNG conversion with PyDNG: https://github.com/schoolpost/PyDNG
 

![Screenshot](https://github.com/jokubasver/yart/blob/master/img/capture.jpg)

## Original Text:

First I have to thank Joe Herman for his project https://github.com/jphfilm/rpi-film-capture. My project is not a fork because all the software part has been rewritten. However, the concept and whole hardware part takes up Joe's ideas.

The app works for me and I captured several hours of movies. However the code is still experimental and requires some polishing.

Documentation (in french ! Google translate is your best friend)

[yart.md](./yart.md)

**Note that this documentation dates from the beginning of the project and may be obsolete at some points. It is essential to consult the Google group, which contains all the advice and experiences of the users.**

Google group

https://groups.google.com/forum/#!forum/yart

