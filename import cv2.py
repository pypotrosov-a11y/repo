import cv2
import numpy as np
import random

class FrameProcessor:
    def __init__(self):
        self.original_image = None
        self.gray_image = None
        self.smoothed_image = None

    def generate_frame(self):

        img = np.zeros((300, 300, 3), dtype=np.uint8)
        
        
        img[:] = (100, 100, 100)
        
        
        cv2.rectangle(img, (50, 50), (150, 150), (0, 255, 0), -1)
        cv2.circle(img, (220, 220), 40, (0, 0, 255), -1)
        
        
        for y in range(300):
            for x in range(300):
                if random.randint(0, 100) < 10: 
                    if random.randint(0, 1) == 0:
                        img[y, x] = (0, 0, 0) 
                    else:
                        img[y, x] = (255, 255, 255) 
        
        self.original_image = img

    def process_frame(self):
        if self.original_image is None:
            print("Сначала сгенерируйте кадр!")
            return

       
        self.gray_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)

        
        
        self.smoothed_image = cv2.medianBlur(self.gray_image, 5)

    def show_results(self):
        if self.smoothed_image is None:
            print("Нет данных для показа. Выполните обработку.")
            return

        
        cv2.imshow("1. Original (with noise)", self.original_image)
        
        cv2.imshow("2. Gray", self.gray_image)
        
        cv2.imshow("3. Smoothed (No Noise)", self.smoothed_image)
        
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()

processor = FrameProcessor()

processor.generate_frame()

processor.process_frame()

processor.show_results()