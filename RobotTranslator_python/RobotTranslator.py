
import sys
import wx
import os
import math
import sqlite3
from library import dat 
from library import dat1
from library import transformations as tran
from wx.lib.wordwrap import wordwrap



#---------------------------------------------------------------------------
#searchListInst=["MoveJ","MoveL","MoveC","DispC","DispL","OcupaPortonJ","OcupaZonaJ","LiberaZonaJ","LiberaPortonJ","OcupaPortonL","OcupaZonaL","LiberaZonaL","LiberaPortonL"]

listaTools=[]
listaWobjs=[]
dbfilename=''
searchListInst=[]
moveJ=[]
moveL=[]
moveC=[]

sampleList = ['ABB'] 
sampleList1 = ['FANUC','KuKa']
sampleList2 = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','20']  

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
        
        
        self.SetBackgroundColour(wx.Colour(100,200,200))
        
        
        
        self.CreateStatusBar()
        self.SetStatusText("Barra de estado")
        
        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu 
     
        menu1 = wx.Menu()
        menu2 = wx.Menu()
        menu1.Append(101, "&ABB movimientos", "Configuracion de instrucciones de movimiento para ABB")
        menu2.Append(102, "&Acerca de...", "Acerca de...")
        menuBar.Append(menu1, "&Configurar")
        menuBar.Append(menu2, "&Info")
        
        self.SetMenuBar(menuBar)
        # Menu events
        self.Bind(wx.EVT_MENU_HIGHLIGHT_ALL, self.OnMenuHighlight)
        self.Bind(wx.EVT_MENU, self.Menu101, id=101)
        self.Bind(wx.EVT_MENU, self.Menu102, id=102)
        
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
        
        #self.stLine=wx.StaticLine(self, -1, (25, 50), (900,1))
        
        #############WOBJ & TOOL##########################
        self.addButton1=wx.Button(self, -1, u"A\xf1adir", (10,10))
        self.delButton1=wx.Button(self, -1, "Eliminar", (10,10))
        self.Bind(wx.EVT_BUTTON, self.OnAddWobj, self.addButton1)
        self.Bind(wx.EVT_BUTTON, self.OnDelWobj, self.delButton1)
        box4 = wx.FlexGridSizer(rows=0,cols=1, hgap=20, vgap=10) 
        box4.AddMany([self.addButton1,
                      self.delButton1])
        
        self.addButton2=wx.Button(self, -1, u"A\xf1adir", (10,10))
        self.delButton2=wx.Button(self, -1, "Eliminar", (10,10))
        self.Bind(wx.EVT_BUTTON, self.OnAddTool, self.addButton2)
        self.Bind(wx.EVT_BUTTON, self.OnDelTool, self.delButton2)
        box5 = wx.FlexGridSizer(rows=0,cols=1, hgap=20, vgap=10) 
        box5.AddMany([self.addButton2,
                      self.delButton2])
        
        self.l5=wx.StaticText(self, -1, "WORKOBJ")
        self.t5= wx.TextCtrl(self, -1, "",size=(200, -1))
        self.l6=wx.StaticText(self, -1, "USER FRAME")
        self.cb6 = wx.ComboBox(self, 500, sampleList2[0], (40, 40), 
                         (100, -1), sampleList2,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER
                         |wx.CB_READONLY 
                         )
        
        self.lb7 = wx.ListCtrl(self, -1,pos=(90, 90), size=(200, 90), style=wx.LC_REPORT)
        self.lb7.SetBackgroundColour(wx.WHITE)
        self.lb7.InsertColumn(0, 'WOBJ')
        self.lb7.InsertColumn(1, 'USER FRAME')
        self.lb7.SetColumnWidth(0,100)
        self.lb7.SetColumnWidth(1, 90)
        
        
        
        self.l8=wx.StaticText(self, -1, "TOOL")
        self.t8= wx.TextCtrl(self, -1, "",size=(200, -1))
        self.l9=wx.StaticText(self, -1, "USER TOOL")
        self.cb9 = wx.ComboBox(self, 500, sampleList2[0], (40, 40), 
                         (100, -1), sampleList2,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER
                         |wx.CB_READONLY 
                         )
        
        self.lb10 = wx.ListCtrl(self, -1,pos=(90, 90), size=(200, 90), style=wx.LC_REPORT)
        self.lb10.SetBackgroundColour(wx.WHITE)
        self.lb10.InsertColumn(0, 'TOOL')
        self.lb10.InsertColumn(1, 'USER TOOL')
        self.lb10.SetColumnWidth(0,100)
        self.lb10.SetColumnWidth(1, 90)
