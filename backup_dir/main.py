# Резервная копия файлов в заданом каталоге.

from backup import Backup

def main():

    backup = input('Директория для резервного копирования: ')
    # Создаю экзепляр класса
    # которому передаю директорию с файлами.
    my_backup = Backup(backup)

    # Получаю список файлов
    my = my_backup.get_files_dir()

    # Вывожу список файлов и прошу указать
    # что исключить из резервной копии.
    #ef = my_backup.set_exclude_files(my)

    my_backup.zip_file()

main()
