import os


def get_path_folder_pics(name_folder_pics):
    path_project = os.getcwd()
    return os.path.join(path_project, name_folder_pics)


def getImage(path_folder_pics):
    path = get_path_folder_pics(path_folder_pics)
    images = []
    extensions = ('.jpg', '.png', '.jpeg', '.png', '.gif')
    for file in os.listdir(path):
        if file.endswith(extensions):
            images.append(os.path.join(path, file))
    else:
        return images


if __name__ == "__main__":
    print(getImage("foto"))
