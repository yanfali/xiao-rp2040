"""Example for Pico. Blinks the built-in LED."""
import board
import neopixel

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.color import MAGENTA

pixel_pin = board.NEOPIXEL

pixel_num = 1

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.1, auto_write=False)

blink = Rainbow(pixels, speed=0.5)

while True:
    blink.animate()
