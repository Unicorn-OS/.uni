import os
import pathlib


def getDirs(this, dirs):
    this_dirs = []
    for dir in dirs:
        this_dirs.append(f"{this}/{dir}")
    return this_dirs


def makeDirs(dirs_array):
    home = pathlib.Path.home()
    for dir in dirs_array:
        os.makedirs(f"{home}/.uni/{dir}", exist_ok=True)
