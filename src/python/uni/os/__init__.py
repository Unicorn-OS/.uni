import lib

this = "os"
dirs = ["dl", "iso", "torr"]


dir_arr = lib.getDirs(this, dirs)

def makeDirs():
    lib.makeDirs(dir_arr)