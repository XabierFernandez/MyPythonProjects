# Encoding: UTF-8
from krc2 import openExcel,dat1,dat2,dat3
from tkinter import messagebox
import tkinter
import os
import sys
import errno

ToolGarra='ToolGarra'
NumToolGarra=7



target2=None
target3=None
filename2=None



path='output'
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
                messagebox.showwarning('AVISO!', 'El numero de stringer debe estar entre 0 y 20.\rRevisar excel.\rNumero de error: {0}'.format(e.value))
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
                messagebox.showwarning('AVISO!', 'La mano del ala tiene que ser "L" o "R" ,right o left.\rRevisar excel.\rNumero de error: {0}'.format(e.value))
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
                messagebox.showerror('AVISO!', 'El numero de set tiene que estar entre 1 y 2.\rRevisar excel.\rNumero de error: {0}'.format(e.value))
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
                messagebox.showwarning('AVISO!', 'El numero de robot tiene que estar entre 1 y 2.\rRevisar excel.\rNumero de error: {0}'.format(e.value))
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
        
        
##########################################################################
def createFileNamePlace():
        global target2
        global target3
        global filename2

        folder="output//ROBOT{1}//{3}H//SET{2}//STR{0}//".format(isIntStr(openExcel.stringer),isRobot(openExcel.Robot), isSet(openExcel.Set),isLeftRight(openExcel.hand))
    
        dir_out_exists(folder)
        
        #providing file name
        filename2 = "nplacestr{0}RS1".format(isIntStr(openExcel.stringer))
        target2 = open (folder + filename2 + '.src', 'w') ## a will append, w will over-write
        target3 = open (folder + filename2 + '.dat', 'w') ## a will append, w will over-write
        
        
##########################################################################
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
                curing=(openExcel.curNameList[(i-1)])
                                 
               
                j=str(openExcel.curNameList[(i-1)])
                
                
                
                target2.write(dat2.HeaderCase.format(j))
                target2.write(dat2.TrayCase1.format(j, (openExcel.baseList[(i - 1)]), getBase(i)))
                target2.write(dat2.TrayCase2.format(j, (openExcel.baseList[(i - 1)]), getBase(i)))
                target2.write(dat2.TrayCase3.format(j, (openExcel.baseList[(i - 1)]), getBase(i)))
                #################################################                           
                target3.write(dat2.TrayCase1_dat.format(j, (openExcel.baseList[(i - 1)])))
                target3.write(dat2.TrayCase2_dat.format(j, (openExcel.baseList[(i - 1)])))
                target3.write(dat2.TrayCase3_dat.format(j, (openExcel.baseList[(i - 1)])))
                
                
        target2.write(dat2.FootSrc)
        target3.write(dat2.FootDat)


        target2.close()
        target3.close()
       
 
##########################################################################################
def leerExcel(num):

    
    openExcel.readExcel(num)
    createFileNamePlace()
    targetWriterPlace()
 
        
                
##############################################################################################
def main():
    # hide main window
    root = tkinter.Tk()
    root.withdraw()
    count=0   
    dir_out_exists(path)            
    s='Escriba el numero de hojas que quiere procesar, despues pulse intro :'
    numBooks=input(s)
    try:
        num = int(numBooks)
            
    except ValueError as e:
        messagebox.showwarning('AVISO!', 'El valor introducido, no es valido.',0)
        sys.exit(0)        
    try:
        if num in range(50):
            for i in range(num):
                leerExcel(i)
                count+=1
            messagebox.showinfo('Output', 'Proceso finalizado')
                
        else:
            raise MyError(4)                    
    except MyError as e:
        messagebox.showwarning('AVISO!', 'El valor introducido, debe ser un dato numerico de 0 a 50.\rNumero de error: {0}'.format(e.value))
        sys.exit(0)
    except IndexError as ex:
        messagebox.showwarning('AVISO!', 'Error de indice,numero de hojas existentes menor al valor proporcionado.\rSolo se han procesado {1} hojas.\r\r{0}'.format(ex,count))
        sys.exit(0)
##############################################################################################
class MyError(Exception):
                def __init__(self, value):
                        self.value = value
                def __str__(self):
                        return repr(self.value)

