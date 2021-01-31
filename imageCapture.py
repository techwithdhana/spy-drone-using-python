from djitellopy import tello
import cv2

drone = tello.Tello()
drone.connect()
drone.stream_on()

while True:
    img = drone.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imread("Video", img)
    cv2.waitKey(1)

