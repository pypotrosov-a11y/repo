import tkinter as tk
from tkinter import ttk

def process_image():
 threshold_value = scale.get()
 result_text = "Порог яркости бликов: " + str(threshold_value)
 label_result.config(text=result_text)

window = tk.Tk()
window.title("Задача 1: Поиск локальных максимумов")
window.geometry("400x250")

notebook = ttk.Notebook(window)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Настройки")

label_info = tk.Label(tab1, text="Порог яркости бликов:")
label_info.pack(pady=10)

scale = tk.Scale(tab1, from_=200, to=255, orient=tk.HORIZONTAL, length=300)
scale.set(230) 
scale.pack(pady=5)

btn_process = tk.Button(tab1, text="Локализовать источники", command=process_image)
btn_process.pack(pady=10)

label_result = tk.Label(tab1, text="Ожидание обработки...")
label_result.pack(pady=10)

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Результат")

label_placeholder = tk.Label(tab2, text="Здесь будет отображаться\nрезультат локализации источников\n(изображение)")
label_placeholder.pack(expand=True)

window.mainloop()