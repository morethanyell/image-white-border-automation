import cv2
import os, sys

def add_border(image_path, border_perc=12):
    # Read the image
    image = cv2.imread(image_path)
    
    # Determine longer and shorter sides
    height, width = image.shape[:2]
    if height > width:
        long_side = height
    else:
        long_side = width 
        
    border_size = long_side * border_perc // 100
    
    # Calculate new dimensions
    new_long_side = long_side + border_size
    
    # Calculate border sizes
    top_border = (new_long_side - height) // 2
    bottom_border = new_long_side - height - top_border
    left_border = (new_long_side - width) // 2
    right_border = new_long_side - width - left_border
    
    # Add white border
    bordered_image = cv2.copyMakeBorder(
        image, top_border, bottom_border, left_border, right_border,
        cv2.BORDER_CONSTANT, value=(255, 255, 255)
    )
    
    return bordered_image

def process_images_in_directory(directory):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Get the full path to the image file
            image_path = os.path.join(directory, filename)
            
            # Add border to the image
            bordered_image = add_border(image_path)
            
            # Save the bordered image
            output_path = os.path.join(directory, "bordered_" + filename)
            cv2.imwrite(output_path, bordered_image)
            print(f"Bordered image saved: {output_path}")

if __name__ == "__main__":
    # Check if the input directory is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_directory")
        sys.exit(1)
    
    # Get the input directory from the command-line argument
    input_directory = sys.argv[1]
    
    # Check if the input directory exists
    if not os.path.isdir(input_directory):
        print("Input directory does not exist.")
        sys.exit(1)
    
    # Process images in the specified directory
    process_images_in_directory(input_directory)