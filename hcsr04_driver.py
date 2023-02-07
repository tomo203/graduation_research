import time
import pigpio

# https://qiita.com/yoroyasu/items/8fb806199f629aa9d277


class hcsr04_driver:
    def __init__(self, pi: pigpio.pi, trig: int, echo: int) -> None:
        self.pi = pi
        self.TRIG = trig
        self.ECHO = echo

        self.pi.set_mode(self.TRIG, pigpio.OUTPUT)
        self.pi.set_mode(self.ECHO, pigpio.INPUT)

    def cbf(self, gpio, level, tick):  # call back function for pulse detect _/~~\__
        t_rise = 0
        t_fall = 0

        if (level == 1):  # right after the rising edge
            t_rise = tick
        else:            # right after the falling edge
            t_fall = tick
            if (t_fall >= t_rise):  # if wrapped 32bit value,
                timepassed = t_fall - t_rise
            else:
                timepassed = t_fall + (0xffffffff + 1 - t_rise)

            # meter to cm, microseconds to seconds, divide by 2
            d = 340 * 100 * timepassed / 1000000 / 2

            return d

    def get_distance(self):
        cb = self.pi.callback(self.ECHO, pigpio.EITHER_EDGE, self.cbf)
