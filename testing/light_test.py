from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = [255, 255, 255]
b = [0, 0, 255]
e = [255,178,102]

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

sleep(2)

sense.clear()
