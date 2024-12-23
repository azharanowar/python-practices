import os

current_dir = os.getcwd()
print(current_dir)

file_path = os.path.join('data_file','index.html')
print(file_path)
with open(file_path, 'r') as file:
    content = file.read()
    print(content)


# Second way using pathlib library

from pathlib import Path

file_path = Path('index.html')

with file_path.open('r') as file:
    content = file.read()
    print(content)

