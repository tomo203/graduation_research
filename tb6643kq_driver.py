import pigpio


class tb6643kq_driver:
    def __init__(self, pin_1=0, pin_2=0, pi="192.168.10.21", freq=1000, range=100) -> None:
        self.PIN_1 = pin_1
        self.PIN_2 = pin_2
        self.FREQ = freq

        self.pi = pigpio.pi(pi)

        self.pi.set_PWM_frequency(self.PIN_1, self.FREQ)
        self.pi.set_PWM_frequency(self.PIN_2, self.FREQ)

        self.pi.set_mode(self.PIN_1, pigpio.OUTPUT)
        self.pi.set_mode(self.PIN_2, pigpio.OUTPUT)
