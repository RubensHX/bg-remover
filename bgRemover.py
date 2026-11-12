import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from rembg import remove 
from PIL import Image 
import os
from typing import Optional

def remove_background(input_folder: str, progress_bar: Progressbar) -> None:
    output_folder = os.path.join(input_folder, "output_images")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    files = os.listdir(input_folder)
    num_files = len(files)
    
    progress = 0
    
    for filename in files:
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                input_image = Image.open(input_path)
                
                output_image = remove(input_image)
                
                output_image.save(output_path.replace(".jpg", ".png").replace(".jpeg", ".png"))
        except Exception as e:
            print(f"Error processing {input_path}: {e}")
        
        progress += 1
        percentage = (progress / num_files) * 100
        
        progress_bar['value'] = percentage
        progress_bar.update()

def select_folder_and_run() -> None:
    input_folder: Optional[str] = filedialog.askdirectory()
    
    if input_folder:
        progress_window = tk.Toplevel(root)
        progress_window.title("Progress")
        progress_window.geometry("300x50")
        
        progress_bar = Progressbar(progress_window, orient="horizontal", length=300, mode="determinate")
        progress_bar.pack()
        
        remove_background(input_folder, progress_bar)

root = tk.Tk()
root.title("Background Remover")

button = tk.Button(root, text="Select Input Folder", command=select_folder_and_run)
button.pack()

root.mainloop()
