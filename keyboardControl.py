from djitellopy import tello
import keyPressModule as kp
from time import sleep

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("u"):ud = speed
    elif kp.getKey("d"): ud = -speed

    if kp.getKey("a"):yv = -speed
    elif kp.getKey("s"): yv = speed

    if kp.getKey("t"):
        drone.takeoff()
    if kp.getKey("l"):
        drone.land()
        sleep(3)


    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)