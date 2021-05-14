import cv2
import numpy as np

cap = cv2.VideoCapture(0)

bg = cv2.imread(r'C:\Users\Arsh Agarwal\OneDrive\WhiteHat\Python\WhiteHat Projects\C121\replaced_image.jpg', 1)
bg = cv2.resize(bg, (640, 480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = np.flip(frame, axis=1)
    
    l_black = np.array([43, 43, 43])
    u_black = np.array([0, 0, 0])

    mask1 = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, bg, mask = mask1)

    f = frame - res
    f = np.where(f == 0, bg, f)

    
    cv2.imshow('Magic', f)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()