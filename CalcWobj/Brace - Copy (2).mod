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
    !

    PROC SchweissenOp50_Limo_LH()
        !------------------------------------!
        !    Weld Piece LH Limo in OP50      !
        !               Brace                !
        !               R6(6)                !
        !------------------------------------!
        !
        !
        MoveJ [[5132.84,353.95,485.313],[0.342939,-0.590122,0.677197,0.27487],[-1,0,-1,0],[9E+009,9E+009,9E+009,9E+009,9E+009,9E+009]],vmax,z200,tGun\WObj:=obOP50_RH;
        MoveL [[5179.73,563.949,513.381],[0.226574,-0.63085,0.706192,0.228004],[-1,-1,-1,0],[9E+009,9E+009,9E+009,9E+009,9E+009,9E+009]],v1000,z10,tGun\WObj:=obOP50_RH;
        !
    ENDPROC


ENDMODULE