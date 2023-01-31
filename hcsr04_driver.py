import time
import pigpio


class hcsr04_driver:
    def __init__(self, pi: pigpio.pi, trig: int, echo: int) -> None:
        self.pi = pi
        self.TRIG = trig
        self.ECHO = echo

        self.pi.set_mode(self.TRIG, pigpio.OUTPUT)
        self.pi.set_mode(self.ECHO, pigpio.INPUT)
        self.pi.write(self.TRIG, pigpio.LOW)

    def get_distance(self):
        self.pi.gpio_trigger(self.TRIG, 10, pigpio.HIGH)

        sig_on = 0
        sig_off = 0

        while self.pi.read(self.ECHO) == pigpio.LOW:
            sig_off = time.time()
        while self.pi.read(self.ECHO) == pigpio.HIGH:
            sig_on = time.time()

        duration = sig_off - sig_on
        distance = duration * 34000 / 2
        return distance
