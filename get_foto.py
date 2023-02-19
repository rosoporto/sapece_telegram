from modules.download import download



def main():
    foto_path = 'foto'
    foto_name = 'hubble.jpeg'
    url_foto = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    download(url_foto, dest_folder=foto_path)


if __name__ == '__main__':
    main()