
class img2txt:

    def convert(self, image_name):
        try:
            from PIL import Image
        except ImportError:
            import Image
        import pytesseract

        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'
        return(pytesseract.image_to_string(Image.open(image_name)))

# Test function
# a = img2txt()
# print(a.convert("test.png"))