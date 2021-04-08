# Finding the path to the apps on MacOS
from pathlib import Path
import os
from os import error
from plistlib import load
import requests
from dotenv import load_dotenv
load_dotenv(".env")

# API request code
AIRTABLE_BASE_ID = os.environ.get('AIRTABLE_BASE_ID')
AIRTABLE_TABLE_NAME = os.environ.get('AIRTABLE_TABLE_NAME')
AIRTABLE_API_KEY = os.environ.get('AIRTABLE_API_KEY')
endpoint = f'{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}'

# Path containing the apps on the Mac
pathofFile = Path('/Applications')
generatedList = list(pathofFile.glob('*.app'))

# Create an empty list where the apps will be stored
emptyList = []
for item in generatedList:
    emptyList.append(item.name)
    # Path where .plist is stored
    filename = f'/Applications/{item.name}/Contents/Info.plist'
    # Reads the file .plist
    try:
        with open(filename, 'rb') as fp:
            p1 = load(fp)
            print(p1["CFBundleIdentifier"])
    except FileNotFoundError:
        print(f"This file {item.name} has FileNotFoundError")
        continue
    except PermissionError:
        print(f"This file {item.name} has PermissionError")
