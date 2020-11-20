from gpiozero import LED
from time import sleep

led4 = LED(4)
led17 = LED(17)
led23 = LED(23)
led19 = LED(19)
led6 = LED(6)
led22 = LED(22)

timeout=0.05

while True:
    led17.on()
    sleep(timeout)
    led17.off()
    sleep(timeout)
    
    led23.on()
    sleep(timeout)
    led23.off()
    sleep(timeout)
    
    led19.on()
    sleep(timeout)
    led19.off()
    sleep(timeout)
    
    led22.on()
    sleep(timeout)
    led22.off()
    sleep(timeout)
    
    led6.on()
    sleep(timeout)
    led6.off()
    sleep(timeout)
    
    led4.on()
    sleep(timeout)
    led4.off()
    sleep(timeout)
    
    