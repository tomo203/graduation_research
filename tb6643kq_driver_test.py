import time
import pigpio
import tb6643kq_driver as driver

pi = pigpio.pi("192.168.137.125")

driverL = driver.Tb6643kq_driver(pi, 5, 6)
driverR = driver.Tb6643kq_driver(pi, 22, 27)


driverL.drive(-30)
driverR.drive(-30)
time.sleep(5)
driverL.drive(30)
driverR.drive(30)
time.sleep(5)
driverL.drive(30)
driverR.drive(-30)
time.sleep(5)
driverL.drive(-30)
driverR.drive(30)
time.sleep(5)
driverL.stop()
driverR.stop()