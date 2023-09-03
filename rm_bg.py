from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def remove_background(input_path, output_path):
    try:
        # Open the input image
        process = Image.open(input_path).convert("RGBA")
        
        # Remove the background
        output = remove(process)
        
        # Save the output image
        output.save(output_path)
        
        # Close the images
        process.close()
        output.close()
        
        print("Background removed and saved successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

def select_input_image():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select the image to remove background")
    return file_path

def select_output_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(title="Select where to save the new image")
    return file_path

if __name__ == "__main__":
    input_path = select_input_image()
    output_path = select_output_path()
    
    if input_path and output_path:
        remove_background(input_path, output_path)
    else:
        print("Operation canceled.")
