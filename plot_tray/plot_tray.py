import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
from xlrd import XL_CELL_TEXT

#Variable global
gPoints=[]

def readExcel(numBooks):

    global gPoints

    book = open_workbook('plot_tray.xls')
    sheet = book.sheet_by_index(numBooks)
    ##############################
    for i in range(int(sheet.cell(1,6).value)):

        label=sheet.cell(1+i,5).value
        print ('Label:',label)
        wobjX1=float(sheet.cell(1,7).value)  
        wobjY1=float(sheet.cell(1,8).value) 
        wobjZ1=float(sheet.cell(1,9).value)
       

        wobjX2=float(sheet.cell(3,7).value)  
        wobjY2=float(sheet.cell(3,8).value) 
        wobjZ2=float(sheet.cell(3,9).value)
        

        x=float(sheet.cell(1+i,0).value) 
        y=float(sheet.cell(1+i,1).value)
        z=float(sheet.cell(1+i,2).value)

        if int(sheet.cell(1+i,4).value)==1:
            #negative x
            if x<0:
                    x = wobjX1 + x
                    
            else:
                    x = wobjX1 - x
            #######################
            #negative y
            if y<0:
                    y = wobjY1 + y
                    
            else:
                    y = wobjY1 + y
            #######################
            #negative z
            if z<0:
                    z = wobjZ1 + z
                    
            else:
                    z = wobjZ1 + z
    #################################################################################
        if int(sheet.cell(1+i,4).value)==2:
            #negative x
            if x<0:
                    x = -wobjX2 - x
                    
            else:
                    x = -wobjX2 - x
            #######################
            #negative y
            if y<0:
                    y = wobjY2 - y
                    
            else:
                    y = wobjY2 + y
            #######################
            #negative z
            if z<0:
                    z = wobjZ2 + z
                    
            else:
                    z = wobjZ2 + z
            #######################
                
                
        print( '[',x,',',y,',',z,']')
        point=[x,y,z,label]
        gPoints.append(point)
                
        
def run():
    
    
    zdir='z'
    s=30
    c='b'
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_autoscale_on(True)
    ax.set_zlim3d(-6000,6000)                    # viewrange for z-axis should be [-4,4] 
    ax.set_ylim3d(-6000, 6000)                   # viewrange for y-axis should be [-2,2] 
    ax.set_xlim3d(-6000, 6000)
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    readExcel(0)

    for i in range(len(gPoints)):
        ax.scatter(gPoints[i][0],gPoints[i][1],gPoints[i][2],zdir,s, c)
        ax.text(gPoints[i][0],gPoints[i][1],gPoints[i][2],gPoints[i][3],fontsize=9, bbox=dict(facecolor='yellow', alpha=0.5) )
        if not i==0:
                ax.plot([gPoints[(i-1)][0],gPoints[i][0]],[gPoints[(i-1)][1],gPoints[i][1]],[gPoints[(i-1)][2],gPoints[i][2]], c)


    plt.show()
    
    
if __name__ == '__main__':
	
	
	run()

