
HeaderSrc = """&ACCESS RVP
&REL 1
&PARAM TEMPLATE = C:\KRC\Roboter\Template\ExpertVorgabe
&PARAM EDITMASK = * """

HeaderDat = """DEFDAT {0}
;FOLD EXTERNAL DECLARATIONS;%{{PE}}%MKUKATPBASIS,%CEXT,%VCOMMON,%P
;FOLD BASISTECH EXT;%{{PE}}%MKUKATPBASIS,%CEXT,%VEXT,%P
EXT  BAS (BAS_COMMAND  :IN,REAL  :IN )
DECL INT SUCCESS
;ENDFOLD (BASISTECH EXT)
;FOLD USER EXT;%{{E}}%MKUKATPUSER,%CEXT,%VEXT,%P
;Make here your modifications

;ENDFOLD (USER EXT)
;ENDFOLD (EXTERNAL DECLARATIONS)"""


#####################################################################
DeclSrc = """
DEF {0}( )
;FOLD INI
  ;FOLD BASISTECH INI
    GLOBAL INTERRUPT DECL 3 WHEN $STOPMESS==TRUE DO IR_STOPM ( )
    INTERRUPT ON 3 
    BAS (#INITMOV,0 )
  ;ENDFOLD (BASISTECH INI)
  ;FOLD USER INI
    ;Make your modifications here

  ;ENDFOLD (USER INI)
;ENDFOLD (INI)




SWITCH NumCuring
"""
##################################################################
FootSrc = """
ENDSWITCH
END"""

FootDat = """
ENDDAT"""
##########################################

HeaderCase = """
;*******************************************************
CASE {0}
;*******************************************************"""
	

