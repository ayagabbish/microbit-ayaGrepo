# Write your code here :-)

from microbit import *
from ultrasonic import Ultrasonic
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()

ultrasonic_sensor = Ultrasonic()

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    motion = pin2.read_digital()
    if distance_value < 5 and motion == 1:
        sleep(1000)
        add_text(0, 0, "motion detected")
        pin0.write_digital(1)
        pin1.write_digital(1)
    else:
        add_text(0, 0, "no motion")
    display.scroll(str(int(distance_value)))
    sleep(2000)
