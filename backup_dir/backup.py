import os, datetime, os, zipfile

# Класс 'Резервное копирование'.
class Backup:

    # Атрибуты класса.
    def __init__(self, dir_f):
        self.__dir_f = dir_f
    
    # Методы-получатели.
    def get_dir_files(self):
        # Возращаю директорию.
        return self.__dir_f

    def get_files_dir(self):
        # Список файлов в директории.
        if os.path.isdir(self.__dir_f):
            return os.listdir(self.__dir_f)
        else:
            print('Нет такого каталога.')

    def get_data_now(self):
        now = datetime.datetime.now()
        data_string = f'{now.day}_{now.month}_{now.year}'

        return data_string

    # Методы-модификаторы.
    def set_exclude_files(self, files):

        # Исключения файлов из копии
        # и возращение модифицированого списка.
        print('Список файлов:')
        for f in files:
            print(f)

        print()
        mod_files = input('Что исключить из копии(через пробел): ')
        mod_files = mod_files.split()
        for mf in mod_files:
            print(f'Исключил из копии файлов: {mf}')

        return mod_files

    def zip_file(self, mod_files):
        """Архивация файлов"""

        # Название архива будет текущая дата/месяц/год
        filename = f'{self.get_data_now()}.zip'

        with zipfile.ZipFile(filename, 'w',
                             zipfile.ZIP_DEFLATED,
                             allowZip64=True) as newBackup:

            # Переменая для сохранения имени каталога.
            archDirName = ''

            # Обход всего дерева директории и сжатие файлов в каждой папке
            for dir_, subdirs, files in os.walk(self.__dir_f):
                if dir_ not in mod_files:
                    print(f'Добавление файлов из директории {dir_}...')
                    # Имя текущей директории в архиве
                    archDirName = '/'.join([archDirName, os.path.basename(dir_)]).strip('/')
                    # Добавить в архив текущую директорию
                    newBackup.write(dir_, archDirName)

                # Добавить в архив файлы из текущей директории
                for file in files:
                    # Проверяю файлы с модифицированым списком.
                    # Если файла нет в списке, он добавляется в архив.
                    if file not in mod_files:
                        # Имя текущего файла в архиве
                        archFileName = archDirName + '/' + file
                        newBackup.write(os.path.join(dir_, file), archFileName)