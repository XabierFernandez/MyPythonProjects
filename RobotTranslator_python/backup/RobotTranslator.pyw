
import sys
import wx
import os
import math
import sqlite3
from library import dat 
from library import transformations as tran



#---------------------------------------------------------------------------
#searchListInst=["MoveJ","MoveL","MoveC","DispC","DispL","OcupaPortonJ","OcupaZonaJ","LiberaZonaJ","LiberaPortonJ","OcupaPortonL","OcupaZonaL","LiberaZonaL","LiberaPortonL"]
dbfilename=''
searchListInst=[]
moveJ=[]
moveL=[]
moveC=[]
#moveJ=["MoveJ","OcupaPortonJ","OcupaZonaJ","LiberaZonaJ","LiberaPortonJ"]
#moveL=["MoveL","DispL","OcupaPortonL","OcupaZonaL","LiberaZonaL","LiberaPortonL"]
#moveC=["DispC","MoveC"]
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
        
        self.inicial()
        
        self.CreateStatusBar()
        self.SetStatusText("Barra de estado")
        
        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu 
     
        menu1 = wx.Menu()
        menu1.Append(101, "&ABB movimientos", "Configuracion de instrucciones de movimiento para ABB")
        menuBar.Append(menu1, "&Configurar")
        self.SetMenuBar(menuBar)
        # Menu events
        self.Bind(wx.EVT_MENU_HIGHLIGHT_ALL, self.OnMenuHighlight)
        self.Bind(wx.EVT_MENU, self.Menu101, id=101)
        
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
        
    def inicial(self):
        global dbfilename
        
        dbfilename=os.path.abspath("RobotTranslator.exe")
        print dbfilename
        dbfilename=dbfilename.replace("RobotTranslator.exe","RBT.db")
        
        if not os.path.isfile(dbfilename):
            
            conn = sqlite3.connect(dbfilename)
            c = conn.cursor()
            # Create table
            c.execute('''CREATE TABLE instrucciones(instruccion text, movimiento text)''')
        
            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
            conn.close()
        else:
            ###################################
            # create sqlite connection            
            conn = sqlite3.connect(dbfilename)
            c = conn.cursor()
           
            data=c.execute('SELECT * FROM instrucciones ').fetchall()
            # close connection
            c.close()
            for i in data:
                
                if str(i[1])=='J':
                    moveJ.append(str(i[0]))
                if str(i[1])=='L':
                    moveL.append(str(i[0]))
                if str(i[1])=='C':
                    moveC.append(str(i[0]))
                searchListInst.append(str(i[0]))
            
        
    def OnMenuHighlight(self, event):
        # Show how to get menu item info from this event handler
        id = event.GetMenuId()
        item = self.GetMenuBar().FindItemById(id)
        if item:
            text = item.GetText()
            help = item.GetHelp()

        # but in this case just call Skip so the default is done
        event.Skip() 
        
    def Menu101(self, event):
        dlg = ConfigDialog(self, -1, u"Instrucciones de movimiento", size=(500, 500),
                         #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                         style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                         useMetal=False,
                         )
        dlg.CenterOnScreen()

        # this does not return until the dialog is closed.
        val = dlg.ShowModal()
    
        if val == wx.ID_OK:
            print ''
            
        else:
           print ''
            

        dlg.Destroy()
       
        
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
##################################################################################
                listaInst=[]
                fileName=''
                inst =dict({'MOVE':'', 'POINT':'', 'POINT1':'', 'Tx':'', 'Ty':'', 'Tz':'','Rx':'','Ry':'','Rz':'','Tx1':'', 'Ty1':'', 'Tz1':'','Rx1':'','Ry1':'','Rz1':'','EXTJ':'','EXTJ1':''})
                file = open(self.t2.GetValue()).readlines()
                #Lista con Robtarget
                listaPuntos=self.listPoints()
                #Lista con Procedimientos
                listaProc=self.searchProc(file)
                #Lista con instrucciones separadas por Procedimientos
                listaInstProc=self.searchPointsProc(file,listaProc)
                
                for i in range(0,len(listaInstProc)):
                    fileName=listaInstProc[i][0]
                    
                    
                    for j in range(1,len(listaInstProc[i])):
                        linea=listaInstProc[i][j]
            
                        inst['MOVE']=self.searchMove(linea)
                        
                        if inst['MOVE']=='C':
                            pointC=[]
                            for point in range(0,len(listaPuntos)):
                                if linea.find(listaPuntos[point])!=-1:
                                    pointC.append(listaPuntos[point])
                                    
                            if linea.find(pointC[0])< linea.find(pointC[1]): 
                                inst['POINT']= pointC[0]  
                                inst['POINT1']= pointC[1] 
                            if linea.find(pointC[0])> linea.find(pointC[1]): 
                                inst['POINT']= pointC[1]  
                                inst['POINT1']= pointC[0] 
                                
                            angulos=self.searchAngles(inst['POINT'])
                            inst['Rx']=angulos[0]
                            inst['Ry']=angulos[1]
                            inst['Rz']=angulos[2]
                            
                            trans=self.searchTrans(inst['POINT'])
                            inst['Tx']=trans[0]
                            inst['Ty']=trans[1]
                            inst['Tz']=trans[2]
                        #################################################
                            angulos1=self.searchAngles(inst['POINT1'])
                            inst['Rx1']=angulos1[0]
                            inst['Ry1']=angulos1[1]
                            inst['Rz1']=angulos1[2]
                            
                            trans1=self.searchTrans(inst['POINT1'])
                            inst['Tx1']=trans1[0]
                            inst['Ty1']=trans1[1]
                            inst['Tz1']=trans1[2]
                            
                            inst['EXTJ']=self.searchEXTJ(inst['POINT'])
                            inst['EXTJ1']=self.searchEXTJ(inst['POINT1'])
                        
                    
