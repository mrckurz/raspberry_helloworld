from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=21, green=18, blue=12)

#led.red = 1  # full red
#sleep(1)
#led.red = 0.5  # half red
#sleep(1)

led.color = (0, 1, 0)  # full green
sleep(1)
led.color = (1, 0, 0) #full red
sleep(1)
led.color = (0, 0, 1) #full blue
sleep(1)
led.color = (1, 0, 1)  # magenta
sleep(1)
led.color = (1, 1, 0)  # yellow
sleep(1)
led.color = (0, 1, 1)  # cyan
sleep(1)
led.color = (1, 1, 1)  # white
sleep(1)

led.color = (0, 0, 0)  # off
sleep(1)

# slowly increase intensity of blue
for n in range(100):
    led.blue = n/100
    sleep(0.1)

led.color = (0, 0, 0)  # off
    
# slowly increase intensity of green
for n in range(100):
    led.green = n/100
    sleep(0.1)

led.color = (0, 0, 0)  # off
    
# slowly increase intensity of red
for n in range(100):
    led.red = n/100
    sleep(0.1)
    
led.color = (0, 0, 0)  # off

# slowly increase intensity of white
for n in range(100):
    led.red = n/100
    led.green = n/100
    led.blue = n/100
    sleep(0.1)
    
led.color = (0, 0, 0)  # off
    
#flash 10 times and turn off
for n in range(10):
    led.color = (1, 1, 1)  # white
    sleep(0.8)
    led.color = (0, 0, 0)  # off
    led.off()

#turnoff
led.color = (0, 0, 0)  # off