TrayCase1 = """
;*** Utilizar para hacer touchup en ptp a continuacion ***;
; 1  Ejecutar Axis_Rob_Move
; 2  Hacer TouchUp en ptp
; 3  Eliminar Axis_Rob_Move y comentarios

Axis_Rob_Move(1.69,-82.8,66.93,14.32,12.14,193,70,50)

;FOLD PTP pWB{0}RS1 Vel=100 % PDAT_MESA Tool[10]:AMF1_G1000 Base[{1}]:{2};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VPTP,%P 1:PTP, 2:pWB{0}RS1, 3:, 5:100, 7:PDAT_MESA
$BWDSTART=FALSE
PDAT_ACT=PPDAT_MESA
FDAT_ACT=FpWB{0}RS1
BAS(#PTP_PARAMS,100)
PTP XpWB{0}RS1
;ENDFOLD
;*********************************************************;

;***Axis_Rob_Move de ayuda para aproximarse a dejada ***;
; Borrar tras touchup en LIN de dejada
Axis_Rob_Move(-90.22,-57.13,49.23,-5.44,97.37,193.9,20,50)
;*******************************************************;

PTP_OFFS(XP{0}RS1, FP{0}RS1, 0, -450, 30, 0, 0, 0, #TOOL, 20, 50, 0.0)

Cicle_Grp_M1000 (Inic_Pla_Right)

;***borrar***;
cyltopos(prg_200)
halt
;************;

LIN_OFFS(XP{0}RS1, FP{0}RS1, 0, 0, 30, 0, 0, 0, #TOOL, 0.1, 50, 0.0)
LIN_OFFS(XP{0}RS1, FP{0}RS1, 0, 0, 15, 0, 0, 0, #TOOL, 0.1, 50, 0.0)

Cntr_Grp_M1000 (C05C06,RH)
"""
#######################################################################################################
TrayCase1_dat = """
DECL E6POS XpWB{0}RS1={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL FDAT FpWB{0}RS1={{TOOL_NO 10,BASE_NO {1},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################

TrayCase2 = """
;FOLD LIN P{0}RS1 Vel=0.1 m/s LV020Z0 Tool[10]:AMF1_G1000 Base[{1}]:{2};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VLIN,%P 1:LIN, 2:P{0}RS1, 3:, 5:0.1, 7:V020Z0
$BWDSTART=FALSE
LDAT_ACT=LV020Z0
FDAT_ACT=FP{0}RS1
BAS(#CP_PARAMS,0.1)
LIN XP{0}RS1
;ENDFOLD

Cntr_Grp_M1000 (AMF09,RLS)
Cyltopos (PRG_51)
Cntr_Grp_M1000 (C07C08,RH)
Cyltopos (PRG_61)
Cntr_Grp_M1000 (AMF10,RLS)
Cntr_Grp_M1000 (C05C06,FREE)
Cntr_Grp_M1000 (C07C08,FREE)
Cyltopos(PRG_88)
LIN_REL{{Z -20}}#TOOL
Cyltopos (PRG_105)
LIN_REL{{Z -30}}#TOOL
Cyltopos (PRG_200)

;*** MOVIMIENTOS DE OFFSETS ***;

LIN_OFFS(XP{0}RS1, FP{0}RS1, 0, 0, -50, 0, 0, 0, #TOOL, 0.3, 50, 0.0)
LIN_OFFS(XP{0}RS1, FP{0}RS1, 0, -450, -50, 0, 0, 0, #TOOL, 0.3, 50, 0.0)

"""
#######################################################################################################
TrayCase2_dat = """
DECL E6POS XP{0}RS1={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL FDAT FP{0}RS1={{TOOL_NO 10,BASE_NO {1},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################

TrayCase3 = """
;******* MEDICION LASER *******;

LIN_OFFS(XPLAS{0}RS1_1, FPLAS{0}RS1_1, 0, -200, 0, 0, 0, 0, #TOOL, 0.3, 50, 0.0)

cyltopos (prg_61)

;FOLD LIN PLAS{0}RS1_1 Vel=0.3 m/s LV020Z0 Tool[10]:AMF1_G1000 Base[{1}]:{2};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VLIN,%P 1:LIN, 2:PLAS{0}RS1_1, 3:, 5:0.3, 7:V020Z0
$BWDSTART=FALSE
LDAT_ACT=LV020Z0
FDAT_ACT=FPLAS{0}RS1_1
BAS(#CP_PARAMS,0.3)
LIN XPLAS{0}RS1_1
;ENDFOLD

;Movimimiento de busqueda con laser
;Search( , )

;FOLD LIN PLAS{0}RS1_2 Vel=0.3 m/s LV020Z0 Tool[10]:AMF1_G1000 Base[{1}]:{2};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VLIN,%P 1:LIN, 2:PLAS{0}RS1_2, 3:, 5:0.3, 7:V020Z0
$BWDSTART=FALSE
LDAT_ACT=LV020Z0
FDAT_ACT=FPLAS{0}RS1_2
BAS(#CP_PARAMS,0.3)
LIN XPLAS{0}RS1_2
;ENDFOLD


;Movimimiento de busqueda con laser
;Search( , )

LIN_OFFS(XPLAS{0}RS1_1, FPLAS{0}RS1_1, 0, -200, 0, 0, 0, 0, #TOOL, 0.3, 50, 0.0)

;******************************;

;FOLD PTP pWB{0}RS1 Vel=100 % PDAT_MESA Tool[10]:AMF1_G1000 Base[{1}]:{2};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VPTP,%P 1:PTP, 2:pWB{0}RS1, 3:, 5:100, 7:PDAT_MESA
$BWDSTART=FALSE
PDAT_ACT=PPDAT_MESA
FDAT_ACT=FpWB{0}RS1
BAS(#PTP_PARAMS,100)
PTP XpWB{0}RS1
;ENDFOLD
"""
#######################################################################################################
TrayCase3_dat = """
DECL E6POS XPLAS{0}RS1_1={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL FDAT FPLAS{0}RS1_1={{TOOL_NO 10,BASE_NO {1},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
DECL E6POS XPLAS{0}RS1_2={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL FDAT FPLAS{0}RS1_2={{TOOL_NO 10,BASE_NO {1},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################
