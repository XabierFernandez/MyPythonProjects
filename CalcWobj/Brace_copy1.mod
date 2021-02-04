%%%
  VERSION:1
  LANGUAGE:ENGLISH
%%%

MODULE Brace
    !
    ! ------------------------------------------------------
    !                                                      !
    ! Implent    : ARM ROBOTICS                            ! 
    !            : PS. Dolores Ibarruri 80 PB 02           ! 
    !            : E48902 Baracaldo - Vizcaya              ! 
    ! Integrator : INGEMAT - Parque Tecn Zamudio - Vizcaya !        
    ! Aplication : Arc Welding Cell -                      !                    
    ! Modul Task : Piece :  Brace (Limo & Combi) Robot 6(6)!
    ! Dessing    : arm robotics (jarp / jcp)               !
    ! Cliente    : GESTAMP Haynrode                        !
    ! Fecha      : Juny - 2017                             !                   
    ! ------------------------------------------------------
    !
    ! Layout
    PERS wobjdata obOP50_RH:=[FALSE,TRUE,"",[[-1461.79,4234.74,1082.31],[-0.5904,0.590429,-0.389119,0.389113]],[[0.0,0.0,0.0],[1,0,0,0]]];
    PERS wobjdata obOP50_LH:=[FALSE,TRUE,"",[[-1428.93,-4116.31,1102.54],[0.588893,0.588866,0.391443,0.391426]],[[0.0,0.0,0.0],[1,0,0,0]]];
    !
    PERS wobjdata obOP50_XF:=[FALSE,TRUE,"",[[0,-4116.31,1102.54],[0.588893,0.588866,0.391443,0.391426]],[[0.0,0.0,0.0],[1,0,0,0]]];
    
    !

    PROC SchweissenOp50_Limo_LH()
        !------------------------------------!
        !    Weld Piece LH Limo in OP50      !
        !               Brace                !
        !               R6(6)                !
        !------------------------------------!
        !
        !
        MoveJ [[3917.65,-373.948,-551.218],[0.022427,0.489361,0.650621,-0.580272],[-1,0,-1,0],[9E+009,9E+009,9E+009,9E+009,9E+009,9E+009]],vmax,z200,tGun\WObj:=obOP50_XF;
        MoveL [[3905.27,-583.948,-497.998],[0.0366288,-0.561518,-0.669798,0.484487],[-1,-1,-1,0],[9E+009,9E+009,9E+009,9E+009,9E+009,9E+009]],v1000,z10,tGun\WObj:=obOP50_XF;
        !
    ENDPROC

    PROC SchweissenOp50_Limo_RH()
        !------------------------------------!
        !    Weld Piece RH Limo in OP50      !
        !               Brace                !
        !               R6(6)                !
        !------------------------------------!
        !
        !
        MoveJ [[4622.17,139.87,698.36],[0.0175883,-0.507824,0.431548,0.745367],[0,0,0,0],[9E+009,9E+009,9E+009,9E+009,9E+009,9E+009]],vmax,z200,tGun\WObj:=obOP50_RH;
        MoveJ [[4512.94,447.19,811.25],[0.0640989,0.600705,-0.542576,-0.583658],[0,0,0,0],[9E+009,9E+009,9E+009,9E+009,9E+009,9E+009]],vmax,z200,tGun\WObj:=obOP50_RH;
        !
    ENDPROC

ENDMODULE