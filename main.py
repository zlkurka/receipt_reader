from PIL import Image
from pytesseract import image_to_string
from pdf2image import convert_from_path
from os import remove
from menu import menu
from enums import Store
from string import ascii_letters


### V ### Changes allowed here!! ### V ###

img_file_name = 'receipt.pdf'

### ^ ### Changes allowed here!! ### ^ ###


def get_receipt(img_file_name):
    
    if '.pdf' in img_file_name.lower():
        
        receipt = ''

        # Source - https://stackoverflow.com/a/48583124
        # Posted by Keval Dave, modified by community. See post 'Timeline' for change history
        # Retrieved 2026-02-08, License - CC BY-SA 4.0
        
        pages = convert_from_path(img_file_name, 500)
        
        for count, page in enumerate(pages):
            page.save(f'out{count}.jpg', 'JPEG')
            receipt += image_to_string(Image.open(f'out{count}.jpg'))
            remove(f'out{count}.jpg')
        
        receipt = receipt.split('\n')

    else:
        receipt = image_to_string(Image.open(img_file_name)).split('\n')
    
    for line in receipt:
        if line == '':
            receipt.remove('')

    return receipt


def parse_receipt(receipt, store):
    match store:
        
        case Store.aldi:
            pass
        
        case Store.meijer:
            for line in receipt:
                
                if 'meijer.com' in line:
                    date_line = receipt[receipt.index(line) + 1].strip(ascii_letters).split('/')
                    date = {
                        'month': date_line[0],
                        'day': date_line[1],
                        'year': date_line[2],
                    }

        case Store.hpp:
            pass

    return date, # purchases, total, tax


def main():
    
    receipt = get_receipt(img_file_name)
    
    store_options = []
    for s in Store:
        store_options.append(s)

    print(receipt)

    store = menu(store_options, 'Where did you shop?')

    receipt_parsed = parse_receipt(receipt, store)

main()