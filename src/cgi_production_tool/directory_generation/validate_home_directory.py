import os
from os import path
from os.path import expanduser
from pathlib import Path


## Dynamically check the home directory on various operating systems..
def validateParentDirectory():
    
    homeDir = Path(input("Production Name: "))
    validDir = homeDir.resolve(strict=False)
    return validDir

valid = validateParentDirectory()
print(valid)

def makeParentDirectory(valid):

    ProductionName = os.mkdir(valid)
    
