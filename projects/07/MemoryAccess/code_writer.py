
class CodeWriter:

    def __init__(self) -> None:
        self.file = open('BasicTest.asm', 'w', encoding='UTF-8')
    

    def write_arithmetic(self, cmd: str) -> None:
        pass 

    def write_push_pop(self, cmd: str, segment: str, index: int) -> None:
        if cmd == 'C_PUSH' and segment == 'constant':
            self.file.write(f"// D = {index}\n@{index}\nD=A\n// Ram[SP] = D\n@SP\nA=M\nM=D\n// SP++\n@SP\nM=M+1\n\n")

    def close(self) -> None:
        self.file.close()