from code_writer import CodeWriter

class CParser:

    def __init__(self, file: str) -> None:
        self.file = file

    def parse(self):
        self.file = self.file.split('\r\n')

        code_writer = CodeWriter()
        for line in self.file:
            # ignores EOF, white space, and comments
            if len(line) == 0 or line[0] == ' ' or (line[0] == '/' and line[1] == '/'):
                continue

            line = line.strip().split(' ')
            cmd = line[0]
            if cmd == 'push' or cmd == 'pop':
                arg1: str = line[1]
                arg2: str = line[2]
                code_writer.write_push_pop(cmd, arg1, arg2)
                print(f"cmd: {cmd}, arg1: {arg1}, arg2: {arg2}.")
            else:
                code_writer.write_arithmetic(cmd)
                print(line[0])

        code_writer.close()
