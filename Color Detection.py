import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

global x,y

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape
    #cx = int(width / 2)
    #cy = int(height / 2)
    
    x=0
    y=0
    
    dim = (1080, 720)
    frame = cv2.resize(frame, dim)
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(grey_frame, 150, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(
        image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE
    )

    cv2.drawContours(
        image=frame,
        contours=contours,
        contourIdx=-1,
        color=(0, 255, 0),
        thickness=2,
        lineType=cv2.LINE_AA,
    )
    
    for contour in contours:

        approx = cv2.approxPolyDP(
            contour, 0.01 * cv2.arcLength(contour, True), True)

        cv2.drawContours(frame, [contour], 0, (0, 0, 0), 0)

        M = cv2.moments(contour)
        if M['m00'] != 0.0:
            x = int(M['m10']/M['m00'])
            y = int(M['m01']/M['m00'])
        
        # Pick pixel value
        pixel_center = hsv_frame[y, x]
        hue_value = pixel_center[0]
        color = "Undefined"
        if hue_value < 5:
            color = "RED"
        elif hue_value < 22:
            color = "ORANGE"
        elif hue_value < 33:
            color = "YELLOW"
        elif hue_value < 78:
            color = "GREEN"
        elif hue_value < 131:
            color = "BLUE"
        elif hue_value < 170:
            color = "VIOLET"
        else:
            color = "RED"
    
        # putting shape name at center of each shape
        if len(approx) == 3:
            cv2.putText(frame, color, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)

  
        elif len(approx) == 4:
            cv2.putText(frame, color, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)

  
        elif len(approx) == 5:
            cv2.putText(frame, color, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)

  
        elif len(approx) == 6:
            cv2.putText(frame, color, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)

  
        #elif len(approx) == 0:
            #cv2.putText(frame, color, (x, y),
                        #cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            #cv2.circle(frame, (x, y), 5, (255, 255, 255), -1)
    
    
        pixel_center_bgr = frame[y, x]
        #b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
        #cv2.rectangle(frame, (x - 220, 10), (x + 200, 120), (255, 255, 255), -1)
        #cv2.putText(frame, color, (x - 200, 100), 0, 3, (b, g, r), 5)
        #cv2.circle(frame, (x, y), 5, (25, 25, 25), 3)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release
cv2.destroyAllWindows()