import click
import os
from fastai.vision.all import *

@click.command()
@click.option('--filepath', default=str(os.getcwd())+"/dataset", help='Where to save the data.')

def download_data(filepath):
    """Download the Imagenette dataset to the provided path. Path must be absolute"""
    if os.path.exists(filepath):
        path = Path(filepath)
        untar_data(URLs.IMAGENETTE, data=path)
    else:
        print("Invalid path")
        exit()
    

if __name__ == '__main__':
    download_data()
