
class CodeWriter:
    def __init__(self) -> None:
        self.file = open('BasicTest.asm', 'w', encoding='UTF-8')
    

    def write_arithmetic(self, cmd: str) -> None:
        pass 

    def write_push_pop(self, cmd: str, segment: str, index: int) -> None:

        if cmd == 'C_PUSH' and segment == 'constant':
            self.file.write(f"""//push-constant-i
                            // D = {index}
                            @{index}
                            D=A
                            // Ram[SP] = D
                            @SP
                            A=M
                            M=D
                            // SP++
                            @SP
                            M=M+1\n\n""".replace(" ", ""))
        elif cmd == 'C_POP' and segment == 'local':
            self.file.write(f"""// pop-local-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @LCL
                            D = D + M
                            @R13 // holds addr
                            M = D
                            // SP--
                            @SP
                            M = M - 1
                            D = M
                            // Ram[addr] = Ram[SP]
                            @R13
                            A = M
                            M = D\n\n""".replace(" ", ""))
        elif cmd == 'C_PUSH' and segment == 'local':
            self.file.write(f"""// push-local-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @LCL
                            D = D + M
                            A = D
                            D = M
                            // Ram[SP] = Ram[addr]
                            @SP
                            A = M
                            M = D
                            // SP++
                            @SP
                            M = M + 1\n\n""".replace(" ", ""))
    def close(self) -> None:
        self.file.close()