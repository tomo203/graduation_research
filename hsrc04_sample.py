# one shot measurement only
#
import pigpio
import time

HC_SR04_trig = 23
HC_SR04_echo = 24

pi = pigpio.pi("192.168.137.125")
pi.set_mode(HC_SR04_trig, pigpio.OUTPUT)
pi.set_mode(HC_SR04_echo, pigpio.INPUT)

t_rise = 0
t_fall = 0


def cbf(gpio, level, tick):  # call back function for pulse detect _/~~\__
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
        d = 340 * 100 * timepassed / 1000000 / 2
        print('{"tick":%10d, "time_us": %6d, "distance_cm": %.2f}' % (
            tick, timepassed, d))


cb = pi.callback(HC_SR04_echo, pigpio.EITHER_EDGE, cbf)
while True:
    pi.gpio_trigger(HC_SR04_trig, 10, 1)  # Trig (10μs pulse)
    # wait for echo signal for 100msec (enough..., I believe...)
    time.sleep(0.1)
    time.sleep(1)

pi.stop()
