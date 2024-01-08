
@i 
M=1 // i = 1

@R2
M=0 // Ram[2] = 0

(LOOP)
    @i
    D=M
    @R1
    D=D-M
    @END
    D;JGT // if (i > RAM[1]) GOTO @END 

    @R0
    D=M
    @R2
    M=D+M // sum = sum + val
    
    @i
    M=M+1 // i++
    @LOOP
    0;JMP // GOTO @LOOP

(END)
    @END
    0;JMP




