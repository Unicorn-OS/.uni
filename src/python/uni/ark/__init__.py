import lib

this = "ark"
dirs = ["bitwarden", "kerberos", "luks"]


dir_arr = lib.getDirs(this, dirs)

def makeDirs():
    lib.makeDirs(dir_arr)