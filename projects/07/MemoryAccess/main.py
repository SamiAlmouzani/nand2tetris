import sys
from parse import CParser

if __name__ == '__main__':

    file_contents: str = ''    
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'rb') as f:
            file_contents: bytes = f.read()
    else:
        print(f"Usage python3 main.py [file.vm]")
        exit()

    parser: CParser = CParser(file_contents.decode(sys.getdefaultencoding()))
    parser.parse()