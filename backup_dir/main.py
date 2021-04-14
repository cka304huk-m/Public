# Бэкапер директории с возможностью
# исключать некоторые файлы.
from backup import Backup
import upload

def main():

    backup = input('Директория для резервного копирования: ')
    # Создаю экзепляр класса
    # которому передаю директорию с файлами.
    my_backup = Backup(backup)

    # Получаю список файлов
    my = my_backup.get_files_dir()

    # Вывожу список файлов и прошу указать
    # что исключить из резервной копии.
    exclude_files = my_backup.set_exclude_files(my)

    # Создаю ахив и выкидываю из него файлы которые
    # присутсвуют в исключениях.
    namef = my_backup.zip_file(exclude_files)

    print()
    up_f = input('Загрузить файл? ДА/НЕТ ')
    if up_f.lower() == 'да':
        # Загрузка файла на Mega.NZ
        upload.upload_file(namef)
    else:
        print('Вы пропустили загрузку файла.')

main()
