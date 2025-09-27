def read(file_path):
    
    with open(file_path, 'r') as file:

        return file.read()
    
    
def read_lines(file_path):
    
    with open(file_path, 'r') as file:
        
        return file.readlines()