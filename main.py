from PIL import Image
from pytesseract import image_to_string as ocr

img_file_name = 'receipt.png'

print(ocr(Image.open(img_file_name)))