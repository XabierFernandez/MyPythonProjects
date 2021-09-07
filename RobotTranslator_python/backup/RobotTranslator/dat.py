
HeaderPE="""/PROG  {0} PROCESS
/ATTR
OWNER	        = MNEDITOR;
COMMENT	        = "{0}";
PROG_SIZE        = 1238;
CREATE	        = DATE 04-06-10  TIME 16:17:00;
MODIFIED        = DATE 04-08-19  TIME 22:01:04;
FILE_NAME        = ;
VERSION        = 0;
LINE_COUNT        = {1};
MEMORY_SIZE        = 1522;
PROTECT	        = READ_WRITE;
TCD:  STACK_SIZE  = 0,
      TASK_PRIORITY  = 50,
      TIME_SLICE  = 0,
      BUSY_LAMP_OFF  = 0,
      ABORT_REQUEST  = 0,
      PAUSE_REQUEST  = 0;
DEFAULT_GROUP        = 1,*,*,*,*;
CONTROL_CODE        = 00000000 00000000;
/MN"""

POSJ= """
   {0}:{1} P[{2}] 100% FINE  ;"""
   
POSL= """
   {0}:{1} P[{2}] 300mm/sec CNT5  ;"""
   
HeaderPOSDAT="""
/POS"""

POSDAT = """
P[{0}: "{1}"]{{
   GP1:
  UF : 0, UT : 0,           CONFIG : 'N U T, 0, 0, 0',
  X = {2}  mm,  Y =  {3}  mm,  Z =  {4}  mm,
  W =    {5} deg,  P =    {6} deg,  R =   {7} deg,
  E1= {8}  mm
}};"""

FooterDAT="""
/END
"""



	

