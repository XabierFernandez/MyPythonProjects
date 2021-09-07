from mmap import mmap,ACCESS_READ
from xlrd import open_workbook
from xlrd import XL_CELL_TEXT

stringer=None
hand=None
Set=None
NumCuring=None

toolList=[]
baseList=[]
curNameList=[]


def readExcel(numBooks):

    global stringer
    global hand
    global Set
    global NumCuring
    global Robot

    global toolList
    global baseList
    global curNameList

    book = open_workbook('setup.xls')
    sheet = book.sheet_by_index(numBooks)
    ##############################

    stringer=int(sheet.cell(0,1).value)
    hand=sheet.cell(1,1).value
    Set=int(sheet.cell(2,1).value)
    NumCuring=int(sheet.cell(3,1).value)
    Robot=int(sheet.cell(4,1).value)

    for i in range(int(NumCuring)):
        curNameList.append(int(sheet.cell(6+i,0).value))
        toolList.append(int(sheet.cell(6+i,1).value))
        baseList.append(int(sheet.cell(6+i,2).value))



    curNameList.reverse()
    toolList.reverse()
    baseList.reverse()



    print(curNameList)
    print(" ")
    ##	print baseList
