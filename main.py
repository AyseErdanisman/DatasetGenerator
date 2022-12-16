import cv2
import os 

video = cv2.VideoCapture('teknofest.mp4')
currentFrame = 0

if not os.path.exists('data'):
    os.makedirs('data')

while(True):
    success, frame = video.read()
    cv2.imshow('Output', frame)
    cv2.imwrite('./data/farme' + str(currentFrame) + '.jpg', frame)
    currentFrame += 1

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

video.release()
video.destroyAllWindows()
