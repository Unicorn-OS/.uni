import lib

this = ".uni"
dirs = ["app", "cloud", "hyperion", "key", "os", "platform", "bank", ".temp"]

dir_arr = lib.getDirs(this, dirs)

def makeDirs():
    lib.makeDirs(dir_arr)