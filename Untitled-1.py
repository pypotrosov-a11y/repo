from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
import random

class ImageProcessorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Задача 4: Комплексное приложение")
        self.window.geometry('500x550')
        self.image = None
        self.result_image = None 

        
        
        self.btn_gen = Button(window, text="Сгенерировать кадр", command=self.generate_image)
        self.btn_gen.grid(column=0, row=0, padx=10, pady=10)

        self.btn_load = Button(window, text="Загрузить из файла", command=self.load_image)
        self.btn_load.grid(column=1, row=0, padx=10, pady=10)

        self.lbl_thresh = Label(window, text="Порог бинаризации:")
        self.lbl_thresh.grid(column=0, row=1, padx=10, pady=5)

        self.scale_threshold = Scale(window, from_=0, to=255, orient=HORIZONTAL)
        self.scale_threshold.set(200)
        self.scale_threshold.grid(column=1, row=1, padx=10, pady=5)

        self.btn_proc = Button(window, text="Найти центроиды", command=self.process_image)
        self.btn_proc.grid(column=0, row=2, columnspan=2, padx=10, pady=10)
        
        
        self.btn_save = Button(window, text="Сохранить результат", command=self.save_image)
        self.btn_save.grid(column=0, row=3, columnspan=2, padx=10, pady=5)

        self.lbl_info = Label(window, text="Координаты центроидов появятся здесь")
        self.lbl_info.grid(column=0, row=4, columnspan=2, padx=10, pady=5)

        self.panel = Label(window)
        self.panel.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

    def generate_image(self):
        img = np.zeros((300, 300), dtype=np.uint8)
        for y in range(300):
            for x in range(300):
                if random.randint(0, 100) < 15:
                    img[y, x] = random.randint(0, 50)
                    
        cv2.circle(img, (80, 80), 20, (255), -1)
        cv2.circle(img, (220, 150), 25, (250), -1)
        cv2.circle(img, (150, 230), 15, (240), -1)
        
        self.image = img
        self.show_image(self.image)

    def load_image(self):
        path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png *.bmp")])
        if path:
            self.image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            self.show_image(self.image)

    def process_image(self):
        if self.image is None:
            self.lbl_info.configure(text="Сначала сгенерируйте или загрузите кадр!")
            return

        thresh_val = self.scale_threshold.get()
        ret, binary = cv2.threshold(self.image, thresh_val, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        display_img = cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)
        coords_text = "Координаты: "
        count = 0

        for contour in contours:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                
                
                cv2.circle(display_img, (cX, cY), 15, (0, 255, 0), 2)
                
               
                cv2.line(display_img, (cX - 20, cY), (cX + 20, cY), (0, 255, 0), 1) 
                cv2.line(display_img, (cX, cY - 20), (cX, cY + 20), (0, 255, 0), 1) 
                
                coords_text = coords_text + "(" + str(cX) + ", " + str(cY) + ")  "
                count = count + 1

        if count == 0:
            coords_text = "Пересвеченные зоны не найдены. Снизьте порог."
        else:
            
            self.result_image = display_img

        self.lbl_info.configure(text=coords_text)
        self.show_image(display_img)

    def save_image(self):
        
        if self.result_image is None:
            self.lbl_info.configure(text="Сначала выполните обработку!")
            return
            
        
        path = filedialog.asksaveasfilename(
            defaultextension=".png", 
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
        )
        if path:
            cv2.imwrite(path, self.result_image)
            self.lbl_info.configure(text="Результат успешно сохранен!")

    def show_image(self, img):
        temp_file = "temp_result.ppm"
        cv2.imwrite(temp_file, img)
        img_tk = PhotoImage(file=temp_file)
        self.panel.configure(image=img_tk)
        self.panel.image = img_tk

root = Tk()
app = ImageProcessorApp(root)
root.mainloop()