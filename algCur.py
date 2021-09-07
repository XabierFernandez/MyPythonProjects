
curToolInic=90721
curToolEnd =90702
curCurrent=0


bStep=False
curNext=curToolInic

while curCurrent!=curToolEnd:
    
    curCurrent=curNext
    if((int(curToolInic/2)*2)- curToolInic)!=0:
        if bStep==False:
            
            curNext=curNext+1
            bStep=True
        else:

            curNext=curNext-3
            bStep=False
    else:
        if bStep==False:
            
            curNext=curNext-3
            bStep=True
        else:

            curNext=curNext+1
            bStep=False
        
    
    print (curCurrent)
