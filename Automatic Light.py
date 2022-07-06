# Add your Python code here. E.g.

from microbit import *
from ultrasonic import Ultrasonic

ultrasonic_sensor = Ultrasonic()
def distance():
    if distance_value < 25:
        pin0.write_digital(1)
    else:
        pin0.write_digital(0)

while True:
    
    distance_value = ultrasonic_sensor.measure_distance_cm()
    display.scroll(str(int(distance_value)))
    if pin1.read_digital() <= 200:
        distance()