from pathlib import Path
from zipfile import ZipFile

# with ZipFile("files.zip", "w") as zip: # create zip file
#     for path in Path("ecommerce").rglob("*.*"): # finds all files, returns generator
#         zip.write(path)

with ZipFile("files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    zip.extractall("extract")
