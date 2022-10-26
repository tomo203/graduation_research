from turtle import back
import pigpio


class tb6643kq_driver:
    def __init__(self, pin_1, pin_2, pi="192.168.10.21", freq=1000, range=100) -> None:
        self.PIN_1 = pin_1
        self.PIN_2 = pin_2
        self.RANGE = range

        self.pi = pigpio.pi(pi)

        self.pi.set_PWM_frequency(self.PIN_1, freq)
        self.pi.set_PWM_frequency(self.PIN_2, freq)

        self.pi.set_PWM_range(self.PIN_1, range)

        self.pi.set_mode(self.PIN_1, pigpio.OUTPUT)
        self.pi.set_mode(self.PIN_2, pigpio.OUTPUT)

    def drive(self, speed):
        follow_pin = self.PIN_1
        back_pin = self.PIN_2

        if speed < 0:
            follow_pin = self.PIN_2
            back_pin = self.PIN_1
            speed = -speed

        self.pi.set_PWM_dutycycle(follow_pin, 100)
        self.pi.set_PWM_dutycycle(back_pin, self.RANGE - speed)
