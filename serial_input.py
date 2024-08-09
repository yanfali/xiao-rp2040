import board
import supervisor
import time
import neopixel

from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.color import GREEN, BLUE, RED, BLACK

print("waiting for input...")
rgb = False
pixel_pin = board.NEOPIXEL
pixel_num = 1
speed = 0.1
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.2, auto_write=False)  
pulse = Pulse(pixels, speed=speed, color=BLACK);

while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        # Sometimes Windows sends an extra (or missing) newline - ignore them
        if value == "":
            continue

        print("RX: {}".format(value))

        rgb = True
        if value == 'r':
          pulse = Pulse(pixels, speed=speed, color=RED)
        elif value == 'g':
          pulse = Pulse(pixels, speed=speed, color=GREEN)
        elif value == 'b':
          pulse = Pulse(pixels, speed=speed, color=BLUE)
        elif value=='f':
          pixels.brightness = 1.0
        elif value=='d':
          pixels.brightness = 0.2
        else:
          rgb = False
          # clear the pixel when we set to false
          Pulse(pixels, speed=0, color=[0,0,0]).animate()
    if rgb:
      # run the animation
      pulse.animate()

    time.sleep(0.25) ## sleep so we don't hog the CPU