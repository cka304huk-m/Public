from settings import *

numberDocument, data_document, inn, comment, sheet = create_document()

def main_sanstar():
    one_string = f'{numberDocument};{data_document};;;{inn};;;;;;;;;;;{comment};'

    with open('sanstar.txt', 'w') as new_file:
        new_file.write(one_string + '\n')
        for row in range(11, sheet.max_row + 1):
            try:
                if sheet[row][1].value != None:
                        new_string = f';{sheet[row][1].value};;;;;;{sheet[row][6].value};;;{sheet[row][8].value};'
                        new_file.write(new_string + '\n')
            except:
                pass

if __name__ == '__main__':
    main_sanstar()