from PIL import Image
import pytesseract

'''
---------------------------------------------
IMPORTANT:
---------------------------------------------
Change the tessaract location in line 16
For installation guide please refer readme.md
---------------------------------------------
'''

class img2txt:

    def convert(self, image_name):
        tessaract_location = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
        pytesseract.pytesseract.tesseract_cmd = tessaract_location
        return(pytesseract.image_to_string(Image.open(image_name)))