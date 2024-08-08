import usb_hid
import time
from adafruit_hid.mouse import Mouse

m = Mouse(usb_hid.devices)

while True:
  m.move(-1,0,0);
  m.move(1,0,0);
  print('jiggled')
  time.sleep(60);

