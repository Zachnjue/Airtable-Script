# Finding the path to the apps on MacOS
from pathlib import Path
import os

pathofFile = Path('/Applications')
generatedList = list(pathofFile.glob('*'))
#emptyList = []
for item in generatedList:
    print(item.name)
    # emptyList.append(item)
# print(emptyList[1])
# sortList


'''with open('listofApps.txt', 'w') as fileobject:
    fileobject.write(str(x))
    fileobject.close()
'''
