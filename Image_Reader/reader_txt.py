from PIL import Image
import pytesseract
print('Reading Images.')
print()

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def read_text():

    # This function reads and returns text from image.
    image = input('Type in the file\'s name: ')
    file = Image.open(image)
    text = pytesseract.image_to_string(file)
    return '\n' + text

print(read_text())
