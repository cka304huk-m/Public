import datetime, os, zipfile

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
        d_month = now.month
        if d_month < 10:
            d_month = f'0{d_month}'
        data_string = f'{now.day}_{d_month}_{now.year}'

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

    def zip_file(self, exclude_files):
        """Архивация файлов"""

        # Название архива будет текущая дата/месяц/год
        filename = f'{self.get_data_now()}.zip'

        with zipfile.ZipFile(filename, 'w',
                             zipfile.ZIP_DEFLATED,
                             allowZip64=True) as newBackup:

            print()

            # Обход всего дерева директории.
            for folder, subfolders, files in os.walk(self.get_dir_files()):
                for sub in subfolders:
                    # Если папка есть в списки исключений.
                    if sub in exclude_files:
                        # Удалить папку из архивации.
                        subfolders.remove(sub)

                for file in files:
                    # Если файла нет в списке исключений.
                    if file not in exclude_files and file != filename:
                        print(f'Добавил в архив {filename} файл - {file}')
                        newBackup.write(os.path.join(folder, file),
                        os.path.relpath(os.path.join(folder, file),
                        self.get_dir_files()))

        # Возвращаю название файла.
        return filename