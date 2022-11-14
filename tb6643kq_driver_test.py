import time
import pigpio
import tb6643kq_driver as driver

pi = pigpio.pi("192.168.11.36")

driver = driver.Tb6643kq_driver(pi, 5, 6)

time.sleep(5)

driver.drive(100)
