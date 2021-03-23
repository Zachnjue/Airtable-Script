# Finding the path to the apps on MacOS
from pathlib import Path
import os

# Path containing the apps on the Mac
pathofFile = Path('/Applications')
generatedList = list(pathofFile.glob('*.app'))

# Create an empty list where the apps will be stored
emptyList = []
for item in generatedList:
    emptyList.append(item.name)

with open('listofApps.txt', 'w') as fileobject:
    fileobject.write(str(emptyList))
    fileobject.close()
