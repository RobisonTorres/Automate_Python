import re
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_nums(image=False):

    # This function reads and return only numbers from image.
    if not image:
        file = input('Type in the file\'s name: ')
        image = Image.open(file)

    #Remove all non-number characters.
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789#@'
    numbers_string = pytesseract.image_to_string(image, config=custom_config)
    numbers_int = re.sub(r'[a-z\n\s]', '', numbers_string.lower())
    
    return numbers_int

if __name__ == "__main__":

    print('Reading Images.')
    print()  
    print(read_nums())
