import openpyxl
from find_codeTdm import find_tdmCode
from months import edit_month
from converter import converter

def create_document():
    try:
        converter()
    except:
        pass

    upd = openpyxl.open('upd.xlsx')
    sheet = upd.active

    numberDocument = sheet['B17'].value[17:24].strip()  # номер документа
    data = sheet['B17'].value[27:].split()  # Дата
    if len(data[0])>1:
        day = data[0]   # День
    else:
        day = f'0{data[0]}'  # День
    month = edit_month(data[1]) # Месяц
    year = data[2]  # Год
    data_document = f'{day}/{month}/{year}'

    inn = '9201002117'
    comment = '=)'

    one_string = f'{numberDocument};{data_document};;;{inn};;;;;;;;;;;{comment};'
    with open('tdm.txt', 'w') as new_file:
        new_file.write(one_string + '\n')
        for row in range(25, sheet.max_row + 1):
            if sheet[row][3].value != None:
                if 'SQ' in sheet[row][3].value[:2]:
                    new_code = find_tdmCode(sheet[row][3].value)
                    new_string = f';{new_code};;;;;;{sheet[row][50].value};;;{sheet[row][60].value};'
                    new_file.write(new_string + '\n')
                else:
                    new_string = f';{sheet[row][3].value};;;;;;{sheet[row][50].value};;;{sheet[row][60].value};'
                    new_file.write(new_string + '\n')

create_document()