#################################################################################
                        if inst['MOVE']!='C':
                            
                            for point in range(0,len(listaPuntos)):
                                if linea.find(listaPuntos[point])!=-1:
                                    inst['POINT']= listaPuntos[point]
                            
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
                    #Punto en el que se escribe los datos en el archivo
                 
                    self.writeToFile(listaInst,fileName)
                
               
               
             
##################################################################################
               
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
    def writeToFile(self,list,fileName): 
        target=open(self.t4.GetValue()+ '\\' + fileName+".PE",'w')
        lineasCount=0
        count=0
        count1=0
       
        for i in range(0,len(list)):
                #Contadores inicializar
                
               
                count=count+1
                count1=count1+1
                #Get Dictionaries
                dictionary=list[i]
                move=dictionary['MOVE']
                
                if move=='J':
                    target.write( dat.POSJ.format(count,move,count1))
                if move=='L':
                    target.write( dat.POSL.format(count,move,count1))
                if move=='C':
                    target.write( dat.POSC.format(count,move,count1))
                    count1=count1+1
                    target.write( dat.POSC1.format(count1))
                    
        
        lineasCount=count
                
        count=0
        target.write(dat.HeaderPOSDAT)
        for j in range(0,len(list)):
            dictionary=list[j]
            count=count+1
            if dictionary['MOVE']=='C':
              
                dictionary=list[j]
                punto=dictionary['POINT']
                tx=dictionary['Tx']
                ty=dictionary['Ty']
                tz=dictionary['Tz']
                rz=dictionary['Rz']
                ry=dictionary['Ry']
                rx=dictionary['Rx']
                extj=dictionary['EXTJ']
                
                target.write( dat.POSDAT.format(count,punto,tx,ty,tz,rx,ry,rz,extj))
                count=count+1
                punto=dictionary['POINT1']
                tx=dictionary['Tx1']
                ty=dictionary['Ty1']
                tz=dictionary['Tz1']
                rz=dictionary['Rz1']
                ry=dictionary['Ry1']
                rx=dictionary['Rx1']
                extj=dictionary['EXTJ1']
                target.write( dat.POSDAT.format(count,punto,tx,ty,tz,rx,ry,rz,extj))
        
            else:
                punto=dictionary['POINT']
                tx=dictionary['Tx']
                ty=dictionary['Ty']
                tz=dictionary['Tz']
                rz=dictionary['Rz']
                ry=dictionary['Ry']
                rx=dictionary['Rx']
                extj=dictionary['EXTJ']
                
                target.write( dat.POSDAT.format(count,punto,tx,ty,tz,rx,ry,rz,extj))
            
        target.write( dat.FooterDAT)
        target.close()
        # read the current contents of the file 
        f = open(self.t4.GetValue()+ '\\' +fileName+".PE",'r')
        text = f.read() 
        f.close() 
        # open the file again for writing 
        f = open(self.t4.GetValue()+ '\\' + fileName+".PE",'w')
        f.write(dat.HeaderPE.format(fileName,lineasCount)) 
        # write the original contents 
        f.write(text) 
        f.close() 
        
   
                
                
            
    
    def getInstListProc(self, file):
        listaInst=[]
        inst =dict({'MOVE':'', 'POINT':'', 'POINT1':'', 'Tx':'', 'Ty':'', 'Tz':'','Rx':'','Ry':'','Rz':'','EXTJ':''})
        listInst=self.getListProc(file)
        
        
      
        
        for i in range (0,len(listInst)):
            if len(listInst[i])>1:
                listaInst.append(listInst[i][0]+'==========')
               
                for j in range(1,len(listInst[i])):
                
                    inst['MOVE']=self.searchMove(listInst[i][j])
                    if inst['MOVE']!='C':
                        inst['POINT']=self.searchPoint(listInst[i][j])
                        punto=inst['POINT'].lower()
                    else:
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
    def listPoints(self): 
        lista=[]
        if self.chckb1.IsChecked():
            file = open(self.t3.GetValue()).readlines()
            file1 = open(self.t3.GetValue()).readlines()
            
            for i in range(0,len(file)):
                search=file[i].find("robtarget")
                search1=file[i].find("CONST")
                search2=file[i].find(":")
                
                
                if search!=-1 and search1!=-1 and search2!=-1 :
                    punto=file[i][search+10:search2]
                    punto=punto.strip()
                    lista.append(punto)
                    
            for i in range(0,len(file1)):
                search=file1[i].find("robtarget")
                search1=file1[i].find("CONST")
                search2=file1[i].find(":")
                
                
                if search!=-1 and search1!=-1 and search2!=-1 :
                    punto=file1[i][search+10:search2]
                    punto=punto.strip()
                    lista.append(punto)
                    
        else:
            file = open(self.t2.GetValue()).readlines()
        
        
            for i in range(0,len(file)):
                search=file[i].find("robtarget")
                search1=file[i].find("CONST")
                search2=file[i].find(":")
                
                
                if search!=-1 and search1!=-1 and search2!=-1 :
                    punto=file[i][search+10:search2]
                    punto=punto.strip()
                    lista.append(punto)
        
        return lista
        
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
        lista=self.listPoints()
        punto="" 
        for i in range(0,len(lista)):
            search=linea.find(lista[i]) 
            
                   
            if search!=-1:
                
                punto=lista[i]
            
                
        search1=linea.lower().find("home")
        if search1!=-1:
            punto="HOME"
            
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

            if linea.find(searchListInst[term])!=-1 and linea.strip().find('!')!=0 :
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

    def OnClose(self, evt):
        
        self.Close()  
        
