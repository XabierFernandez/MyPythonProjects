# Encoding: UTF-8
import os
import errno
import openExcel
import dat1
import dat2
import dat3
import ctypes
import sys

ToolGarra='ToolGarra'
NumToolGarra=7

target=None
target1=None
filename=None

target2=None
target3=None
filename2=None

target4=None
target5=None
filename3=None

path='output\\'
toolStr=['TOOL_Z1_1','TOOL_Z1_2','TOOL_Z2_1','TOOL_Z2_2']
baseStr=['pick','Par','Impar','BWB5S2','BWB4S2','BWB3S2','BWB2S2','BWB1S2','BWB5S1','BWB4S1','BWB3S1','BWB2S1','BWB1S1']

def dir_out_exists(aPath):
        try:
                os.makedirs(aPath)
        except OSError as exception:
                if exception.errno != errno.EEXIST:
                        raise

##############################
def isIntStr(var):
        
        try:
                var == int(var)
                if (var>0 and var<=20):
                        return var
                else:
                        raise MyError(3)
        except MyError as e:
                Mbox('AVISO!', 'El numero de stringer debe estar entre 0 y 20.\rRevisar excel.\rNumero de error: {0}'.format(e.value), 0)
                sys.exit(0)  
############################## 
##############################
def isIntStrTool(var):
        try:
                 var == int(var)
                                  
        except:
                 return False
                
        var1 = int(var)
        if (var1>0 and var1<=4):
                return True
        else:
                return False
############################## 
##############################
def isIntStrBase(var):
        try:
                 var == int(var)
                                  
        except:
                 return False
                
        var1 = int(var)
        if (var1>0 and var1<=3):
                return True
        else:
                return False

##############################   
##############################
def isIntCur(var):
        try:
                 var == int(var)
                                  
        except:
                 return False
                
        var1 = int(var)
        if (var1>1 and var1<=32):
                if var1 % 2 == 0:
                        return True
                else:
                        return False        
        else:
                return False
##############################    
##############################        
def isLeftRight(var):
        
        hands=('L','R')
        try:
                if var in hands:
                        return var
                else:
                        raise MyError(2)
        except MyError as e:
                Mbox('AVISO!', 'La mano del ala tiene que ser "L" o "R" ,right o left.\rRevisar excel.\rNumero de error: {0}'.format(e.value), 0)
                sys.exit(0)   
                
##############################        
##############################        
def isSet(var):
        
        sets=(1,2)
        try:
                if var in sets:
                        return var
                else:
                        raise MyError(1)

        except MyError as e:
                Mbox('AVISO!', 'El numero de set tiene que estar entre 1 y 2.\rRevisar excel.\rNumero de error: {0}'.format(e.value), 0)
                sys.exit(0)   
##############################
##############################        
def isRobot(var):
        
        robots=(1,2)
        try:
                if var in robots:
                        return var
                else:
                        raise MyError(5)

        except MyError as e:
                Mbox('AVISO!', 'El numero de robot tiene que estar entre 1 y 2.\rRevisar excel.\rNumero de error: {0}'.format(e.value), 0)
                sys.exit(0)   
##############################
def getTool(i):
        global toolStr
        tool=None
        
        if openExcel.toolList[(i-1)]==1:
                tool=toolStr[0]
        if openExcel.toolList[(i-1)]==2:
                tool=toolStr[1]
        if openExcel.toolList[(i-1)]==3:
                tool=toolStr[2]
        if openExcel.toolList[(i-1)]==4:
                tool=toolStr[3]
        return tool
####################################################
def getBase(i): 
        global baseStr
        base=None
################ pick up ################################################
        if openExcel.baseList[(i-1)]==1:
                base=baseStr[0]
################ par ################################################
        if openExcel.baseList[(i-1)]==2:
                base=baseStr[1]
################ impar ################################################
        if openExcel.baseList[(i-1)]==3:
                base=baseStr[2]
######################################################################
################ SET2 ################################################
        if openExcel.baseList[(i-1)]==6:
                base=baseStr[3]
        if openExcel.baseList[(i-1)]==7:
                base=baseStr[4]
        if openExcel.baseList[(i-1)]==8:
                base=baseStr[5]
        if openExcel.baseList[(i-1)]==9:
                base=baseStr[6]
        if openExcel.baseList[(i-1)]==10:
                base=baseStr[7]
