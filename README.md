# whiteb.py
#### Just a simple Python script that adds white border in all JPEG images in a given directory. 

I made this script to automate adding white borders to my photos. Hope it helps you too. :) 

#### Functionality
Makes your photos square by adding white borders. For horizontal images, a smaller white border is added on the width. Inversely for veritical images, a smaller white border is added on the length.

- This script adds 12% (pixels) of the longer side of the image
- Then it adds `((longer side + %12) - shorter side)` to the shorter side of the image
- The resulting new size of the image will be a square
- Does not overwrite the original file

#### Example
If you have a horizontal image with a width of 3000 and a length of 2000, it will add 360 white pixels on left and right (horizontally) and then 1720 white pixels on top and bottom (veritically).

#### Usage

- Install Python on your computer
- Download `whiteb.py` onto your computer
- Open your termninal and install the dependency using `pip` E.g.:
`pip install opencv-python` 
- To add white borders on your images, run the script like below
`python3 .\whiteb.py "C:\Users\myComputerUsername\Downloads\Images\Japan Trip 2024"`

Above script will start adding white borders to all JPEG images in the directory without overwriting the original images. The filename of the edited images will be `bordered_<original filename>.jpeg`
