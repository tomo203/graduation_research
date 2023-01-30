import pigpio
import hcsr04_driver as driver

pi = pigpio.pi("192.168.10.109")

driver = driver.hcsr04_driver(pi, 23, 24)

while True:
    distance = driver.get_distance()
    print(distance)
