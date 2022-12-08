import lib

this = "telepathy"
dirs = ["email", "facebook", "skype", "twitter", "whatsapp"]


dir_arr = lib.getDirs(this, dirs)

def makeDirs():
    lib.makeDirs(dir_arr)