######################################################################
        self.ln = wx.StaticLine(self, -1,pos=wx.DefaultPosition, size=(650,-1), style=wx.LI_HORIZONTAL)
     
        
        box1 = wx.FlexGridSizer(rows=0,cols=5, hgap=30, vgap=5)
        box1.AddMany([self.cerrarButton,self.procesarButton,(0,0),(0,0),(0,0)]) 
        
        box2 = wx.FlexGridSizer(rows=0,cols=2, hgap=20, vgap=5) 
        box2.AddMany([self.l5,self.l6,
                      self.t5,self.cb6,
                     self.lb7,box4])
        
        box3 = wx.FlexGridSizer(rows=0,cols=2, hgap=20, vgap=5) 
        box3.AddMany([self.l8,self.l9,
                      self.t8,self.cb9,
                     self.lb10,box5])
        
        box4 = wx.FlexGridSizer(rows=0,cols=5, hgap=20, vgap=5) 
        box4.AddMany([self.l2,(0,0),(0,0),self.l4,(0,0),
                    self.t2,self.explorarButton,(0,0),self.t4,self.explorarButton2,
                    self.l3,(0,0),(0,0),(0,0),(0,0),
                    self.t3,self.explorarButton1,(0,0),(0,0),(0,0)])
        
        
      
