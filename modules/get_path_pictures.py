import os
import argparse


def get_path_pictures(folder_with_pics):
    '''
    Функция получает пути до картинок. folder_with_pics - имя папки с картинкаим
    '''
    work_folder = os.path.abspath(os.getcwd())
    folder_pics = os.path.join(work_folder, folder_with_pics)
    pictures = os.listdir(folder_pics)
    pics_with_path = []
    for picture in pictures:
        pic_with_path = os.path.join(folder_pics, picture)
        pics_with_path.append(pic_with_path)
    return pics_with_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Полусает пути до картинки в папке')
    parser.add_argument("FL", help="Имя папки c картинками")
    args = parser.parse_args()
    print(get_path_pictures(args.FL))