################################################################# 

class ConfigDialog(wx.Dialog):
   
   
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition, 
            style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,
            useMetal=False,
            ):
                
        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        # This next step is the most important, it turns this Python
        # object into the real wrapper of the dialog (instead of pre)
        # as far as the wxPython extension is concerned.
        self.PostCreate(pre)
        
        
        data = self.readTable()
        
        samplelist=[]
        for i in data:
            
            s = str(i[0]) +' ==> '+ str(i[1])
            samplelist.append(s)
        ###################################
        
               
     
        sampleList1=['C','L','J']
        
        self.l1=wx.StaticText(self, -1,"Instruccion",(10,5),size=wx.DefaultSize)
        self.t1= wx.TextCtrl(self, -1, "",(10,30),size=(300, -1),style=wx.TE_PROCESS_ENTER)
        
        self.l1=wx.StaticText(self, -1,"Lista de instrucciones",(110,70),size=wx.DefaultSize)
        self.lb1 = wx.ListBox(self, 26, (110, 90), (200, 300), samplelist, wx.LB_SINGLE)
        self.rb = wx.RadioBox( self, wx.ID_ANY, u"Tipo",(10,90), 
                              wx.DefaultSize, sampleList1, 1, wx.RA_SPECIFY_COLS )
        self.addButton=wx.Button(self, -1, u"A\xf1adir", (375,90))
        self.Bind(wx.EVT_BUTTON, self.OnAdd, self.addButton)
        self.delButton=wx.Button(self, -1, u"Eliminar", (375,130))
        self.Bind(wx.EVT_BUTTON, self.OnDel, self.delButton)
    
    def readTable (self):
        global dbfilename
        ###################################
        # create sqlite connection            
        conn = sqlite3.connect(dbfilename)
        c = conn.cursor()
       
        data=c.execute('SELECT * FROM instrucciones ').fetchall()
        # close connection
        c.close()
        
        return data
        
        
    def OnAdd (self, event):
        
        global dbfilename
        
        """Event handler for the button click."""
       
        dlg = wx.MessageDialog(self, u'\xbfQuiere a\xf1adir instruccion?',
                               'Alerta',
                               #wx.OK | wx.ICON_INFORMATION 
                               wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                               )

        result=dlg.ShowModal()
        dlg.Destroy() 
        print result
        if result==5103:
            ######data gathering###############
            inst=self.t1.GetValue()
            typeMove=self.rb.GetStringSelection()
            string=inst+' ==> '+ typeMove 
            
                                      
            
            ###################################
            # create sqlite connection            
            conn = sqlite3.connect(dbfilename)
            c = conn.cursor()
           
            data=c.execute('SELECT * FROM instrucciones ').fetchall()
            index=0
            bOk=False
            for i in data:
                if (inst.lower() == str(i[0]).lower()) or (inst.upper() == str(i[0]).upper()):
                    bOk=True
                index = index + 1  
            
            if not bOk==True and inst != '':
                # insert a row
                self.lb1.Insert(string,0)
                insertData=(inst,typeMove)
                
                c.execute('INSERT INTO instrucciones VALUES(?,?)',insertData)
                conn.commit()                  
                # close connection
                c.close()
                
            elif inst == '':
                dlg = wx.MessageDialog(self, 'Campo Instruccion no puede estar vacio!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                dlg.ShowModal()
                dlg.Destroy()
                
            else:
                dlg = wx.MessageDialog(self, 'Instruccion existente, elija otra!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                dlg.ShowModal()
                dlg.Destroy()
            c.close()
    def OnDel(self, event):
        global dbfilename
        index = self.lb1.GetSelection()
        if index!=-1:
            dlg = wx.MessageDialog(self, u'\xbfQuiere eliminar la instruccion?',
                           'Alerta',
                           #wx.OK | wx.ICON_INFORMATION 
                           wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                           )

            result=dlg.ShowModal()
            dlg.Destroy() 
            if result==5103:
                
                text = self.lb1.GetString(index)
                search=text.find(' ==> ')
                text=text[0:search]
                
                data = text
                conn = sqlite3.connect(dbfilename)
                c = conn.cursor()
                c.execute("""DELETE  FROM instrucciones WHERE instruccion = ? """,(data,))
                conn.commit()                  
                # close connection
                c.close()
                self.lb1.Delete(index)
                
        else:
            dlg = wx.MessageDialog(self, u'Seleccion\xe9 linea!',
                           'Mensaje',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
            dlg.ShowModal()
            dlg.Destroy()
        c.close()
      

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None,"RobotTranslator por XF v0.1-alpha")
        self.SetTopWindow(frame)

        frame.Show(True)
        return True
        
app = MyApp(redirect=False)
app.MainLoop()
