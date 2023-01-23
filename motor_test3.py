import time
import pigpio

# メイン
FREQ = 1000

IN_A_1 = 5
IN_A_2 = 6
IN_B_1 = 22
IN_B_2 = 27

t = 5

pi = pigpio.pi('192.168.137.125')

pi.set_mode(IN_A_1, pigpio.OUTPUT)
pi.set_mode(IN_A_2, pigpio.OUTPUT)
pi.set_mode(IN_B_1, pigpio.OUTPUT)
pi.set_mode(IN_B_2, pigpio.OUTPUT)

pi.set_PWM_frequency(IN_A_1, FREQ)
pi.set_PWM_frequency(IN_A_2, FREQ)
pi.set_PWM_frequency(IN_B_1, FREQ)
pi.set_PWM_frequency(IN_B_2, FREQ)

time.sleep(5)

pi.set_PWM_range(IN_A_1, 100)
pi.set_PWM_range(IN_A_2, 100)
pi.set_PWM_range(IN_B_1, 100)
pi.set_PWM_range(IN_B_2, 100)

pi.set_PWM_dutycycle(IN_A_1, 0)
pi.set_PWM_dutycycle(IN_A_2, 0)
pi.set_PWM_dutycycle(IN_B_1, 0)
pi.set_PWM_dutycycle(IN_B_2, 0)


pi.set_PWM_dutycycle(IN_A_1, 100)

pi.set_PWM_dutycycle(IN_A_2, 100)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_2, 80)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_2, 60)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_2, 40)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_2, 20)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_2, 0)
time.sleep(t)

pi.set_PWM_dutycycle(IN_A_1, 100)
pi.set_PWM_dutycycle(IN_A_2, 100)

pi.set_PWM_dutycycle(IN_A_2, 100)

pi.set_PWM_dutycycle(IN_A_1, 100)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_1, 80)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_1, 60)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_1, 40)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_1, 20)
time.sleep(t)
pi.set_PWM_dutycycle(IN_A_1, 0)
time.sleep(t)

pi.set_PWM_dutycycle(IN_A_1, 100)
pi.set_PWM_dutycycle(IN_A_2, 100)
time.sleep(1)
# pi.set_PWM_dutycycle(IN_A_1, 0)
# pi.set_PWM_dutycycle(IN_A_2, 0)
