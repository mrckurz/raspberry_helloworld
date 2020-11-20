from gpiozero import LEDBoard
from time import sleep

leds = LEDBoard(4, 17, 23, 19, 6, 22)

for led in leds:
    led.on()
    sleep(1)
    led.off()