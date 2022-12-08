import lib

dirs = ["bitwarden", "kerberos", "luks"]


def getDirs():
    key_dirs = []
    for dir in dirs:
        key_dirs.append(f"key/{dir}")
    return key_dirs

def makeDirs():
    lib.makeDirs(getDirs())