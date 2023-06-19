import os

absolute_path = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(absolute_path, 'files', 'text.txt')

try:
    file_obj = open(file_path)
    print('File found')

except FileNotFoundError:
    print('File not found')
