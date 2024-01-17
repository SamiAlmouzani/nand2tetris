
class CodeWriter:
    def __init__(self, filename: str) -> None:
        self.file = open(f"{filename.split('.')[0]}.asm", 'w', encoding='UTF-8')
    
    def write_arithmetic(self, cmd: str) -> None:
        if cmd == 'add':
            self.file.write(f"""//add
                            @SP
                            M = M - 1 // SP--
                            @SP
                            A = M
                            D = M // D = Ram[SP]  
                            @SP
                            M = M - 1 // SP--
                            @R13
                            M = D // Ram[13] = D
                            @SP
                            A = M
                            D = M // D = Ram[SP]
                            @R13
                            D = D + M // D = D + Ram[13]
                            @SP
                            A = M
                            M = D // Ram[SP] = D
                            @SP
                            M = M + 1 // SP++\n\n""".replace(" ", ""))
        if cmd == 'sub':
            self.file.write(f"""//sub
                            @SP
                            M = M - 1               
                            @SP
                            A = M
                            D = M // D = Ram[SP]  
                            @SP
                            M = M - 1 // SP--
                            @R13
                            M = D // Ram[13] = D
                            @SP
                            A = M
                            D = M // D = Ram[SP]
                            @R13
                            D = D - M // D = D - Ram[13]
                            @SP
                            A = M
                            M = D // Ram[SP] = D
                            @SP
                            M = M + 1 // SP++\n\n""".replace(" ", ""))
        pass 

    def write_push_pop(self, cmd: str, segment: str, index: int) -> None:
        
        if cmd == 'push' and segment == 'constant':
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
        elif cmd == 'push' and segment == 'local':
            seg = 'LCL'
            self.file.write(f"""// push-local-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @{seg}
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
    
        elif cmd == 'pop' and segment == 'local':
            seg = 'LCL'
            self.file.write(f"""// pop-local-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @{seg}
                            D = D + M
                            @R13 // holds addr
                            M = D
                            // SP--
                            @SP
                            M = M - 1
                            A = M 
                            D = M
                            // Ram[addr] = Ram[SP]
                            @R13
                            A = M
                            M = D\n\n""".replace(" ", ""))
        elif cmd == 'push' and segment == 'argument':
            seg = 'ARG'
            self.file.write(f"""// push-argument-i
                            // addr <- arg + i
                            @{index}
                            D = A
                            @{seg}
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
    
        elif cmd == 'pop' and segment == 'argument':
            seg = 'ARG'
            self.file.write(f"""// pop-argument-i
                            // addr <- arg + i
                            @{index}
                            D = A
                            @{seg}
                            D = D + M
                            @R13 // holds addr
                            M = D
                            // SP--
                            @SP
                            M = M - 1
                            A = M 
                            D = M
                            // Ram[addr] = Ram[SP]
                            @R13
                            A = M
                            M = D\n\n""".replace(" ", ""))
        elif cmd == 'push' and segment == 'this':
            seg = 'THIS'
            self.file.write(f"""// push-this-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @{seg}
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
    
        elif cmd == 'pop' and segment == 'this':
            seg = 'THIS'
            self.file.write(f"""// pop-this-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @{seg}
                            D = D + M
                            @R13 // holds addr
                            M = D
                            // SP--
                            @SP
                            M = M - 1
                            A = M
                            D = M
                            // Ram[addr] = Ram[SP]
                            @R13
                            A = M
                            M = D\n\n""".replace(" ", ""))
 
        elif cmd == 'push' and segment == 'that':
            seg = 'THAT'
            self.file.write(f"""// push-that-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @{seg}
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
    
        elif cmd == 'pop' and segment == 'that':
            seg = 'THAT'
            self.file.write(f"""// pop-that-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @{seg}
                            D = D + M
                            @R13 // holds addr
                            M = D
                            // SP--
                            @SP
                            M = M - 1
                            A = M
                            D = M
                            // Ram[addr] = Ram[SP]
                            @R13
                            A = M
                            M = D\n\n""".replace(" ", ""))
        elif cmd == 'push' and segment == 'static':
            self.file.write(f"""// push-static-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @Foo.{index}
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
    
        elif cmd == 'pop' and segment == 'static':
            self.file.write(f"""// pop-static-i
                            // addr <- lcl + i
                            @{index}
                            D = A
                            @Foo.{index}
                            D = D + M
                            @R13 // holds addr
                            M = D
                            // SP--
                            @SP
                            M = M - 1
                            A = M
                            D = M
                            // Ram[addr] = Ram[SP]
                            @R13
                            A = M
                            M = D\n\n""".replace(" ", ""))

        elif cmd == 'push' and segment == 'temp':
            self.file.write(f"""// push-temp-i
                            // addr <- lcl + i
                            @5
                            D = A
                            @{index}
                            A = D + A
                            D = M
                            // Ram[SP] = Ram[addr]
                            @SP
                            A = M
                            M = D
                            // SP++
                            @SP
                            M = M + 1\n\n""".replace(" ", ""))
        elif cmd == 'pop' and segment == 'temp':
            self.file.write(f"""// pop-temp-i
                            // addr <- lcl + i
                            @5
                            D = A
                            @{index}
                            D = D + A
                            @R13 // holds addr
                            M = D
                            // SP--
                            @SP
                            M = M - 1
                            A = M
                            D = M
                            // Ram[addr] = Ram[SP]
                            @R13
                            A = M
                            M = D\n\n""".replace(" ", ""))
        elif cmd == 'push' and segment == 'pointer' and index == "0":
            seg = 'THIS'
            self.file.write(f"""
                            //push-pointer-0
                            @{seg}
                            D = M
                            @SP
                            A = M
                            M = D//*SP=THIS
                            @SP
                            M = M + 1//SP++\n\n""".replace(" ", ""))
    
        elif cmd == 'pop' and segment == 'pointer' and index == "0":
            seg = 'THIS'
            self.file.write(f"""
                            //pop-pointer-0
                            @SP
                            M = M - 1
                            A = M
                            D = M
                            @{seg}
                            M = D\n\n""".replace(" ", ""))


        elif cmd == 'push' and segment == 'pointer' and index == "1":
            seg = 'THAT'
            self.file.write(f"""
                            //push-pointer-1
                            @{seg}
                            D = M
                            @SP
                            A = M
                            M = D//*SP=THAT
                            @SP
                            M = M + 1//SP++\n\n""".replace(" ", ""))

        elif cmd == 'pop' and segment == 'pointer' and index == "1":
            seg = 'THAT'
            self.file.write(f"""
                            //pop-pointer-1
                            @SP
                            M = M - 1
                            A = M 
                            D = M
                            @{seg}
                            M = D\n\n""".replace(" ", ""))

    def close(self) -> None:
        self.file.write(f"""(END)
                            @END
                            0;JMP""".replace(" ", ""))
        self.file.close()