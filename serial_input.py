import board
import supervisor
import time
import neopixel

from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.color import GREEN, BLUE, RED, YELLOW

print("waiting for input...")
rgb = False
pixel_pin = board.NEOPIXEL
pixel_num = 1
pixel_brightness = 0.1
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.1, auto_write=False)  
color = YELLOW;
pulse = Pulse(pixels, speed=0.1, color=YELLOW);
while True:
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        # Sometimes Windows sends an extra (or missing) newline - ignore them
        if value == "":
            continue
        print("RX: {}".format(value))
        if value == 'r':
          pulse = Pulse(pixels, speed=pixel_brightness, color=RED)
          rgb = True
        elif value == 'g':
          pulse = Pulse(pixels, speed=pixel_brightness, color=GREEN)
          rgb = True
        elif value == 'b':
          pulse = Pulse(pixels, speed=pixel_brightness*2, color=BLUE)
          rgb = True
        elif value == 'g':
          pulse = Pulse(pixels, speed=0.1, color=GREEN)
          rgb = True
        else:
          rgb = False
          Pulse(pixels, speed=0, color=[0,0,0]).animate()
    if rgb:
      pulse.animate()
    time.sleep(0.25)