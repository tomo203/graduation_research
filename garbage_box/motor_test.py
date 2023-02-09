import time
import pigpio


# モータの制御
def motor_control(right_speed, left_speed):
    if right_speed >= 0:
        pi.write(IN_A_1, pigpio.HIGH)
        pi.write(IN_A_2, pigpio.LOW)

        right_param = right_speed
    else:
        pi.write(IN_A_1, pigpio.LOW)
        pi.write(IN_A_2, pigpio.HIGH)

        right_param = -right_speed

    if left_speed >= 0:
        pi.write(IN_B_1, pigpio.HIGH)
        pi.write(IN_B_2, pigpio.LOW)

        left_param = left_speed
    else:
        pi.write(IN_B_1, pigpio.LOW)
        pi.write(IN_B_2, pigpio.HIGH)

        left_param = -left_speed

    # pi.hardware_PWM(PWM_A, FREQ, right_param)
    # pi.hardware_PWM(PWM_B, FREQ, left_param)


# メイン
FREQ = 1000

# PWM_A = 12
# PWM_B = 13

IN_A_1 = 5
# IN_A_2 = 6
IN_A_2 = 12
IN_B_1 = 22
IN_B_2 = 27

pi = pigpio.pi('192.168.10.21')

# pi.set_mode(PWM_A, pigpio.OUTPUT)
# pi.set_mode(PWM_B, pigpio.OUTPUT)

pi.set_mode(IN_A_1, pigpio.OUTPUT)
pi.set_mode(IN_A_2, pigpio.OUTPUT)
pi.set_mode(IN_B_1, pigpio.OUTPUT)
pi.set_mode(IN_B_2, pigpio.OUTPUT)


pi.write(IN_A_1, pigpio.HIGH)
pi.hardware_PWM(IN_A_2, FREQ, 1000000)
time.sleep(0.5)

pi.write(IN_A_1, pigpio.HIGH)
pi.hardware_PWM(IN_A_2, FREQ, 800000)
time.sleep(3)

pi.write(IN_A_1, pigpio.HIGH)
pi.hardware_PWM(IN_A_2, FREQ, 500000)
time.sleep(3)

pi.write(IN_A_1, pigpio.HIGH)
pi.hardware_PWM(IN_A_2, FREQ, 300000)
time.sleep(3)

pi.write(IN_A_1, pigpio.HIGH)
pi.hardware_PWM(IN_A_2, FREQ, 100000)
time.sleep(3)

pi.write(IN_A_1, pigpio.HIGH)
pi.hardware_PWM(IN_A_2, FREQ, 0)
time.sleep(3)


pi.write(IN_A_1, pigpio.HIGH)
pi.write(IN_A_2, pigpio.HIGH)

# pi.write(IN_B_1, pigpio.HIGH)
# pi.write(IN_B_2, pigpio.HIGH)

# for i in range(3):
#     pi.write(IN_A_1, pigpio.HIGH)
#     pi.write(IN_A_2, pigpio.LOW)
#     pi.hardware_PWM(PWM_A, FREQ, 300000)
#
#     pi.write(IN_B_1, pigpio.HIGH)
#     pi.write(IN_B_2, pigpio.LOW)
#     pi.hardware_PWM(PWM_B, FREQ, 300000)
#
#     time.sleep(1)
#
#     pi.write(IN_A_1, pigpio.LOW)
#     pi.write(IN_A_2, pigpio.HIGH)
#     pi.hardware_PWM(PWM_A, FREQ, 000000)
#
#     pi.write(IN_B_1, pigpio.LOW)
#     pi.write(IN_B_2, pigpio.HIGH)
#     pi.hardware_PWM(PWM_B, FREQ, 000000)
#
#     time.sleep(0.5)
#
#     pi.write(IN_A_1, pigpio.LOW)
#     pi.write(IN_A_2, pigpio.HIGH)
#     pi.hardware_PWM(PWM_A, FREQ, 300000)
#
#     pi.write(IN_B_1, pigpio.LOW)
#     pi.write(IN_B_2, pigpio.HIGH)
#     pi.hardware_PWM(PWM_B, FREQ, 300000)
#
#     time.sleep(1)
#
#     pi.write(IN_A_1, pigpio.LOW)
#     pi.write(IN_A_2, pigpio.HIGH)
#     pi.hardware_PWM(PWM_A, FREQ, 000000)
#
#     pi.write(IN_B_1, pigpio.LOW)
#     pi.write(IN_B_2, pigpio.HIGH)
#     pi.hardware_PWM(PWM_B, FREQ, 000000)
#
#     time.sleep(0.5)
#
# pi.write(IN_A_1, pigpio.LOW)
# pi.write(IN_A_2, pigpio.HIGH)
# pi.hardware_PWM(PWM_A, FREQ, 000000)
#
# pi.write(IN_B_1, pigpio.LOW)
# pi.write(IN_B_2, pigpio.HIGH)
# pi.hardware_PWM(PWM_B, FREQ, 000000)

