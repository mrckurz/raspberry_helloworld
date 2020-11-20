from gpiozero import LED
from gpiozero import RGBLED
from gpiozero import Button
from time import sleep

button = Button(16)
led4 = LED(4)
led17 = LED(17)
led23 = LED(23)
led19 = LED(19)
led6 = LED(6)
led22 = LED(22)
led25 = LED(25)
led = RGBLED(red=21, green=18, blue=12)
led2 = RGBLED(red=27, green=5, blue=26)

while True:
        if button.is_pressed:
            print("Button is pressed")
            led4.on()
            led17.on()
            led23.on()
            led19.on()
            led6.on()
            led22.on()
            led.color = (0, 1, 0)  # white
            led2.color = (0, 1, 0)  # white
            led25.on()
        else:
            print("Button is not pressed")
            led4.off()
            led17.off()
            led23.off()
            led19.off()
            led6.off()
            led22.off()
            led.off()
            led2.off()
            led25.off()
        sleep(0.2)