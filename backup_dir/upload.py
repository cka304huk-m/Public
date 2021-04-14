# Загрузка файлов на облачное хранилище.
from mega import Mega

def upload_file():

    # Создаю экзепляр.
    mega = Mega()

    email = 'ваша почта'
    password = 'ваш пароль'
    filename = input('название файла для загрузки: ')

    # Захожу на облачное хранилище под
    # своим аккаунтом.
    m = mega.login(email, password)

    # Загружаю файл на облачное хранилище.
    file = m.upload(filename)
    # Получаю ссылку на него.
    link = m.get_upload_link(file)
    print(f'Файл успешно загружен на Mega.NZ')
    print(f'Ccылка на него: {link}')

upload_file()