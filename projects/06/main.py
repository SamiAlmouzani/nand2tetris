import sys
from parse import Parse 

file = ''
if __name__ == "__main__":
    if len(sys.argv) == 2:
        with open('add/Add.asm') as f:
            file = f.read()         
        
    else:
        print('Usage python3 main.py [file.asm]')