import time
import pigpio


class Tb6643kq_driver:
    def __init__(self, pi: pigpio.pi, pin_1: int, pin_2: int, freq=1000, range=100) -> None:
        self.pi = pi

        self.PIN_1 = pin_1
        self.PIN_2 = pin_2
        self.FREQ = freq
        self.RANGE = range

        self.pi.set_PWM_frequency(self.PIN_1, freq)
        self.pi.set_PWM_frequency(self.PIN_2, freq)

        self.pi.set_PWM_range(self.PIN_1, range)
        self.pi.set_PWM_range(self.PIN_2, range)

        self.pi.set_mode(self.PIN_1, pigpio.OUTPUT)
        self.pi.set_mode(self.PIN_2, pigpio.OUTPUT)

    def drive(self, speed: int) -> None:
        follow_pin = self.PIN_1
        back_pin = self.PIN_2

        if speed < 0:
            follow_pin = self.PIN_2
            back_pin = self.PIN_1
            speed = -speed

        self.pi.set_PWM_dutycycle(follow_pin, self.RANGE)
        self.pi.set_PWM_dutycycle(back_pin, self.RANGE - speed)

    def accelatation(self, start: int, end: int, at_time: int) -> None:
        at = (end - start) / at_time

        for i in range(start, end, at):
            self.drive(i)
            time.sleep(1)

    def stop(self) -> None:
        self.pi.set_PWM_dutycycle(self.PIN_1, self.RANGE)
        self.pi.set_PWM_dutycycle(self.PIN_2, self.RANGE)
