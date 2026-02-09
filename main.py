from PIL import Image
from pytesseract import image_to_string as ocr
from pdf2image import convert_from_path
from os import remove as remove_file


img_file_name = 'receipt.pdf'


def get_receipt(img_file_name):
    
    if '.pdf' in img_file_name.lower():
        
        receipt = ''

        # Source - https://stackoverflow.com/a/48583124
        # Posted by Keval Dave, modified by community. See post 'Timeline' for change history
        # Retrieved 2026-02-08, License - CC BY-SA 4.0
        
        pages = convert_from_path(img_file_name, 500)
        
        for count, page in enumerate(pages):
            page.save(f'out{count}.jpg', 'JPEG')
            receipt += ocr(Image.open(f'out{count}.jpg'))
            remove_file(f'out{count}.jpg')

    else:
        receipt = ocr(Image.open(img_file_name))

    return receipt


def main():
    
    receipt = get_receipt(img_file_name)
    
    print(receipt)

main()