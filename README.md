# whiteb.py
#### Just a simple Python script that adds white border in all JPEG images in a given directory. 

I made this script to automate adding white borders to my photos. Hope it helps you too. :) 

#### Usage

- Install Python on your computer
- Download `whiteb.py` onto your computer
- Open your termninal and install the dependency using `pip` E.g.:
`pip install opencv-python` 
- To add white borders on your images, run the script like below
    - `python3 .\whiteb.py "C:\Users\myComputerUsername\Downloads\Images\Japan Trip 2024"`
    - Above script will start adding white borders to all JPEG images in the directory without overwriting the original images. The filename of the edited images will be `bordered_<original filename>.jpeg`
- You include the following flags
    - Aspect Ratio: `--ar=[instav|instah|sq|ofpxl]` 
        - `sq` is the default
        - `instav` results to adding border such that new AR is Instagram-friendly vertical 5:4 image
        - `instah` results to adding border such that new AR is Instagram-friendly vertical 4:5 image
        - `ofpxl` results to adding 150-pixel equally to all sides of the image
    - Border Percentage: `--border-perc=float`
        - Accepts values from 1 to 99. Defaults to 12.
        - The border thickness derived from the image's shorter side, e.g.: a horizontal image with a leght of 1000 will add 100 pixels top and bottom if `--border-perc=10` is supplied
    - Overwrite Original: `--overwrite-orig=[y|n]`
        - Self-explanatory. Defaults to `n`
    - JPEG Quality: `--qual=integer`
        - Leverages `cv2.IMWRITE_JPEG_QUALITY` value from 0-100, where 100 results to highest possible JPEG quality