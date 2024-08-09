# Circuit Python experiments

## Description

I ordered some Xiao RP2040s a while back, intending to create a blinking device that would allow me to identify a server pretty quickly from a bunch of identical boxes in your homelab. This is my experiments with the device and piecing together tutorials so I can send input to the xiao and then make it change the RGB LED on demand. It's more for fun, but it could be useful if you have a large number of identical boxes and you're not sure which one is which when they are racked up.

It was also pretty easy to come up with a primitive mouse jiggler using only a few lines of circuit python. The Circuit python libraries are definitely very powerful.

## To do

Probably get a 3D printer working again and coming up with some kind of case.

## Dependencies

1. vscode + [circuit python extension](https://marketplace.visualstudio.com/items?itemName=joedevivo.vscode-circuitpython)
2. circuit python version 9.1.1
3. golang 1.22 and serial 