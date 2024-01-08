// while (true)
//   if (KBD != 0)
//     for(i=Screen; i < Screen + 8191; i++)
//       Ram[addr] = -1
//   else // color white
//     for(i=Screen; i < Screen + 8191; i++)
//       Ram[addr] = 0

@8191
D=A
@max
M=D

(INFINITE)
    @i
    M=0 // i = 0
    
    @KBD
    D=M // D = Ram[KBD] 
    @BLACK
    D;JGT // Ram[KBD] > 0 GOTO BLACK
    @WHITE
    D;JEQ // Ram[KBD] == 0 GOTO WHITE
    
    @INFINITE
    0;JMP

(BLACK)
    @max
    D=M
    @i
    D=D-M
    @INFINITE
    D;JEQ // if (max - i) = 0
    
    @i
    D=M 
    @SCREEN
    A=D+A
    M=-1 // sets Ram[i] = -1 
    
    @i
    M=M+1 // i++
    
    @BLACK
    0;JMP
 
 (WHITE)
    @max
    D=M
    @i
    D=D-M
    @INFINITE
    D;JEQ // if (max - i) = 0
    
    @i
    D=M 
    @SCREEN
    A=D+A
    M=0 // sets Ram[i] = -1 
    
    @i
    M=M+1 // i++
   
    @WHITE
    0;JMP
    


     

     

    
    