######################################################################
################ SET1 ################################################
        if openExcel.baseList[(i-1)]==11:
                base=baseStr[8]
        if openExcel.baseList[(i-1)]==12:
                base=baseStr[9]
        if openExcel.baseList[(i-1)]==13:
                base=baseStr[10]
        if openExcel.baseList[(i-1)]==14:
                base=baseStr[11]
        if openExcel.baseList[(i-1)]==15:
                base=baseStr[12]
        return base
#####################################################

def createFileNamePick():
        global target
        global target1
        global filename

        folder="output\\ROBOT{1}\\{3}H\\SET{2}\\STR{0}\\".format(isIntStr(openExcel.stringer),isRobot(openExcel.Robot), isSet(openExcel.Set),isLeftRight(openExcel.hand))
        dir_out_exists(folder)
                                         
        #providing file name
        filename = "Mpickstr{0}{1}S{2}".format(isIntStr(openExcel.stringer), isLeftRight(openExcel.hand), isSet(openExcel.Set))
        target = open (folder + filename + '.src', 'w') ## a will append, w will over-write
        target1 = open (folder + filename + '.dat', 'w') ## a will append, w will over-write
        
        
##########################################################################
def createFileNamePlace():
        global target2
        global target3
        global filename2

        folder="output\\ROBOT{1}\\{3}H\\SET{2}\\STR{0}\\".format(isIntStr(openExcel.stringer),isRobot(openExcel.Robot), isSet(openExcel.Set),isLeftRight(openExcel.hand))
    
        dir_out_exists(folder)
        
        #providing file name
        filename2 = "Mplacstr{0}{1}S{2}".format(isIntStr(openExcel.stringer), isLeftRight(openExcel.hand), isSet(openExcel.Set))
        target2 = open (folder + filename2 + '.src', 'w') ## a will append, w will over-write
        target3 = open (folder + filename2 + '.dat', 'w') ## a will append, w will over-write
        
        
##########################################################################
##########################################################################
def createFileNameVision():
        global target4
        global target5
        global filename3

        folder="output\\ROBOT{1}\\{3}H\\SET{2}\\STR{0}\\".format(isIntStr(openExcel.stringer),isRobot(openExcel.Robot), isSet(openExcel.Set),isLeftRight(openExcel.hand))
       
        dir_out_exists(folder)
                                         
        #providing file name
        filename3 = "Mvisstr{0}{1}S{2}".format(isIntStr(openExcel.stringer), isLeftRight(openExcel.hand), isSet(openExcel.Set))
        target4 = open (folder + filename3 + '.src', 'w') ## a will append, w will over-write
        target5 = open (folder + filename3 + '.dat', 'w') ## a will append, w will over-write
        
        
