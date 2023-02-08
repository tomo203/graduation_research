import time
import pigpio

# https://qiita.com/yoroyasu/items/8fb806199f629aa9d277


class hcsr04_driver:
    def __init__(self, pi: pigpio.pi, trig: int, echo: int) -> None:
        self.pi = pi
        self.TRIG = trig
        self.ECHO = echo
        self.distance = 0

        self.pi.set_mode(self.TRIG, pigpio.OUTPUT)
        self.pi.set_mode(self.ECHO, pigpio.INPUT)

        cb = self.pi.callback(self.ECHO, pigpio.EITHER_EDGE, self.cbf)

    def cbf(self, gpio, level, tick):  # call back function for pulse detect _/~~\__
        global t_rise, t_fall

        if (level == 1):  # right after the rising edge
            t_rise = tick
        else:            # right after the falling edge
            t_fall = tick
            if (t_fall >= t_rise):  # if wrapped 32bit value,
                timepassed = t_fall - t_rise
            else:
                timepassed = t_fall + (0xffffffff + 1 - t_rise)

            # meter to cm, microseconds to seconds, divide by 2
            self.distance = 340 * 100 * timepassed / 1000000 / 2

    def get_distance(self):
        self.pi.gpio_trigger(self.TRIG, 10, 1)  # Trig (10μs pulse)
        # wait for echo signal for 100msec (enough..., I believe...)
        time.sleep(0.1)
        return self.distance
