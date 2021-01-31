from djitellopy import tello
import keyPressModule as kp
import time
import cv2

kp.init()
drone = tello.Tello()
drone.connect()
print(drone.get_battery())

global img
drone.stream_on()

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
        time.sleep(3)

    if kp.getKey("p"):
        cv2.imwrite(f'Sources / pictures / {time.time()}.jpg', img)
        time.sleep(0.3)


    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    drone.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imread("Video", img)
    cv2.waitKey(1)
