import pathlib

def hardlinkTemplates():
    from = f"{this}/artifact/home/Templates"
    files = []
    cmd = f"ln {from}/{file} {pathlib.Path.home()}/Templates/"