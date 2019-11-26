from os import listdir
from os import path
from os import getcwd




def ls():
    return listdir(pwd())


def isdir(dirpath):
    return path.isdir(dirpath)

def isfile(filepath):
    return path.isfile(filepath)


def pwd():
    return getcwd()


def mkdir(dir):
    pass


