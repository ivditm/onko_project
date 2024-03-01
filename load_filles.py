import logging
import os


from dotenv import load_dotenv
import yadisk


from exceptions import TokenException


load_dotenv()


logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG)


TOKEN: str = os.getenv('token')
CLIENT_SECRET: str = os.getenv('client_secret')
CLIENT_ID: str = os.getenv('client_id')
DIR_TO: str = 'C:/Dev/onko_project/data/'
DIR_FROM: str = '/file_processor'

TOKEN_ERROR_MESSAGE: str = 'ошибка токена'


def create_connection(client_id: str,
                      client_secret: str,
                      token: str) -> yadisk.YaDisk:
    return yadisk.YaDisk(client_id, client_secret, token)


def get_directories(y: yadisk.YaDisk):
    root = y.get_meta("/")
    directories = [item.name
                   for item in root.embedded.items
                   if item.type == "dir"]
    return directories


def find_files_xlsx(disk: yadisk.YaDisk, dir) -> list[str]:
    return [item['path'] for item in disk.listdir(dir)
            if item['path'].endswith('.xlsx')]


def download_fills(load_path, files, disk):
    if not os.path.exists(load_path):
        os.mkdir(load_path)
    os.chdir(load_path)
    for file in files:
        disk.download(file.split(':')[1], file.split('/')[-1])


def main():
    disk = create_connection(CLIENT_ID, CLIENT_SECRET, TOKEN)
    if not disk.check_token():
        raise TokenException(TOKEN_ERROR_MESSAGE)
    print(len(find_files_xlsx(disk, '/file_processor')))
    if not os.path.isdir(DIR_TO) and not os.listdir(DIR_TO):
        download_fills(DIR_TO,
                       find_files_xlsx(disk, DIR_FROM),
                       disk)


if __name__ == '__main__':
    main()
