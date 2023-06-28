from xls2xlsx import XLS2XLSX
import os.path

def converter():
    cur_dir = os.getcwd()   # Текущий каталог.
    file_list = os.listdir(cur_dir) # Список файлов в текущем каталоге.
    for file in file_list:
        if file.endswith('xls'):
            x2x = XLS2XLSX(file)
            x2x.to_xlsx('upd.xlsx')