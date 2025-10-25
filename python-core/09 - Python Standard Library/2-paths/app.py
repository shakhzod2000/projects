from pathlib import Path

# 'r' is for raw string
Path(r"C:\Program Files\Microsoft")
Path() # curr folder
Path("ecommerce/__init__.py")
Path() / ".." / "5-zip" / "ecommerce" / "__init__.py"
Path.home()

path = Path("../5-zip/ecommerce/__init__.py")
path.exists()
path.is_file()
path.is_dir()
print(f'name: {path.name}')
print(f'stem: {path.stem}')
print(f'suffix: {path.suffix}')
print(f'parent: {path.parent}')
path = path.with_suffix(".txt") # not renaming
print(path)
