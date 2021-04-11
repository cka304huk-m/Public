# Бэкапер директории с возможностью
# исключать некоторые файлы.
from backup import Backup
import os, zipfile

def main():

    backup = input('Директория для резервного копирования: ')
    # Создаю экзепляр класса
    # которому передаю директорию с файлами.
    my_backup = Backup(backup)

    # Получаю список файлов
    my = my_backup.get_files_dir()

    # Вывожу список файлов и прошу указать
    # что исключить из резервной копии.
    ef = my_backup.set_exclude_files(my)

    my_backup.zip_file()

main()