""" First mode
class File:
    def __init__(self, file, mode):
        print('Opening file')
        self.file = open(file, mode)

    def __enter__(self):
        print('Returning the file')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Closing the file')
        self.file.close()


with File('abc.txt', 'w') as file:
    file.write('Hello Friend')
"""

#   Second Mode
from contextlib import contextmanager


@contextmanager
def open_file(file, mode):
    try:
        print("Opening the file")
        file = open(file, mode)
        yield file
    finally:
        print("Closing the file")
        file.close()


with open_file('abc.txt', 'w') as file:
    file.write('123')
    file.write('123')
    file.write('123')
