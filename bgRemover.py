import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar
from rembg import remove 
from PIL import Image 
import os

def remove_background(input_folder, progress_bar):
    """
    Remove background from images in the input folder and save processed images in a folder named "output_images" in the same location as the input folder.
    
    Args:
    - input_folder (str): Path to the folder containing input images.
    - progress_bar (tk.Progressbar): Progress bar widget to update the progress.
    """
    # Create output directory if it doesn't exist
    output_folder = os.path.join(input_folder, "output_images")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Get the list of files in the input folder
    files = os.listdir(input_folder)
    num_files = len(files)
    
    # Initialize progress counter
    progress = 0
    
    # Process each image in the input folder
    for filename in files:
        # Construct the input and output file paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # Check if the file is an image
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                # Processing the image
                input_image = Image.open(input_path)
                
                # Removing the background from the given Image
                output_image = remove(input_image)
                
                # Saving the image in PNG format
                output_image.save(output_path.replace(".jpg", ".png").replace(".jpeg", ".png"))
        except Exception as e:
            print(f"Error processing {input_path}: {e}")
        
        # Update progress counter
        progress += 1
        percentage = (progress / num_files) * 100
        
        # Update progress bar
        progress_bar['value'] = percentage
        progress_bar.update()

def select_folder_and_run():
    # Open file dialog to select the input folder
    input_folder = filedialog.askdirectory()
    
    # Run the background removal process
    if input_folder:
        # Create Tkinter window for progress display
        progress_window = tk.Toplevel(root)
        progress_window.title("Progress")
        progress_window.geometry("300x50")
        
        # Create progress bar
        progress_bar = Progressbar(progress_window, orient="horizontal", length=300, mode="determinate")
        progress_bar.pack()
        
        # Run background removal process
        remove_background(input_folder, progress_bar)

# Create Tkinter window
root = tk.Tk()
root.title("Background Remover")

# Add button to select folder and run process
button = tk.Button(root, text="Select Input Folder", command=select_folder_and_run)
button.pack()

# Start Tkinter event loop
root.mainloop()
