from PIL import Image
import pytesseract

img_file_name = 'example_file.png'

print(pytesseract.image_to_string(Image.open(img_file_name)))