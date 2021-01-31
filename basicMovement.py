from djitellopy import tello
from time import sleep

drone = tello.Tello()
drone.connect()

drone.takeoff()
drone.send_rc_control(0, 0, 0, 0)
sleep(2)
drone.land()