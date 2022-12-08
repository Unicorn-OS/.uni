import lib

# Crucial: This all has to be Highly Encrypted! and use 'unikey' Biometrics to unlock & access

this = "key"
dirs = ["Bitwarden", "Kerberos", "LUKS", "OpenLDAP"]

dir_arr = lib.getDirs(this, dirs)

def makeDirs():
    lib.makeDirs(dir_arr)