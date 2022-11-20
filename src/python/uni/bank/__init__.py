import lib

this = "bank"
dirs = ["coin", "parity", "bank"]


dir_arr = lib.getDirs(this, dirs)

def makeDirs():
    lib.makeDirs(dir_arr)