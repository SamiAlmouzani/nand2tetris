//push-constant-i
//D=10
@10
D=A
//Ram[SP]=D
@SP
A=M
M=D
//SP++
@SP
M=M+1

//pop-local-i
//addr<-lcl+i
@0
D=A
@LCL
D=D+M
@R13//holdsaddr
M=D
//SP--
@SP
M=M-1
A=M
D=M
//Ram[addr]=Ram[SP]
@R13
A=M
M=D

//push-constant-i
//D=21
@21
D=A
//Ram[SP]=D
@SP
A=M
M=D
//SP++
@SP
M=M+1

//push-constant-i
//D=22
@22
D=A
//Ram[SP]=D
@SP
A=M
M=D
//SP++
@SP
M=M+1

//pop-argument-i
//addr<-arg+i
@2
D=A
@ARG
D=D+M
@R13//holdsaddr
M=D
//SP--
@SP
M=M-1
A=M
D=M
//Ram[addr]=Ram[SP]
@R13
A=M
M=D

//pop-argument-i
//addr<-arg+i
@1
D=A
@ARG
D=D+M
@R13//holdsaddr
M=D
//SP--
@SP
M=M-1
A=M
D=M
//Ram[addr]=Ram[SP]
@R13
A=M
M=D

//push-constant-i
//D=36
@36
D=A
//Ram[SP]=D
@SP
A=M
M=D
//SP++
@SP
M=M+1

//pop-this-i
//addr<-lcl+i
@6
D=A
@THIS
D=D+M
@R13//holdsaddr
M=D
//SP--
@SP
M=M-1
A=M
D=M
//Ram[addr]=Ram[SP]
@R13
A=M
M=D

//push-constant-i
//D=42
@42
D=A
//Ram[SP]=D
@SP
A=M
M=D
//SP++
@SP
M=M+1

//push-constant-i
//D=45
@45
D=A
//Ram[SP]=D
@SP
A=M
M=D
//SP++
@SP
M=M+1

//pop-that-i
//addr<-lcl+i
@5
D=A
@THAT
D=D+M
@R13//holdsaddr
M=D
//SP--
@SP
M=M-1
A=M
D=M
//Ram[addr]=Ram[SP]
@R13
A=M
M=D

//pop-that-i
//addr<-lcl+i
@2
D=A
@THAT
D=D+M
@R13//holdsaddr
M=D
//SP--
@SP
M=M-1
A=M
D=M
//Ram[addr]=Ram[SP]
@R13
A=M
M=D

//push-constant-i
//D=510
@510
D=A
//Ram[SP]=D
@SP
A=M
M=D
//SP++
@SP
M=M+1

//pop-temp-i
//addr<-lcl+i
@5
D=A
@6
D=D+A
@R13//holdsaddr
M=D
//SP--
@SP
M=M-1
A=M
D=M
//Ram[addr]=Ram[SP]
@R13
A=M
M=D

//push-local-i
//addr<-lcl+i
@0
D=A
@LCL
D=D+M
A=D
D=M
//Ram[SP]=Ram[addr]
@SP
A=M
M=D
//SP++
@SP
M=M+1

//push-that-i
//addr<-lcl+i
@5
D=A
@THAT
D=D+M
A=D
D=M
//Ram[SP]=Ram[addr]
@SP
A=M
M=D
//SP++
@SP
M=M+1

//add
@SP
M=M-1//SP--
@SP
A=M
D=M//D=Ram[SP]
@SP
M=M-1//SP--
@R13
M=D//Ram[13]=D
@SP
A=M
D=M//D=Ram[SP]
@R13
D=D+M//D=D+Ram[13]
@SP
A=M
M=D//Ram[SP]=D
@SP
M=M+1//SP++

//push-argument-i
//addr<-arg+i
@1
D=A
@ARG
D=D+M
A=D
D=M
//Ram[SP]=Ram[addr]
@SP
A=M
M=D
//SP++
@SP
M=M+1

//sub
@SP
M=M-1
@SP
A=M
D=M//D=Ram[SP]
@SP
M=M-1//SP--
@R13
M=D//Ram[13]=D
@SP
A=M
D=M//D=Ram[SP]
@R13
D=D-M//D=D-Ram[13]
@SP
A=M
M=D//Ram[SP]=D
@SP
M=M+1//SP++

//push-this-i
//addr<-lcl+i
@6
D=A
@THIS
D=D+M
A=D
D=M
//Ram[SP]=Ram[addr]
@SP
A=M
M=D
//SP++
@SP
M=M+1

//push-this-i
//addr<-lcl+i
@6
D=A
@THIS
D=D+M
A=D
D=M
//Ram[SP]=Ram[addr]
@SP
A=M
M=D
//SP++
@SP
M=M+1

//add
@SP
M=M-1//SP--
@SP
A=M
D=M//D=Ram[SP]
@SP
M=M-1//SP--
@R13
M=D//Ram[13]=D
@SP
A=M
D=M//D=Ram[SP]
@R13
D=D+M//D=D+Ram[13]
@SP
A=M
M=D//Ram[SP]=D
@SP
M=M+1//SP++

//sub
@SP
M=M-1
@SP
A=M
D=M//D=Ram[SP]
@SP
M=M-1//SP--
@R13
M=D//Ram[13]=D
@SP
A=M
D=M//D=Ram[SP]
@R13
D=D-M//D=D-Ram[13]
@SP
A=M
M=D//Ram[SP]=D
@SP
M=M+1//SP++

//push-temp-i
//addr<-lcl+i
@5
D=A
@6
A=D+A
D=M
//Ram[SP]=Ram[addr]
@SP
A=M
M=D
//SP++
@SP
M=M+1

//add
@SP
M=M-1//SP--
@SP
A=M
D=M//D=Ram[SP]
@SP
M=M-1//SP--
@R13
M=D//Ram[13]=D
@SP
A=M
D=M//D=Ram[SP]
@R13
D=D+M//D=D+Ram[13]
@SP
A=M
M=D//Ram[SP]=D
@SP
M=M+1//SP++

(END)
@END
0;JMP