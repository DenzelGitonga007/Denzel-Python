from rembg import remove
from PIL import Image

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

if __name__ == "__main__":
    input_path = input("Enter the path to the input image: ")
    output_path = input("Enter the path to save the output image: ")
    
    remove_background(input_path, output_path)



# input_path = "D:\gtest.png"
# output_path = "D:\output.png"  # Save as PNG

# img_process = Image.open(input_path).convert("RGBA")  # Convert to RGBA
# output = remove(img_process)
# output.save(output_path)

# # Close the images
# img_process.close()
# output.close()
