from pytesseract import pytesseract
from PIL import Image



path_to_tesseract = r'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
path_to_image = "../newpy.jpg"

pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(path_to_image)

text = pytesseract.image_to_string(img)