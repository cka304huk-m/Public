# Загрузка файлов на облачное хранилище.
from mega import Mega

def upload_file(namef):

    # Создаю экзепляр.
    mega = Mega()

    email = 'электронная почта'
    password = 'пароль'

    # Название файла.
    filename = namef
    folder = input('папка назначения: ')

    # Захожу на облачное хранилище под
    # своим аккаунтом.
    m = mega.login(email, password)

    # Загружаю файл на облачное хранилище.
    if folder:
        up_folder = m.find(folder)
        file = m.upload(filename, up_folder[0])
        # Получаю ссылку на него.
        link = m.get_upload_link(file)
    else:
        file = m.upload(filename)
        # Получаю ссылку на него.
        link = m.get_upload_link(file)
    print(f'Файл {namef} успешно загружен на Mega.NZ')
    print(f'Ccылка на него: {link}')
