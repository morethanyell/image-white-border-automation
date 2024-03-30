import cv2
import os
import sys
import argparse

def add_border(image_path, border_perc=12):
    # Read the image
    image = cv2.imread(image_path)
    
    # Determine longer and shorter sides
    height, width = image.shape[:2]
    
    long_side = height if height > width else width
        
    border_size = long_side * border_perc // 100
    
    # Calculate new dimensions
    new_long_side = long_side + border_size
    
    # Calculate border sizes and ensure they are integers
    top_border = int((new_long_side - height) // 2)
    bottom_border = int(new_long_side - height - top_border)
    left_border = int((new_long_side - width) // 2)
    right_border = int(new_long_side - width - left_border)
    
    # Add white border
    bordered_image = cv2.copyMakeBorder(
        image, top_border, bottom_border, left_border, right_border,
        cv2.BORDER_CONSTANT, value=(255, 255, 255)
    )
    
    return bordered_image

def process_images_in_directory(directory, border_perc, overwrite_orig):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Get the full path to the image file
            image_path = os.path.join(directory, filename)
            
            # Add border to the image
            bordered_image = add_border(image_path, border_perc)
            
            # Decide whether to overwrite the original or save with prefix
            if overwrite_orig.lower() == 'y':
                output_path = image_path
            else:
                output_path = os.path.join(directory, "bordered_" + filename)
            
            # Save the bordered image
            cv2.imwrite(output_path, bordered_image)
            print(f"Bordered image saved: {output_path}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Add white border to images")
    parser.add_argument("input_directory", help="Directory containing images")
    parser.add_argument("--border-perc", type=float, default=12, help="Percentage of border thickness (must be greater than 0)")
    parser.add_argument("--overwrite-orig", choices=['y', 'n'], default='n', help="Whether to overwrite original files (y/n)")
    args = parser.parse_args()
    
    # Check if the border percentage is greater than 0
    if args.border_perc <= 0:
        print("Error: Border percentage must be greater than 0.")
        sys.exit(1)
    
    # Check if the input directory exists
    if not os.path.isdir(args.input_directory):
        print("Input directory does not exist.")
        sys.exit(1)
    
    # Process images in the specified directory
    process_images_in_directory(args.input_directory, args.border_perc, args.overwrite_orig)