######################################################################       
        box = wx.FlexGridSizer(rows=0,cols=5, hgap=20, vgap=5) 
        box.AddMany([self.cb,(0,0),(0,0),(0,0),(0,0),
                    self.l1,(0,0),(0,0),(0,0),(0,0),
                    self.cb1,(0,0),(0,0),(0,0),(0,0),
                    self.t1,self.chckb1,(0,0),box3,(0,0),
                    (0,0),(0,0),(0,0),box2,(0,0),
                    (0,0),(0,0),(0,0),(0,0),(0,0),
                    (0,0),(0,0),(0,0),(0,0),(0,0)])
        
        subMainSizer=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer.Add(box,1, wx.EXPAND | wx.ALL, 20)
        
        subMainSizer2=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer2.Add(box4,1, wx.EXPAND | wx.ALL, 20)
        
        subMainSizer3=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer3.Add(self.ln,1, wx.EXPAND | wx.ALL, 20)
        
        subMainSizer1=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer1.Add(box1,1, wx.EXPAND | wx.ALL, 20)
        
        MainSizer=wx.BoxSizer(wx.VERTICAL)
        MainSizer.Add(subMainSizer)
        MainSizer.Add(subMainSizer3)
        MainSizer.Add(subMainSizer2)
        MainSizer.Add(subMainSizer1)
        
        self.SetSizerAndFit(MainSizer)
        
        #################################
        self.l3.Enable(False)
        self.t3.Enable(False)
        self.explorarButton1.Enable(False)
        
        
        self.inicial()
        
        
    def OnAddTool (self, event):
        
        global dbfilename
        
        """Event handler for the button click."""
       
        dlg = wx.MessageDialog(self, u'\xbfQuiere a\xf1adir TOOL?',
                               'Alerta',
                               #wx.OK | wx.ICON_INFORMATION 
                               wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                               )

        result=dlg.ShowModal()
        dlg.Destroy() 
       
        if result==5103:
            ######data gathering###############
            tool=self.t8.GetValue()
            sel=self.cb9.GetSelection()
            ut=self.cb9.GetString(sel)
            insertData=(tool,ut)
                                   
            
            ###################################
            # create sqlite connection            
            conn = sqlite3.connect(dbfilename)
            c = conn.cursor()
           
            data=c.execute('SELECT * FROM tools ').fetchall()
        
            bOk=False
            for i in data:
                if (tool.lower() == str(i[0]).lower()) or (tool.upper() == str(i[0]).upper()):
                    bOk=True
              
            
            if not bOk==True and tool != '':
                               
                c.execute('INSERT INTO tools VALUES(?,?)',insertData)
                conn.commit()                  
                # close connection
                c.close()
                
            elif tool == '':
                dlg = wx.MessageDialog(self, 'Campo tool no puede estar vacio!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                dlg.ShowModal()
                dlg.Destroy()
                
            else:
                dlg = wx.MessageDialog(self, 'Tool existente, elija otra!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                dlg.ShowModal()
                dlg.Destroy()
            c.close()
            self.readTable()
            
    def OnDelTool(self, event):
        global dbfilename
        index = self.lb10.GetFirstSelected()
        if index!=-1:
            dlg = wx.MessageDialog(self, u'\xbfQuiere eliminar el tool?',
                           'Alerta',
                           #wx.OK | wx.ICON_INFORMATION 
                           wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                           )

            result=dlg.ShowModal()
            dlg.Destroy() 
            if result==5103:
                
                data = self.lb10.GetItemText(index)
                conn = sqlite3.connect(dbfilename)
                c = conn.cursor()
                c.execute("""DELETE  FROM tools WHERE tool = ? """,(data,))
                conn.commit()                  
                # close connection
                c.close()
                self.lb10.DeleteItem(index)
                
        else:
            dlg = wx.MessageDialog(self, u'Seleccion\xe9 linea!',
                           'Mensaje',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
            dlg.ShowModal()
            dlg.Destroy()
        c.close()
        self.readTable()
    
    def OnAddWobj (self, event):
        
        global dbfilename
        
        """Event handler for the button click."""
       
        dlg = wx.MessageDialog(self, u'\xbfQuiere a\xf1adir Wobj?',
                               'Alerta',
                               #wx.OK | wx.ICON_INFORMATION 
                               wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                               )

        result=dlg.ShowModal()
        dlg.Destroy() 
        
        if result==5103:
            ######data gathering###############
            wobj=self.t5.GetValue()
            sel=self.cb6.GetSelection()
            uf=self.cb6.GetString(sel)
            insertData=(wobj,uf)
                                   
            
            ###################################
            # create sqlite connection            
            conn = sqlite3.connect(dbfilename)
            c = conn.cursor()
           
            data=c.execute('SELECT * FROM wobjs ').fetchall()
        
            bOk=False
            for i in data:
                if (wobj.lower() == str(i[0]).lower()) or (wobj.upper() == str(i[0]).upper()):
                    bOk=True
              
            
            if not bOk==True and wobj != '':
                               
                c.execute('INSERT INTO wobjs VALUES(?,?)',insertData)
                conn.commit()                  
                # close connection
                c.close()
                
            elif wobj == '':
                dlg = wx.MessageDialog(self, 'Campo wobj no puede estar vacio!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                dlg.ShowModal()
                dlg.Destroy()
                
            else:
                dlg = wx.MessageDialog(self, 'Wobj existente, elija otra!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                dlg.ShowModal()
                dlg.Destroy()
            c.close()
            self.readTable()
            
    def OnDelWobj(self, event):
        global dbfilename
        index = self.lb7.GetFirstSelected()
        if index!=-1:
            dlg = wx.MessageDialog(self, u'\xbfQuiere eliminar el wobj?',
                           'Alerta',
                           #wx.OK | wx.ICON_INFORMATION 
                           wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                           )

            result=dlg.ShowModal()
            dlg.Destroy() 
            if result==5103:
                
                data = self.lb7.GetItemText(index)
                conn = sqlite3.connect(dbfilename)
                c = conn.cursor()
                c.execute("""DELETE  FROM wobjs WHERE wobj = ? """,(data,))
                conn.commit()                  
                # close connection
                c.close()
                self.lb7.DeleteItem(index)
                
        else:
            dlg = wx.MessageDialog(self, u'Seleccion\xe9 linea!',
                           'Mensaje',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
            dlg.ShowModal()
            dlg.Destroy()
        c.close()
        self.readTable()
        
        
    def readTable (self):
        global dbfilename
        listTools=dict({'TOOL':'', 'UT':''})
        listWobjs=dict({'WOBJ':'', 'UF':''})
        
        self.lb10.DeleteAllItems()
        self.lb7.DeleteAllItems()
        ###################################
        # create sqlite connection            
        conn = sqlite3.connect(dbfilename)
        c = conn.cursor()
       
        data=c.execute('SELECT * FROM tools ').fetchall()
        data1=c.execute('SELECT * FROM wobjs ').fetchall()
        # close connection
        c.close()
        
        index=0
        for i in data:
            #loop through and add it
            self.lb10.InsertStringItem(index,str(i[0]))
            self.lb10.SetStringItem(index,1,str(i[1]))
            index = index + 1  
            
        index=0
        for i in data1:
            #loop through and add it
            self.lb7.InsertStringItem(index,str(i[0]))
            self.lb7.SetStringItem(index,1,str(i[1]))
            index = index + 1 
        
        for i in data:
           
            listTools['TOOL']=(str(i[0]))
            print listTools['TOOL']
            listTools['UT']=(str(i[1]))
            print listTools['UT']
           
            listaTools.append(listTools.copy())
      
            
        for i in data1:
           
            listWobjs['WOBJ']=(str(i[0]))
            listWobjs['UF']=(str(i[1]))
            
            listaWobjs.append(listWobjs.copy())
            
        print listaTools    
        
        
    def inicial(self):
        global dbfilename
       
        
        dbfilename=os.path.abspath("RobotTranslator.exe")
      
        dbfilename=dbfilename.replace("RobotTranslator.exe","RBT.db")
        
        if not os.path.isfile(dbfilename):
            
            conn = sqlite3.connect(dbfilename)
            c = conn.cursor()
            # Create table
            c.execute('''CREATE TABLE instrucciones(instruccion text, movimiento text)''')
            c.execute('''CREATE TABLE tools(tool text, userTool text)''')
            c.execute('''CREATE TABLE wobjs(wobj text, userWobj text)''')
        
            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
            conn.close()
            self.readTable()
            
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
           
                
            self.readTable()
      
        
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
        
        
    def Menu102(self, event):
        # First we create and fill the info object
        licenseText="Licencia LGPL"
        info = wx.AboutDialogInfo()
        info.Name = "RobotTranslator"
        info.Version = "1.0"
        info.Copyright = "(C) 2014 Xabier Fernandez"
        info.Description = wordwrap(
            "The \"Robot Translator\" program is a software program that allows you "
            "to translate programs from ABB industrial robot to Fanuc or Kuka robots"
             
            "\n\nAt the moment this piece of software is in its testing phase "
            "of development. Our goal is to incorporate more capabilities  "
            "and more brands of robots as we go along with its development "
            "The development of this software has been done using the \"Wxpython\" libraries "
            "and \"Editra\", which it's the editor that comes bundled with \"Wxpython\"",
            350, wx.ClientDC(self))
            
        info.WebSite = ("http://www.armrobotics.com/", "ARM Robotics S.L. home page")
        info.Developers = [ "Xabier Fernandez Gutierrez" ]

        info.License = wordwrap(licenseText, 500, wx.ClientDC(self))

        # Then we call wx.AboutBox giving it that info object
        wx.AboutBox(info)
       
        
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
                inst =dict({'MOVE':'', 'POINT':'', 'POINT1':'', 'Tx':'', 'Ty':'', 'Tz':'','Rx':'','Ry':'','Rz':'','Tx1':'', 'Ty1':'', 'Tz1':'','Rx1':'','Ry1':'','Rz1':'','EXTJ':'','EXTJ1':'','UT':'','UF':''})
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
                        
                        if linea.lower().find('home')==-1:
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
                                
                                inst['UT']=self.searchTool(linea)
                                inst['UF']=self.searchWobj(linea)
                            #################################################    
                            
                    
#################################################################################
                            if inst['MOVE']!='C':
                                
                                for point in range(0,len(listaPuntos)):
                                    if linea.find(listaPuntos[point])!=-1:
                                        inst['POINT']= listaPuntos[point]
                                
                                
                                angulos=self.searchAngles(inst['POINT'])
                                inst['Rx']=angulos[0]
                                inst['Ry']=angulos[1]
                                inst['Rz']=angulos[2]
                                
                                trans=self.searchTrans(inst['POINT'])
                                inst['Tx']=trans[0]
                                inst['Ty']=trans[1]
                                inst['Tz']=trans[2]
                                
                                inst['EXTJ']=self.searchEXTJ(inst['POINT'])
                                
                                inst['UT']=self.searchTool(linea)
                                inst['UF']=self.searchWobj(linea)
                                    
                                    
                       
                        else:
                            inst['MOVE']=self.searchMove(linea)
                            if inst['MOVE']!='C':
                                
                                inst['POINT']='HOME'
                                    
                                inst['Rx']='0.0'
                                inst['Ry']='0.0'
                                inst['Rz']='0.0'
                        
                                inst['Tx']='0.0'
                                inst['Ty']='0.0'
                                inst['Tz']='0.0'
                                
                                inst['EXTJ']='0.0'
                                
                                inst['UT']=self.searchTool(linea)
                                inst['UF']=self.searchWobj(linea)
                            
                                                        
                                
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
        
        if self.cb1.GetValue()=='FANUC':
            target=open(self.t4.GetValue()+ '\\' + fileName + ".PE",'w')
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
                    tool=dictionary['UT']
                    wobj=dictionary['UF']
                    
                    target.write( dat.POSDAT.format(count,punto,tx,ty,tz,rz,ry,rx,extj,wobj,tool))
                    count=count+1
                    punto=dictionary['POINT1']
                    tx=dictionary['Tx1']
                    ty=dictionary['Ty1']
                    tz=dictionary['Tz1']
                    rz=dictionary['Rz1']
                    ry=dictionary['Ry1']
                    rx=dictionary['Rx1']
                    extj=dictionary['EXTJ1']
                    tool=dictionary['UT']
                    wobj=dictionary['UF']
                    target.write( dat.POSDAT.format(count,punto,tx,ty,tz,rz,ry,rx,extj,wobj,tool))
            
                else:
                    punto=dictionary['POINT']
                    tx=dictionary['Tx']
                    ty=dictionary['Ty']
                    tz=dictionary['Tz']
                    rz=dictionary['Rz']
                    ry=dictionary['Ry']
                    rx=dictionary['Rx']
                    extj=dictionary['EXTJ']
                    tool=dictionary['UT']
                    wobj=dictionary['UF']
                    
                    target.write( dat.POSDAT.format(count,punto,tx,ty,tz,rz,ry,rx,extj,wobj,tool))
                
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
            print 'fanuc'
####################################################################################            
        if self.cb1.GetValue()=='KuKa':
            target=open(self.t4.GetValue()+ '\\' + fileName + ".src",'w')
            target1=open(self.t4.GetValue()+ '\\' + fileName + ".dat",'w')
            
            #headers
            target.write( dat1.HeaderSrc)
            target.write( dat1.DeclSrc.format(fileName))
            target1.write( dat1.HeaderDat.format(fileName))
            
            for i in range(0,len(list)):
                    #Contadores inicializar
                 
                    #Get Dictionaries
                    dictionary=list[i]
                    move=dictionary['MOVE']
                    punto=dictionary['POINT']
                    tx=dictionary['Tx']
                    ty=dictionary['Ty']
                    tz=dictionary['Tz']
                    rz=dictionary['Rz']
                    ry=dictionary['Ry']
                    rx=dictionary['Rx']
                    extj=dictionary['EXTJ']
                    punto1=dictionary['POINT1']
                    tx1=dictionary['Tx1']
                    ty1=dictionary['Ty1']
                    tz1=dictionary['Tz1']
                    rz1=dictionary['Rz1']
                    ry1=dictionary['Ry1']
                    rx1=dictionary['Rx1']
                    extj1=dictionary['EXTJ1']
                    tool=dictionary['UT']
                    wobj=dictionary['UF']
                    
                    if punto!="HOME":
                        if move=='J':
                            target.write( dat1.PTP.format(punto,tool,wobj))
                            target1.write( dat1.PTP_dat.format(punto,tx,ty,tz,rz,ry,rx,extj,tool,wobj))
                        if move=='L':
                            target.write( dat1.LIN.format(punto,tool,wobj))
                            target1.write( dat1.LIN_dat.format(punto,tx,ty,tz,rz,ry,rx,extj,tool,wobj))
                        if move=='C':
                            target.write( dat1.CIRC.format(punto,punto1,tool,wobj))
                            target1.write( dat1.CIRC_dat.format(punto,tx,ty,tz,rz,ry,rx,extj))
                            target1.write( dat1.CIRC_dat1.format(punto1,tx1,ty1,tz1,rz1,ry1,rx1,extj1,tool,wobj))
                    else:
                
                        target.write( dat1.PTPHOME)
                          
                        
            #################
            target.write(dat1.FootSrc)
            target1.write(dat1.FootDat)
           
            target.close()
            target1.close()
           
            print 'kuka'
            
        
   
#################################################################     
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

    def searchTool(self,linea): 
        listaTools
       
       
        linea =linea.replace("\\",",")
       
        ut='0'
        
        for i in range(0,len(listaTools)):
            tool=listaTools[i]
           
            search=linea.find(tool['TOOL'].strip())
            if search!=-1:
                ut=tool['UT']
      
        return ut
        
    def searchWobj(self,linea): 
       
        linea =linea.replace("\\",",")
      
        uf='0'
        
        for i in range(0,len(listaWobjs)):
            wobj=listaWobjs[i]
            search=linea.find(wobj['WOBJ'].strip())
            if search!=-1:
                uf=wobj['UF']
    
        return uf
        
        
 
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
             
        sampleList1=['C','L','J']
        
        self.l1=wx.StaticText(self, -1,"Instruccion",(10,5),size=wx.DefaultSize)
        self.t1= wx.TextCtrl(self, -1, "",(10,30),size=(300, -1),style=wx.TE_PROCESS_ENTER)
        
        self.l1=wx.StaticText(self, -1,"Lista de instrucciones",(110,70),size=wx.DefaultSize)
        self.lb1 = wx.ListCtrl(self, -1,pos=(90, 90), size=(275, 300), style=wx.LC_REPORT)
        self.lb1.SetBackgroundColour(wx.WHITE)
        self.lb1.InsertColumn(0, 'Instruccion')
        self.lb1.InsertColumn(1, 'Tipo movimiento')
        self.lb1.SetColumnWidth(0,100)
        self.lb1.SetColumnWidth(1, 100)
            
        self.rb = wx.RadioBox( self, wx.ID_ANY, u"Tipo",(10,90), 
                              wx.DefaultSize, sampleList1, 1, wx.RA_SPECIFY_COLS )
        self.addButton=wx.Button(self, -1, u"A\xf1adir", (375,90))
        self.Bind(wx.EVT_BUTTON, self.OnAdd, self.addButton)
        self.delButton=wx.Button(self, -1, u"Eliminar", (375,130))
        self.Bind(wx.EVT_BUTTON, self.OnDel, self.delButton)
 #################################################################### 
        self.readTable()
                  
 ####################################################################
    
    def readTable (self):
        global dbfilename
        self.lb1.DeleteAllItems()
        ###################################
        # create sqlite connection            
        conn = sqlite3.connect(dbfilename)
        c = conn.cursor()
       
        data=c.execute('SELECT * FROM instrucciones ').fetchall()
        # close connection
        c.close()
        
        index=0
        for i in data:
            #loop through and add it
            self.lb1.InsertStringItem(index,str(i[0]))
            self.lb1.SetStringItem(index,1,str(i[1]))
            index = index + 1  
        
        
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
        
        if result==5103:
            ######data gathering###############
            inst=self.t1.GetValue()
            typeMove=self.rb.GetStringSelection()
            insertData=(inst,typeMove)
                                   
            
            ###################################
            # create sqlite connection            
            conn = sqlite3.connect(dbfilename)
            c = conn.cursor()
           
            data=c.execute('SELECT * FROM instrucciones ').fetchall()
        
            bOk=False
            for i in data:
                if (inst.lower() == str(i[0]).lower()) or (inst.upper() == str(i[0]).upper()):
                    bOk=True
              
            
            if not bOk==True and inst != '':
                               
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
            self.readTable()
    def OnDel(self, event):
        global dbfilename
        index = self.lb1.GetFirstSelected()
        if index!=-1:
            dlg = wx.MessageDialog(self, u'\xbfQuiere eliminar la instruccion?',
                           'Alerta',
                           #wx.OK | wx.ICON_INFORMATION 
                           wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                           )
            
            result=dlg.ShowModal()
            dlg.Destroy() 
            if result==5103:
                
                data = self.lb1.GetItemText(index)
                conn = sqlite3.connect(dbfilename)
                c = conn.cursor()
                c.execute("""DELETE  FROM instrucciones WHERE instruccion = ? """,(data,))
                conn.commit()                  
                # close connection
                c.close()
                self.lb1.DeleteItem(index)
                
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
        frame = MyFrame(None,"RobotTranslator por XF v1.0-alpha")
        
        self.SetTopWindow(frame)
        frame.CenterOnScreen()

        frame.Show(True)
        return True
        
app = MyApp(redirect=False)
app.MainLoop()
