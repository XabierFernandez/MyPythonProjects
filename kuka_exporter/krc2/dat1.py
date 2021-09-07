
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


GRIPP (POS_PICK_L)
GRIPP (POS_PICK_S)

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
;FOLD PTP P{0[0]} CONT Vel=100 % PDAT{0[0]} Tool[{1}] :{2}  Base[{3}] :{4} ;%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VPTP,%P 1:PTP, 2:P{0[0]}, 3:C_PTP, 5:100, 7:PDAT{0[0]}
$BWDSTART=FALSE
PDAT_ACT=PPDAT{0[0]}
FDAT_ACT=FP{0[0]}
BAS(#PTP_PARAMS,100)
PTP XP{0[0]} C_PTP
;ENDFOLD"""
#######################################################################################################
TrayCase1_dat = """
DECL E6POS XP{0[0]}={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL PDAT PPDAT{0[0]}={{VEL 100.0,ACC 100.0,APO_DIST 100.0,APO_MODE #CPTP}}
DECL FDAT FP{0[0]}={{TOOL_NO {1},BASE_NO {3},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################

TrayCase2 = """
;FOLD LIN P{0[1]} CONT Vel=0.5 m/s CPDAT{0[1]} Tool[{1}]:{2} Base[{3}]:{4};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VLIN,%P 1:LIN, 2:P{0[1]}, 3:C_DIS, 5:0.5, 7:CPDAT{0[1]}
$BWDSTART=FALSE
LDAT_ACT=LCPDAT{0[1]}
FDAT_ACT=FP{0[1]}
BAS(#CP_PARAMS,0.5)
LIN XP{0[1]} C_DIS
;ENDFOLD"""
#######################################################################################################
TrayCase2_dat = """
DECL E6POS XP{0[1]}={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL LDAT LCPDAT{0[1]}={{VEL 0.5,ACC 100.0,APO_DIST 10.0,APO_FAC 50.0,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0}}
DECL FDAT FP{0[1]}={{TOOL_NO {1},BASE_NO {3},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################

TrayCase3 = """
;FOLD LIN P{0[2]} CONT Vel=0.3 m/s CPDAT{0[2]} Tool[{1}]:{2} Base[{3}]:{4};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VLIN,%P 1:LIN, 2:P{0[2]}, 3:C_DIS, 5:0.3, 7:CPDAT{0[2]}
$BWDSTART=FALSE
LDAT_ACT=LCPDAT{0[2]}
FDAT_ACT=FP{0[2]}
BAS(#CP_PARAMS,0.3)
LIN XP{0[2]} C_DIS
;ENDFOLD"""
#######################################################################################################
TrayCase3_dat = """
DECL E6POS XP{0[2]}={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL LDAT LCPDAT{0[2]}={{VEL 0.3,ACC 100.0,APO_DIST 5.0,APO_FAC 50.0,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0}}
DECL FDAT FP{0[2]}={{TOOL_NO {1},BASE_NO {3},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################

TrayCase4 = """
;FOLD LIN {0[3]} Vel=0.1 m/s CPDAT{0[3]} Tool[{1}]:{2} Base[{3}]:{4};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VLIN,%P 1:LIN, 2:{0[3]}, 3:, 5:0.1, 7:CPDAT{0[3]}
$BWDSTART=FALSE
LDAT_ACT=LCPDAT{0[3]}
FDAT_ACT=FP{0[3]}
BAS(#CP_PARAMS,0.1)
LIN X{0[3]}
;ENDFOLD"""
#######################################################################################################
TrayCase4_dat = """
DECL E6POS X{0[3]}={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL LDAT LCPDAT{0[3]}={{VEL 0.1,ACC 100.0,APO_DIST 100.0,APO_FAC 50.0,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0}}
DECL FDAT FP{0[3]}={{TOOL_NO {1},BASE_NO {3},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################

TrayCase5 = """
GRIPP (CLOSE_{0})
CNTRLGRIPP(CLOSE_{0})"""

TrayCase6 = """
;FOLD LIN P{0[4]} CONT Vel=0.5 m/s CPDAT{0[4]} Tool[{1}]:{2} Base[{3}]:{4};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VLIN,%P 1:LIN, 2:P{0[4]}, 3:C_DIS, 5:0.5, 7:CPDAT{0[4]}
$BWDSTART=FALSE
LDAT_ACT=LCPDAT{0[4]}
FDAT_ACT=FP{0[4]}
BAS(#CP_PARAMS,0.5)
LIN XP{0[4]} C_DIS
;ENDFOLD"""
#######################################################################################################
TrayCase6_dat = """
DECL E6POS XP{0[4]}={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL LDAT LCPDAT{0[4]}={{VEL 0.5,ACC 100.0,APO_DIST 10.0,APO_FAC 50.0,ORI_TYP #VAR,CIRC_TYP #BASE,JERK_FAC 50.0}}
DECL FDAT FP{0[4]}={{TOOL_NO {1},BASE_NO {3},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################

TrayCase7 = """
;FOLD PTP P{0[5]} CONT Vel=100 % PDAT{0[5]} Tool[{1}]:{2} Base[{3}]:{4};%{{PE}}%R 5.5.32,%MKUKATPBASIS,%CMOVE,%VPTP,%P 1:PTP, 2:P{0[5]}, 3:C_PTP, 5:100, 7:PDAT{0[5]}
$BWDSTART=FALSE
PDAT_ACT=PPDAT{0[5]}
FDAT_ACT=FP{0[5]}
BAS(#PTP_PARAMS,100)
PTP XP{0[5]} C_PTP
;ENDFOLD"""
#######################################################################################################
TrayCase7_dat = """
DECL E6POS XP{0[5]}={{X 0,Y 0,Z 0,A 0,B 0,C 0,S 2,T 10,E1 0.0,E2 0.0,E3 0.0,E4 0.0,E5 0.0,E6 0.0}}
DECL PDAT PPDAT{0[5]}={{VEL 100.0,ACC 100.0,APO_DIST 100.0,APO_MODE #CPTP}}
DECL FDAT FP{0[5]}={{TOOL_NO {1},BASE_NO {3},IPO_FRAME #BASE,POINT2[] " ",TQ_STATE FALSE}}
;"""
#######################################################################################################