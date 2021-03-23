# Finding the path to the apps on MacOS
from pathlib import Path
import os

pathofFile = Path('/Applications')
generatedList = list(pathofFile.glob('*.app'))

emptyList = []
for item in generatedList:
    emptyList.append(item)
    print(item.name)

with open('listofApps.txt', 'w') as fileobject:
    fileobject.write(str(item))
    fileobject.close()
