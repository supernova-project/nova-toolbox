from os import listdir
from os import path
from os import getcwd




def pwd():
    return getcwd()

def isdir(dirpath):
    return path.isdir(dirpath)

def isfile(filepath):
    return path.isfile(filepath)

def ls():
    return listdir(pwd())


def mkdir(dir):
    pass


