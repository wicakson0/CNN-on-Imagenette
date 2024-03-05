import click
import os
from fastai.vision.all import *

@click.command()
@click.option('--path', default=str(os.getcwd()), help='Where to save the data.')

def download_data(path):
    """Download the Imagenette dataset to the provided path."""
    os.chdir(path)
    imagenette_path = untar_data(URLs.IMAGENETTE_320)
    return imagenette_path

if __name__ == '__main__':
    download_data()
