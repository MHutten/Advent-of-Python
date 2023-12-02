import os

def read_input(relative_path: str):
    try:
        filename: str = os.path.join(os.path.dirname(__file__), relative_path)
        return open(filename, 'r').read()
    except:
        pass