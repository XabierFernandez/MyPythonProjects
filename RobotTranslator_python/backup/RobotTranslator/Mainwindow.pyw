

import wx
import os
import math
import dat 

import transformations as tran



#---------------------------------------------------------------------------
searchListInst=["MoveJ","MoveL","DispL","OcupaPortonJ","OcupaZonaJ","LiberaZonaJ","LiberaPortonJ","OcupaPortonL","OcupaZonaL","LiberaZonaL","LiberaPortonL"]

moveJ=["MoveJ","OcupaPortonJ","OcupaZonaJ","LiberaZonaJ","LiberaPortonJ"]
moveL=["MoveL","DispL","OcupaPortonL","OcupaZonaL","LiberaZonaL","LiberaPortonL"]
moveC=["DispC","MoveC"]
sampleList = ['ABB'] 
sampleList1 = ['FANUC','KuKa'] 
bOk=False
# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "ABB source (*.mod)|*.MOD|"\
           "All files (*.*)|*.*"
#---------------------------------------------------------------------------

class MyFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """   
   
     
    def __init__(self, parent, title):
            
        wx.Frame.__init__(self, parent, -1, title,
                          style= wx.SYSTEM_MENU | wx.CAPTION |wx.MINIMIZE_BOX| wx.CLOSE_BOX)
        
        self.CenterOnScreen()
        self.SetBackgroundColour(wx.Colour(100,200,200))
        
        
        self.cb = wx.ComboBox(self, 500,sampleList[0] , (90, 50), 
                         (160, -1), sampleList,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER
                         |wx.CB_READONLY 
                         )
        self.l1=wx.StaticText(self, -1, "Convertir a:")
        
        self.cb1 = wx.ComboBox(self, 500, sampleList1[0], (90, 50), 
                         (160, -1), sampleList1,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER
                         |wx.CB_READONLY 
                         )
       
        
        self.t1 = wx.TextCtrl(self, -1,
                        u'Has selecionado ABB para llevar acabo la conversion.'
                        u'Los datos de robtarget, \xbf Est\xe1n en un archivo a parte?',
                       size=(200, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        
        self.chckb1 = wx.CheckBox(self, -1, "Si")#, (65, 40), (150, 20), wx.NO_BORDER)
        self.Bind(wx.EVT_CHECKBOX, self.OnCheck, self.chckb1)
        
        self.l2=wx.StaticText(self, -1, "Archivo a procesar")
        self.t2= wx.TextCtrl(self, -1, "",size=(210, -1),style=wx.TE_READONLY)
        self.explorarButton=wx.Button(self, -1, "Explorar", (10,10))
        self.Bind(wx.EVT_BUTTON, self.OnButtonFile, self.explorarButton)
        
        self.l3=wx.StaticText(self, -1, "Archivo de datos Globales para ABB ")
        self.t3= wx.TextCtrl(self, -1, "",size=(210, -1),style=wx.TE_READONLY)
        self.explorarButton1=wx.Button(self, -1, "Explorar", (10,10))
        self.Bind(wx.EVT_BUTTON, self.OnButtonFile1, self.explorarButton1)
        
        self.l4=wx.StaticText(self, -1, "Directorio destino")
        self.t4= wx.TextCtrl(self, -1, "",size=(210, -1),style=wx.TE_READONLY)
        self.explorarButton2=wx.Button(self, -1, "Explorar", (10,10))
        self.Bind(wx.EVT_BUTTON, self.OnButtonDir, self.explorarButton2)
        
        self.cerrarButton=wx.Button(self, -1, "Cerrar", (10,10))
        self.Bind(wx.EVT_BUTTON, self.OnClose, self.cerrarButton)
        self.procesarButton=wx.Button(self, -1, "Procesar", (10,10))
        self.Bind(wx.EVT_BUTTON, self.OnProcesar, self.procesarButton)
        
        box1 = wx.FlexGridSizer(rows=0,cols=5, hgap=30, vgap=5)
        box1.AddMany([self.cerrarButton,self.procesarButton,(0,0),(0,0),(0,0)]) 
      
        
        box = wx.FlexGridSizer(rows=0,cols=5, hgap=20, vgap=5) 
        box.AddMany([self.cb,(0,0),(0,0),(0,0),(0,0),
                    self.l1,(0,0),(0,0),(0,0),(0,0),
                    self.cb1,(0,0),(0,0),(0,0),(0,0),
                    self.t1,self.chckb1,(0,0),(0,0),(0,0),
                    self.l2,(0,0),(0,0),self.l4,(0,0),
                    self.t2,self.explorarButton,(0,0),self.t4,self.explorarButton2,
                    self.l3,(0,0),(0,0),(0,0),(0,0),
                    self.t3,self.explorarButton1,(0,0),(0,0),(0,0),
                    (0,0),(0,0),(0,0),(0,0),(0,0)])
        
        subMainSizer=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer.Add(box,1, wx.EXPAND | wx.ALL, 20)
        
        subMainSizer1=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer1.Add(box1,1, wx.EXPAND | wx.ALL, 20)
        
        MainSizer=wx.BoxSizer(wx.VERTICAL)
        MainSizer.Add(subMainSizer)
        MainSizer.Add(subMainSizer1)
        
        self.SetSizerAndFit(MainSizer)
        
        #################################
        self.l3.Enable(False)
        self.t3.Enable(False)
        self.explorarButton1.Enable(False)
        
    def OnButtonDir(self, evt):
       
        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'open' dialog, and allows multitple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.
        
        dlg = wx.DirDialog(self,"Seleccionar directorio:",\
                           style=1 ,defaultPath='c:/', pos = (100,100))

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPath()
          
            self.t4.SetValue(path)
            
        dlg.Destroy()
    
    
    def OnButtonFile(self, evt):
      

        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'open' dialog, and allows multitple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.
        dlg = wx.FileDialog(
            self, message="Seleccionar archivo",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPaths()
            self.t2.SetValue(path[0])
            

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()
    
    def OnButtonFile1(self, evt):
      

        # Create the dialog. In this case the current directory is forced as the starting
        # directory for the dialog, and no default file name is forced. This can easilly
        # be changed in your program. This is an 'open' dialog, and allows multitple
        # file selections as well.
        #
        # Finally, if the directory is changed in the process of getting files, this
        # dialog is set up to change the current working directory to the path chosen.
        dlg = wx.FileDialog(
            self, message="Seleccionar archivo",
            defaultDir=os.getcwd(), 
            defaultFile="",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR
            )

        # Show the dialog and retrieve the user response. If it is the OK response, 
        # process the data.
        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            path = dlg.GetPaths()
            self.t3.SetValue(path[0])
         

        # Destroy the dialog. Don't do this until you are done with it!
        # BAD things can happen otherwise!
        dlg.Destroy()
    
    def OnCheck(self, evt):
        
        if evt.IsChecked()==True:
            self.l3.Enable(True)
            self.t3.Enable(True)
            self.explorarButton1.Enable(True)
        else:
            self.t3.Clear()
            self.l3.Enable(False)
            self.t3.Enable(False)
            self.explorarButton1.Enable(False)
            
#################################################################  
#################################################################  
#################################################################  
            
    def OnProcesar(self, evt): 
        
        t2 = self.t2.GetValue()
        t4 = self.t4.GetValue()
        if t2!='' and t4!='':
            dlg = wx.MessageDialog(self, u'\xbfQuiere proceder?',
                           'Alerta',
                           #wx.OK | wx.ICON_INFORMATION 
                           wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_QUESTION
                           )
           

            result=dlg.ShowModal()
            dlg.Destroy() 
            if result==5103:
                file = open(self.t2.GetValue()).readlines()
                lista=self.getInstListProc(file)
                
                self.writeToFile(lista)
                
                dlg = wx.MessageDialog(self, u'Proceso finalizado!!',
                           'Mensaje',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                
                dlg.ShowModal()
                dlg.Destroy()
    
                print ("Proceso finalizado")
      
               
        else:
            dlg = wx.MessageDialog(self, u'Debe selecionar una ruta para\narchivo a procesar y directorio destino',
                           'Mensaje',
                           wx.OK | wx.ICON_EXCLAMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
           
            dlg.ShowModal()
            dlg.Destroy()
      
        
        
###################################################################   
    def writeToFile(self,list): 
        
        count=0
        index=0
        
        for i in range(0,len(list)):
            print len(list[i])
            if len(list[i])!=9 and list[i]!='?xabi?' :
                fileName=list[i].replace('=','')
                target=open(self.t4.GetValue()+ '\\' + fileName+".PE",'w')
               
                count=0
                index=i+1
            if len(list[i])==9:
                count=count+1
                dictionary=list[i]
                move=dictionary['MOVE']
                if move=='J':
                    target.write( dat.POSJ.format(count,move,count))
                if move=='L':
                    target.write( dat.POSL.format(count,move,count))
                    
                
                if len(list)>i+1:
                    if len(list[i+1])!=9 or list[i+1]=='?xabi?':
                        count=0
                        target.write(dat.HeaderPOSDAT)
                        for j in range(index,len(list)):
                            if len(list[j])==9:
                              
                                count=count+1
                                dictionary=list[j]
                                punto=dictionary['POINT']
                                tx=dictionary['Tx']
                                ty=dictionary['Ty']
                                tz=dictionary['Tz']
                                rz=dictionary['Rz']
                                ry=dictionary['Ry']
                                rx=dictionary['Rx']
                                extj=dictionary['EXTJ']
                                
                                target.write( dat.POSDAT.format(count,punto,tx,ty,tz,rz,ry,rz,extj))
                        
                            else:
                                break
                        target.write( dat.FooterDAT)
                        target.close()
                        # read the current contents of the file 
                        f = open(self.t4.GetValue()+ '\\' + fileName+".PE",'r')
                        text = f.read() 
                        f.close() 
                        # open the file again for writing 
                        f = open(self.t4.GetValue()+ '\\' + fileName+".PE",'w') 
                        f.write(dat.HeaderPE.format(fileName,count)) 
                        # write the original contents 
                        f.write(text) 
                        f.close() 
                        
                        index=0   
                
                
            
    
    def getInstListProc(self, file):
        listaInst=[]
        inst =dict({'MOVE':'', 'POINT':'', 'Tx':'', 'Ty':'', 'Tz':'','Rx':'','Ry':'','Rz':'','EXTJ':''})
        listInst=self.getListProc(file)
        
        for kins in range(0,len(listInst)):
            print listInst[kins]
      
        
        for i in range (0,len(listInst)):
            if len(listInst[i])>1:
                listaInst.append(listInst[i][0]+'==========')
               
                for j in range(1,len(listInst[i])):
                
                    inst['MOVE']=self.searchMove(listInst[i][j])
                    inst['POINT']=self.searchPoint(listInst[i][j])
                    punto=inst['POINT'].lower()
                  
                    if punto.find('home')==-1:
                        angulos=self.searchAngles(inst['POINT'])
                        inst['Rx']=angulos[0]
                        inst['Ry']=angulos[1]
                        inst['Rz']=angulos[2]
                       
                    else:
                        inst['Rx']='0.0'
                        inst['Ry']='0.0'
                        inst['Rz']='0.0'
                        
                    if punto.find('home')==-1: 
                        trans=self.searchTrans(inst['POINT'])
                        inst['Tx']=trans[0]
                        inst['Ty']=trans[1]
                        inst['Tz']=trans[2]
                        
                    else:
                        inst['Tx']='0.0'
                        inst['Ty']='0.0'
                        inst['Tz']='0.0'
                        
                    if punto.find('home')==-1: 
                        inst['EXTJ']=self.searchEXTJ(inst['POINT'])
                                                
                    else:
                        inst['EXTJ']='0.0'
                  
                    listaInst.append(inst.copy())
        listaInst.append('?xabi?')          
        return listaInst
   
        
    
    def getListProc(self, file):
       
        listaProcedimientos=self.searchProc(file)
        listaPuntosProc=self.searchPointsProc(file,listaProcedimientos)
        
        return listaPuntosProc
    
#################################################################   
    def searchTrans(self,punto): 
        trans=[]
        if self.chckb1.IsChecked():
            file = open(self.t3.GetValue()).readlines()
        else:
            file = open(self.t2.GetValue()).readlines()
        
        for i in range(0,len(file)):
            search=file[i].find("robtarget")
            search1=file[i].find(punto + ":")
            searcht=file[i].find("[[")
            searcht1=file[i].find("],",searcht)
        
            if search!=-1 and search1!=-1 and searcht!=-1 and searcht1!=-1 :
                linea=file[i]
                translations=linea[searcht+2:searcht1]
                translations = translations.split(',')
                Tx=format(float(translations[0]),'0.3f')
                Ty=format(float(translations[1]),'0.3f')
                Tz=format(float(translations[2]),'0.3f')
                trans.append(str(Tx))
                trans.append(str(Ty))
                trans.append(str(Tz))
                            
                
        return trans
#################################################################   
    def searchEXTJ(self,punto):
        exteje=''
        if self.chckb1.IsChecked():
            file = open(self.t3.GetValue()).readlines()
        else:
            file = open(self.t2.GetValue()).readlines()
        for i in range(0,len(file)):    
            search=file[i].find("robtarget")
            search1=file[i].find(punto + ":")
            searchext=file[i].find(",[")
            searchext1=file[i].find(",[",searchext+1)
            searchext2=file[i].find(",[",searchext1+1)
            searchtext3=file[i].find(",",searchext2+1)
             
            if search!=-1 and search1!=-1 and searchext2!=-1 and searchtext3!=-1 :
                linea=file[i]
                exteje=format(float(linea[searchext2+2:searchtext3]),'0.3f')
                exteje=str(exteje)
        return exteje
        
#################################################################   
    def searchAngles(self,punto): 
        angulos=[]
        if self.chckb1.IsChecked():
            file = open(self.t3.GetValue()).readlines()
        else:
            file = open(self.t2.GetValue()).readlines()
        
        for i in range(0,len(file)):
            search=file[i].find("robtarget")
            search1=file[i].find(punto + ":")
            searchq=file[i].find(",[")
            searchq1=file[i].find("],",searchq)
        
            if search!=-1 and search1!=-1 and searchq!=-1 and searchq1!=-1 :
                linea=file[i]
                quaternios=linea[searchq+2:searchq1]
                            
                quaternion= quaternios.split(',')
                angles = tran.euler_from_quaternion([float(quaternion[0]),float(quaternion[1]),float(quaternion[2]),float(quaternion[3])],'sxyz')
                Rx=format(math.degrees(angles[0]),'0.3F')
                Ry=format(math.degrees(angles[1]),'0.3F')
                Rz=format(math.degrees(angles[2]),'0.3F')
                angulos.append(Rx)
                angulos.append(Ry)
                angulos.append(Rz)
                
        return angulos
        
    
#################################################################   
    def searchPoint(self, linea): 
        punto="" 
        search1=linea.find("p",4) 
        searchp=linea.find(",v",4)
        
        if search1!=-1 and searchp!=-1:
            
            punto=linea[search1:searchp]
            
        return punto
          
#################################################################   
    def searchMove(self, linea):
        move=''
        
        for term in range(0,len(moveJ)):

            if linea.find(moveJ[term])==0:
                move='J'
        for term in range(0,len(moveL)):

            if linea.find(moveL[term])==0:
                move='L'
        for term in range(0,len(moveC)):

            if linea.find(moveC[term])==0:
                move='C'
        
        return move
            
 
         
#################################################################   
    def searchInst(self, linea):
        bOk=False
        
        for term in range(0,len(searchListInst)):

            if linea.find(searchListInst[term])!=-1 and linea.find('!')==-1 :
                bOk=True
        
        return bOk
            
#################################################################  
    def searchProc(self,listaFile):
        lista=[]
        for line in range(0,len(listaFile)):
            search=listaFile[line].find("PROC")
            search1=listaFile[line].find("()")
            search2=listaFile[line].find("ENDPROC") 
            
            if search!=-1 and search1!=-1 and search2==-1:
                linea=listaFile[line]
                proceso=linea[search+4:search1]
                lista.append(proceso.strip())
                            
        return lista   
#################################################################      
    def searchPointsProc(self,listaFile,listaProcedimientos):
        listaProc=[]
        listaPoints=[]
        bOk=False
        for line1 in range(0,len(listaProcedimientos)):
                       
            listaPoints=[]
            listaPoints.append(listaProcedimientos[line1])
          
            for line2 in range(0,len(listaFile)):
                if (listaFile[line2].find(listaProcedimientos[line1])!=-1 and 
                    listaFile[line2].strip().find("PROC")==0 and listaFile[line2].find("()")!=-1):
                    
                    bOk=True
               
                if listaFile[line2].strip().find("ENDPROC")==0 :
                    
                    bOk=False
                               
                if self.searchInst(listaFile[line2])==True and bOk==True:
                         
                    listaPoints.append(listaFile[line2].strip())
                    
            
            listaProc.append(listaPoints)
            
       
        return listaProc	
                            
#################################################################              
            
            
            
        
             
#    def Rutinas(self, listaFile):
#        listaInst=[]
#        listaFinal=[]
        
#        listapuntos=[]
#        folder= self.t4.GetValue()
#        for line in range(0,len(listaFile)):
#            search=listaFile[line].find("PROC")
#            search1=listaFile[line].find("()")
#            search2=listaFile[line].find("ENDPROC")
            
#            search3=listaFile[line].find("MoveJ") 
#            search4=listaFile[line].find("MoveL") 
#            search5=listaFile[line].find("DispL")
#            search6=listaFile[line].find("DispC")
              
#            search7=listaFile[line].find("OcupaPortonJ")
#            search8=listaFile[line].find("OcupaZonaJ")
#            search9=listaFile[line].find("LiberaZonaJ") 
#            search10=listaFile[line].find("LiberaPortonJ") 
            
#            search11=listaFile[line].find("OcupaPortonL")
#            search12=listaFile[line].find("OcupaZonaL")
#            search13=listaFile[line].find("LiberaZonaL") 
#            search14=listaFile[line].find("LiberaPortonL")  
                        
        
#            if search!=-1 and search1!=-1 and search2==-1:
                
                
                                    
#                linea=listaFile[line]
#                proceso=linea[search+4:search1]
#                filename=proceso.strip()
#                target=open (folder +"\\" + filename + '.PE', 'w')
                
               
#            if (search3!=-1 or search4!=-1 or search5!=-1 or search6!=-1 or 
#                search7!=-1 or search8!=-1 or search9!=-1 or 
#                search10!=-1 or search11!=-1 or search12!=-1 or search13!=-1 or search14!=-1)and search2==-1 :
                
#                listapuntos.append(listaFile[line].strip())
          
#            for line in range(0,len(listapuntos)):
#                search3=listapuntos[line].find("MoveJ") 
#                search4=listapuntos[line].find("MoveL") 
#                search5=listapuntos[line].find("DispL")
#                search6=listapuntos[line].find("DispC")
                  
#                search7=listapuntos[line].find("OcupaPortonJ")
#                search8=listapuntos[line].find("OcupaZonaJ")
#                search9=listapuntos[line].find("LiberaZonaJ") 
#                search10=listapuntos[line].find("LiberaPortonJ") 
                
#                search11=listapuntos[line].find("OcupaPortonL")
#                search12=listapuntos[line].find("OcupaZonaL")
#                search13=listapuntos[line].find("LiberaZonaL") 
#                search14=listapuntos[line].find("LiberaPortonL") 
                
#                search1=listapuntos[line].find("p",4) 
#                searchp=listapuntos[line].find(",v",4)
                
#                if (search4!=-1 or search5!=-1 or search11!=-1 or search12!=-1 or 
#                search13!=-1 or search14!=-1):
#                    move="L"
#                    target.write("Move type :" + move)
#                    target.write("\n")
#                    listaInst.append(move)
                    
#                if (search3!=-1 or search7!=-1 or search8!=-1 or search9!=-1 or 
#                search10!=-1 ):
#                    move="J"
#                    target.write("\nMove type :" + move)
#                    target.write("\n")
#                    listaInst.append(move)
                    
            
#                if search1!=-1 and searchp!=-1:
#                    linea=listapuntos[line]
                    
#                    punto=linea[search1:searchp]
#                    target.write("Punto :" + punto)
#                    target.write("\n")
#                    listaInst.append(punto)
                    
#                    for line in range(0,len(listaFile)):
#                        search=listaFile[line].find("robtarget")
#                        search1=listaFile[line].find(punto + ":")
                        
#                        searchq=listaFile[line].find(",[")
#                        searchq1=listaFile[line].find("],",searchq)
                        
#                        searcht=listaFile[line].find("[[")
#                        searcht1=listaFile[line].find("],",searcht)
            
#                        searchext=listaFile[line].find(",[")
#                        searchext1=listaFile[line].find(",[",searchext+1)
#                        searchext2=listaFile[line].find(",[",searchext1+1)
#                        searchtext3=listaFile[line].find(",",searchext2+1)
#                        if search!=-1 and search1!=-1 and searchext2!=-1 and searchtext3!=-1 :
#                            linea=listaFile[line]
#                            exteje=linea[searchext2+2:searchtext3]
#                            target.write("Datos eje externo :" + exteje)
#                            target.write("\n") 
#                            listaInst.append(exteje)                        
#                        if search!=-1 and search1!=-1 and searcht!=-1 and searcht1!=-1 :
#                            linea=listaFile[line]
#                            translations=linea[searcht+2:searcht1]
#                            translations = translations.split(',')
#                            Tx=translations[0]
#                            Ty=translations[1]
#                            Tz=translations[2]
#                            translaciones=[Tx,Ty,Tz]
#                            target.write("Datos translaciones :" + str(translaciones))
#                            target.write("\n")
#                            listaInst.append(translaciones)  
#                        if search!=-1 and search1!=-1 and searchq!=-1 and searchq1!=-1 :
#                            linea=listaFile[line]
#                            quaternios=linea[searchq+2:searchq1]
#                            #print ("\n"+"q = " + quaternios )
#                            quaternion= quaternios.split(',')
#                            angles = tran.euler_from_quaternion([float(quaternion[0]),float(quaternion[1]),float(quaternion[2]),float(quaternion[3])],'sxyz')
#                            Rx=math.degrees(angles[0])
#                            Ry=math.degrees(angles[1])
#                            Rz=math.degrees(angles[2])
#                            angulos=[Rx,Ry,Rz]
#                            target.write("Datos rotacion :" + str(angulos))
#                            target.write("\n")
#                            target.write("\n")
#                            listaInst.append(angulos) 
                            
          
       
#            listapuntos=[]
                 
    
#################################################################  

    def OnClose(self, evt):
        
        self.Close()  
        
#################################################################  

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None,"RobotTranslator por XF v0.1-alpha")
        self.SetTopWindow(frame)

        frame.Show(True)
        return True
        
app = MyApp(redirect=False)
app.MainLoop()