##########################################################################
def targetWriterPick():
        global target
        global target1
        global filename
        
        cur=openExcel.NumCuring
        target.write(dat1.HeaderSrc)
        target.write(dat1.DeclSrc.format(filename))
        target1.write(dat1.HeaderDat.format(filename))
        
        for i in range(cur,0,-1):
                
                garra=''
                j=str(openExcel.curNameList[(i-1)])
                      
                points = ((j + '0'), (j + '1'),(j + '2'),('curing' + j),(j + '3'), (j + '4'))
                
                if ((openExcel.toolList[(i-1)])==1 or (openExcel.toolList[(i-1)])==2):
                        garra='L'
                if ((openExcel.toolList[(i-1)])==3 or (openExcel.toolList[(i-1)])==4):
                        garra='S'
                
                
                target.write(dat1.HeaderCase.format(j))
                target.write(dat1.TrayCase1.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target.write(dat1.TrayCase2.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target.write(dat1.TrayCase3.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target.write(dat1.TrayCase4.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target.write(dat1.TrayCase5.format(garra))
                target.write(dat1.TrayCase6.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target.write(dat1.TrayCase7.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                
                target1.write(dat1.TrayCase1_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target1.write(dat1.TrayCase2_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target1.write(dat1.TrayCase3_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target1.write(dat1.TrayCase4_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target1.write(dat1.TrayCase6_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target1.write(dat1.TrayCase7_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                
        target.write(dat1.FootSrc)
        target1.write(dat1.FootDat)


        target.close()
        target1.close()
       
                
##############################################################################################
##########################################################################
def targetWriterPlace():
        global target2
        global target3
        global filename2
        x=0
        cur=openExcel.NumCuring
        target2.write(dat2.HeaderSrc)
        target2.write(dat2.DeclSrc.format(filename2))
        target3.write(dat2.HeaderDat.format(filename2))
        
        for i in range(cur,0,-1):
                garra=''
                garra1=''
                direct=''
                LS=''
                paridad=False
                curing=(openExcel.curNameList[(i-1)])
                if curing %2 == 0:
                    paridad=True
                if curing %2 != 0:
                    paridad=False
                    
               
                j=str(openExcel.curNameList[(i-1)])
                points = ((j + '0'), (j + '1'),(j + '2'),('place' + j),(j + '3'), (j + '4'),(j + '5'))
                
                if ((openExcel.toolList[(i-1)])==1 or (openExcel.toolList[(i-1)])==2):
                        garra='L'
                if ((openExcel.toolList[(i-1)])==3 or (openExcel.toolList[(i-1)])==4):
                        garra='S'
                if isLeftRight(openExcel.hand)=='R':
                    ####Para garra L hand RH ##################################################################
                    if paridad==True and (openExcel.toolList[(i-1)]==1 or openExcel.toolList[(i-1)]==2):
                            direct='ADDR_XPOS'
                            LS='2'
                            garra1='Z1_1'
                    if paridad==False and (openExcel.toolList[(i-1)]==1 or openExcel.toolList[(i-1)]==2):
                            direct='ADDR_XPOS'
                            LS='1'
                            garra1='Z1_2'
                    ####Para Garra S hand RH ##################################################################
                    if  paridad==True and(openExcel.toolList[(i-1)]==3 or openExcel.toolList[(i-1)]==4):
                            direct='ADDR_XPOS'
                            LS='1'
                            garra1='Z2_2'
                    if paridad==False and (openExcel.toolList[(i-1)]==3 or openExcel.toolList[(i-1)]==4):                        
                            direct='ADDR_XPOS'
                            LS='2'
                            garra1='Z2_1'
                ###########################################################################################
                ###########################################################################################
                ####Para garra L hand LH ##################################################################
                if isLeftRight(openExcel.hand)=='L':
                    if paridad==True and (openExcel.toolList[(i-1)]==1 or openExcel.toolList[(i-1)]==2):
                            direct='ADDR_XPOS'
                            LS='1'
                            garra1='Z1_2'
                    if paridad==False and (openExcel.toolList[(i-1)]==1 or openExcel.toolList[(i-1)]==2):                        
                            direct='ADDR_XPOS'
                            LS='2'
                            garra1='Z1_1'
                    ####Para Garra S hand LH ##################################################################
                    if paridad==True and (openExcel.toolList[(i-1)]==3 or openExcel.toolList[(i-1)]==4):
                            direct='ADDR_XPOS'
                            LS='2'
                            garra1='Z2_1'
                    if paridad==False and (openExcel.toolList[(i-1)]==3 or openExcel.toolList[(i-1)]==4):            
                            direct='ADDR_XPOS'
                            LS='1'
                            garra1='Z2_2'        
                    
                    ########################################################################
                   
                
                
                
                target2.write(dat2.HeaderCase.format(j))
                target2.write(dat2.TrayCase1.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target2.write(dat2.TrayCase2.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target2.write(dat2.TrayCase3.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                #################################################
                if x>=2:
                        target2.write(dat2.TrayCase11.format(garra1))
                #################################################
                
                target2.write(dat2.TrayCase4.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                if x<2:
                    target2.write(dat2.TrayCase14.format())
                    
                #################################################
                if x>=2:
                        target2.write(dat2.TrayCase10.format(garra))
                #################################################   
                
                target2.write(dat2.TrayCase5.format(garra))
		target2.write(dat2.TrayCase13.format())
                target2.write(dat2.TrayCase15.format())
                target2.write(dat2.TrayCase6.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target2.write(dat2.TrayCase7.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target2.write(dat2.TrayCase12.format(LS, direct))
                target2.write(dat2.TrayCase8.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target2.write(dat2.TrayCase9.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                
                target3.write(dat2.TrayCase1_dat.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target3.write(dat2.TrayCase2_dat.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target3.write(dat2.TrayCase3_dat.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target3.write(dat2.TrayCase4_dat.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target3.write(dat2.TrayCase6_dat.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                target3.write(dat2.TrayCase7_dat.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                #target3.write( dat1.TrayCase8_dat.format(points,NumToolGarra, ToolGarra, (openExcel.baseList[(i-1)]),getBase(i)))
                target3.write(dat2.TrayCase9_dat.format(points, NumToolGarra, ToolGarra, (openExcel.baseList[(i - 1)]), getBase(i)))
                x+=1
                
        target2.write(dat2.FootSrc)
        target3.write(dat2.FootDat)


        target2.close()
        target3.close()
       
##########################################################################################
##########################################################################
def targetWriterVision():
        global target4
        global target5
        global filename3

        cur=openExcel.NumCuring
        target4.write(dat3.HeaderSrc)
        target4.write(dat3.DeclSrc.format(filename3))
        target5.write(dat3.HeaderDat.format(filename3))
        
        for i in range(cur,0,-1):
                garra1=''
                        
                j=str(openExcel.curNameList[(i-1)])
                points = ((j + '0'), (j + '1'),(j + '2'),(j + '3'), (j + '4'),(j + '5'))
                
                
                if ((openExcel.toolList[(i-1)])==1):
                        garra1='Z1_2'
                if ((openExcel.toolList[(i-1)])==2):
                        garra1='Z1_1'
                if ((openExcel.toolList[(i-1)])==3):
                        garra1='Z2_2'
                if ((openExcel.toolList[(i-1)])==4):
                        garra1='Z2_1'
                ########################################################################
                                
                target4.write(dat3.HeaderCase.format(j))
                target4.write(dat3.TrayCase1.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target4.write(dat3.TrayCase2.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target4.write(dat3.TrayCase3.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                
                target4.write(dat3.TrayCase4.format())
                
                target4.write(dat3.TrayCase5.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target4.write(dat3.TrayCase6.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                
                
                target5.write(dat3.TrayCase1_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target5.write(dat3.TrayCase2_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target5.write(dat3.TrayCase3_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target5.write(dat3.TrayCase5_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
                target5.write(dat3.TrayCase6_dat.format(points, NumToolGarra, ToolGarra, 1, 'pick'))
        
                
        target4.write(dat3.FootSrc)
        target5.write(dat3.FootDat)


        target4.close()
        target5.close()
       
##########################################################################################
def leerExcel(num):

    
    openExcel.readExcel(num)
    createFileNamePick()
    createFileNamePlace()
    createFileNameVision()

    targetWriterPick()
    targetWriterPlace()
    targetWriterVision()
        
                
##############################################################################################
def main():
    count=0   
    dir_out_exists(path)            
    s='Escriba el numero de hojas que quiere procesar, despues pulse intro :'
    numBooks=raw_input(s)
    try:
        num = int(numBooks)
            
    except ValueError as e:
        Mbox('AVISO!', 'El valor introducido, no es valido.',0)
        sys.exit(0)        
    try:
        if num in range(50):
            for i in range(num):
                leerExcel(i)
                count+=1
            Mbox('Output', 'Proceso finalizado', 0)
                
        else:
            raise MyError(4)                    
    except MyError as e:
        Mbox('AVISO!', 'El valor introducido, debe ser un dato numerico de 0 a 50.\rNumero de error: {0}'.format(e.value), 0)
        sys.exit(0)
    except IndexError as ex:
        Mbox('AVISO!', 'Error de indice,numero de hojas existentes menor al valor proporcionado.\rSolo se han procesado {1} hojas.\r\r{0}'.format(ex,count), 0)
        sys.exit(0)
    
   
##############################################################################################  
def Mbox(title, text, style):
        ctypes.windll.user32.MessageBoxA(0, text, title, style)
##############################################################################################
class MyError(Exception):
                def __init__(self, value):
                        self.value = value
                def __str__(self):
                        return repr(self.value)

