import pigpio
import time
import sys
import hcsr04_driver as driver

pi = pigpio.pi("192.168.137.125")

driver = driver.hcsr04_driver(pi, 23, 24)

while True:
    try:
        distance = driver.get_distance()
        print(distance)

        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()

# pi = pigpio.pi("192.168.137.125")
# pi.set_mode(23, pigpio.OUTPUT)
# pi.set_mode(24, pigpio.INPUT)
# pi.write(23, pigpio.LOW)


# def get_distance():
#     sig_on = 0
#     sig_off = 0

#     # pi.gpio_trigger(23, 10, pigpio.HIGH)
#     pi.write(23, pigpio.HIGH)
#     time.sleep(0.00001)
#     pi.write(23, pigpio.LOW)

#     while pi.read(24) == pigpio.LOW:

#         print("b")

#         sig_on = time.time()
#     while pi.read(24) == pigpio.HIGH:
#         sig_off = time.time()

#     duration = sig_off - sig_on
#     distance = duration * 34000 / 2
#     return distance


# while True:
#     try:
#         distance = get_distance()
#         print("a")
#         if distance > 2 and distance < 400:
#             print(distance)

#         time.sleep(1)

#     except KeyboardInterrupt:
#         sys.exit()
