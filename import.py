import cv2
import numpy as np
import random

def generate_test_image():
    
    img = np.zeros((400, 400), dtype=np.uint8)
    
    
    for y in range(400):
        for x in range(400):
            if random.randint(0, 100) < 10:
                img[y, x] = random.randint(0, 50)
                
    
    cv2.circle(img, (100, 100), 20, (255), -1)
    cv2.circle(img, (300, 150), 25, (250), -1)
    cv2.circle(img, (200, 300), 15, (240), -1)
    
    return img

def nothing(x):
    pass

original_image = generate_test_image()

cv2.namedWindow("Result")

cv2.createTrackbar("Threshold", "Result", 200, 255, nothing)

print("Для выхода нажмите любую клавишу в окне с картинкой.")

while True:
    
    thresh_val = cv2.getTrackbarPos("Threshold", "Result")
    
   
    ret, binary = cv2.threshold(original_image, thresh_val, 255, cv2.THRESH_BINARY)
    
    
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    
    display_img = cv2.cvtColor(original_image, cv2.COLOR_GRAY2BGR)
    
    
    for contour in contours:
        
        M = cv2.moments(contour)
        
        
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            
            
            cv2.circle(display_img, (cX, cY), 4, (0, 0, 255), -1)
            
            
            text_coords = "X: " + str(cX) + ", Y: " + str(cY)
            
            
            cv2.putText(display_img, text_coords, (cX - 30, cY - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)
            
            
            print("Найден центроид с координатами: " + text_coords)
        else:
            
            pass

   
    cv2.imshow("Result", display_img)
    
    
    key = cv2.waitKey(1) & 0xFF
    if key != 255: 
        break

cv2.destroyAllWindows()