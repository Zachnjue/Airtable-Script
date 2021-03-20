# Finding the path to the apps on MacOS
from pathlib import Path
import os
p = Path('/Applications')
x = list(p.glob('*'))
with open('listofApps.txt', 'w'):
