import time
import cv2
import pigpio


if __name__ == '__main__':
    LED_PIN = 20
    pi = pigpio.pi('192.168.10.21')
    pi.set_mode(LED_PIN, pigpio.OUTPUT)

    while True:
        pi.write(LED_PIN, pigpio.HIGH)
        time.sleep(0.5)
        pi.write(LED_PIN, pigpio.LOW)
        time.sleep(0.5)
        key = cv2.waitKey(1)
