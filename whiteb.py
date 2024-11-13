#!/usr/bin/env python3

# Author: morethanyell (daniel.l.astillero@gmail.com)
# Description: Adds white border to JPEG images in a directory. The default outputfile appends "bordered_" to the filenames.

import cv2
import os
import sys
import argparse

def add_border(image_path, border_perc=12, aspect_ratio='sq'):
    # Read the image
    image = cv2.imread(image_path)
    
    # Determine longer and shorter sides
    height, width = image.shape[:2]
    
    # Calculate longer side after adding border
    long_side = max(height, width)
    border_size = int(long_side * border_perc // 100)
    
    top, bottom, left, right = 0, 0, 0, 0
    
    if aspect_ratio == 'instav':
        
        if height > width:
            top, bottom = border_size, border_size
            new_height = height + (2 * border_size)
            new_width = (new_height * 4) / 5
            left, right = int((new_width - width) / 2), int((new_width - width) / 2)
        else:
            left, right = border_size, border_size
            new_width = width + (2 * border_size)
            new_height = (new_width * 5) / 4
            top, bottom = int((new_height - height) / 2), int((new_height - height) / 2)
              
        image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        
    elif aspect_ratio == 'instah':
        
        if height > width:
            top, bottom = border_size, border_size
            new_height = height + (2 * border_size)
            new_width = (new_height * 5) / 4
            left, right = int((new_width - width) / 2), int((new_width - width) / 2)
        else:
            left, right = border_size, border_size
            new_width = width + (2 * border_size)
            new_height = (new_width * 4) / 5
            top, bottom = int((new_height - height) / 2), int((new_height - height) / 2)
              
        image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        
    elif aspect_ratio == 'ofpxl':
        
        top, bottom, left, right = 150, 150, 150, 150
              
        image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        
    else:
        
        new_height = int(height + 2 * border_size)
        new_width = int(width + 2 * border_size)
        
        image = cv2.copyMakeBorder(image, border_size, border_size, border_size, border_size, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        
        # Crop to make square
        if new_height > new_width:
            image = cv2.copyMakeBorder(image, 0, 0, (new_height - new_width) // 2, (new_height - new_width) // 2, cv2.BORDER_CONSTANT, value=(255, 255, 255))
        elif new_width > new_height:
            image = cv2.copyMakeBorder(image, (new_width - new_height) // 2, (new_width - new_height) // 2, 0, 0, cv2.BORDER_CONSTANT, value=(255, 255, 255))
    
    return image

def process_images_in_directory(directory, border_perc, overwrite_orig, aspect_ratio, qual):
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        
        if not filename.endswith((".jpg", ".jpeg")):
            print("Skipping this file as it is not a JPEG image. Sorry.")
            continue
        
        if filename.startswith("bordered_"):
            print(f"Skipping an already bordered image.: {filename}")
            continue
        
        # Get the full path to the image file
        image_path = os.path.join(directory, filename)
        
        # Add border to the image
        bordered_image = add_border(image_path, border_perc, aspect_ratio)
        
        # Decide whether to overwrite the original or save with prefix
        if overwrite_orig.lower() == 'y':
            output_path = image_path
        else:
            output_path = os.path.join(directory, "bordered_" + filename)

        # Save the bordered image
        cv2.imwrite(output_path, bordered_image, [cv2.IMWRITE_JPEG_QUALITY, qual])
        print(f"Bordered image saved: {output_path}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Add white border to images")
    parser.add_argument("input_directory", help="Directory containing images")
    parser.add_argument("--border-perc", type=float, default=12, help="Percentage of border thickness (must be greater than 0)")
    parser.add_argument("--overwrite-orig", choices=['y', 'n'], default='n', help="Whether to overwrite original files (y/n)")
    parser.add_argument("--ar", choices=['instav', 'instah', 'ofpxl', 'sq'], default='sq', help="Aspect ratio: instav, instah, or sq (default: sq)")
    parser.add_argument("--qual", type=int, default=100, help="JPEG quality. Defaults to 85%")
    args = parser.parse_args()
    
    # Check if the border percentage is greater than 0
    if args.border_perc <= 0:
        print("Error: Border percentage must be greater than 0.")
        sys.exit(1)
    
    if args.qual > 100 or args.qual < 1:
        print(f"JPEG quality selected must be from 1 to 100. Defaulting to 100% instead.")
        qual = 100
    
    # Check if the input directory exists
    if not os.path.isdir(args.input_directory):
        print("Input directory does not exist.")
        sys.exit(1)
    
    # Process images in the specified directory
    process_images_in_directory(args.input_directory, args.border_perc, args.overwrite_orig, args.ar, args.qual)
