import openpyxl
from converter import *

def create_document():
    upd = openpyxl.open('upd.xlsx')

    sheet = upd.active

    numDataDoc = sheet['B7'].value
    numberDocument = numDataDoc.split()[3]
    dayDocument = numDataDoc.split()[5]
    if len(dayDocument) == 1:
        dayDocument = f'0{dayDocument}'
    monthDocument = numDataDoc.split()[6]
    yearDocument = numDataDoc.split()[7]
    data_document = ''
    if monthDocument == 'Января':
        data_document = f'{dayDocument}.01.{yearDocument}'
    elif monthDocument == 'Февраля':
        data_document = f'{dayDocument}.02.{yearDocument}'
    elif monthDocument == 'Марта':
        data_document = f'{dayDocument}.03.{yearDocument}'
    elif monthDocument == 'Апреля':
        data_document = f'{dayDocument}.04.{yearDocument}'
    elif monthDocument == 'Мая':
        data_document = f'{dayDocument}.05.{yearDocument}'
    elif monthDocument == 'Июня':
        data_document = f'{dayDocument}.06.{yearDocument}'
    elif monthDocument == 'Июля':
        data_document = f'{dayDocument}.07.{yearDocument}'
    elif monthDocument == 'Августа':
        data_document = f'{dayDocument}.08.{yearDocument}'
    elif monthDocument == 'Сентября':
        data_document = f'{dayDocument}.09.{yearDocument}'
    elif monthDocument == 'Октября':
        data_document = f'{dayDocument}.10.{yearDocument}'
    elif monthDocument == 'Ноября':
        data_document = f'{dayDocument}.11.{yearDocument}'
    elif monthDocument == 'Декабря':
        data_document = f'{dayDocument}.12.{yearDocument}'

    inn = 910605851840  # ИНН
    comment = ' (•◡•) /'

    return numberDocument, data_document, inn, comment, sheet


try:
    create_document()
except:
    converter()
    create_document()