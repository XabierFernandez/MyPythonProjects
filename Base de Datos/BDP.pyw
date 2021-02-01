#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#----------------------------------------------------------------------
# A very simple wxPython example.  Just a wx.Frame, wx.Panel,
# wx.StaticText, wx.Button, and a wx.BoxSizer, but it shows the basic
# structure of any wxPython application.
#----------------------------------------------------------------------
 
import wx
import time
import os
import sqlite3
import datetime
import subprocess

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "All files (*.*)|*.*"
robotsList = ['KuKa', 'Fanuc', 'ABB', 'Motoman', 'Staubli', 'Kawasaki']
stateList = ['En curso', 'Finalizado']
tipoList = ['Programacion', 'Instalacion','Mantenimiento']
searchList = ['numProyect','stateProyect' ,'tipoProyect' ,'fechaIniProyect' ,'cliente' ,'fabrica' ,'direccion' ,'codePostal' ,'phone' ,'email' ,'responsable' ,'robots', 'descripcion']
searchList1 = ['Numero de Proyecto','Estado' ,'Tipo de proyecto' ,'Fecha Inicio de proyecto' ,'Cliente' ,'Fabrica' ,'Direccion' ,'Codigo Postal' ,'Telefono' ,'Email' ,'Responsable' ,'Robots', 'Descripcion']




class MyFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """    
    def __init__(self, parent, title):
            
        wx.Frame.__init__(self, parent, -1, title,
                          pos=(100, 10), style= wx.SYSTEM_MENU | wx.CAPTION |wx.MINIMIZE_BOX| wx.CLOSE_BOX)
        
        self.icon = wx.Icon('BDP.ico', wx.BITMAP_TYPE_ICO, 32,32)
        self.SetIcon(self.icon)
        
        
        
        self.SetBackgroundColour(wx.Colour(100,200,200))
       
        self.inicial()
       
        # Create the menubar
        menuBar = wx.MenuBar()

        # and a menu 
        menu = wx.Menu()

        # add an item to the menu, using \tKeyName automatically
        # creates an accelerator, the third param is some help text
        # that will show up in the statusbar
        menu.Append(wx.ID_EXIT, "&Salir\tAlt-S", "Abandonar BDP")

        # bind the menu event to an event handler
        self.Bind(wx.EVT_MENU, self.OnTimeToClose, id=wx.ID_EXIT)

        # and put the menu on the menubar
        menuBar.Append(menu, "&Archivo")
        self.SetMenuBar(menuBar)

        self.CreateStatusBar()
        
 ###--Buttons--##############################################################
    
        self.mostrarButton=wx.Button(self, -1, "Mostrar", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnShow, self.mostrarButton)
        self.eliminarButton=wx.Button(self, -1, "Eliminar", (50,50))
        self.Bind(wx.EVT_BUTTON, self.eliminar, self.eliminarButton)
        self.nuevoButton=wx.Button(self, -1, "Nuevo", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnAdd, self.nuevoButton)
        self.editButton=wx.Button(self, -1, "Editar", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnEdit, self.editButton)
        
        self.search = wx.SearchCtrl(self, size=(200,-1), style=wx.TE_PROCESS_ENTER)
        self.search.ShowSearchButton(True)
        self.search.ShowCancelButton(True)
        self.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnDoSearch, self.search)
        self.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.OnCancel, self.search)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnDoSearch, self.search)
        
        self.searchProyectCtrl= wx.ComboBox(self, 500, searchList1[0], (90, 50), 
                         (160, -1), searchList1,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER 
                         | wx.CB_READONLY             
                         )
       
        
        
######################################################################
        #row1 and col2
        l15=wx.StaticText(self, -1, "Proyectos:")
        self.proyectsCtrl= wx.ListCtrl(self, -1,pos=(10,10), size=(704,400), style=wx.LC_REPORT)
        self.proyectsCtrl.SetBackgroundColour(wx.WHITE)
        self.proyectsCtrl.InsertColumn(0, 'Numero de Proyecto')
        self.proyectsCtrl.InsertColumn(1, 'Estado del Proyecto')
        self.proyectsCtrl.InsertColumn(2, 'Tipo de proyecto')
        self.proyectsCtrl.InsertColumn(3, 'Cliente')
        self.proyectsCtrl.InsertColumn(4, 'Fabrica')
        self.proyectsCtrl.SetColumnWidth(0,140)
        self.proyectsCtrl.SetColumnWidth(1, 140)
        self.proyectsCtrl.SetColumnWidth(2, 140)
        self.proyectsCtrl.SetColumnWidth(3, 140)
        self.proyectsCtrl.SetColumnWidth(4, 140)
        #self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnSelect, self.proyectsCtrl)

        sizer= wx.FlexGridSizer(rows=0,cols=2, hgap=5, vgap=5)        
        sizer.AddMany([l15,self.proyectsCtrl,
                       (0,0),self.search, 
                       (0,0),self.searchProyectCtrl,                      
                       ])
        
        sizer1= wx.FlexGridSizer(rows=0,cols=1, hgap=5, vgap=5)
        sizer1.AddMany([self.mostrarButton,
                        (0,0),(0,0),(0,0),(0,0),(0,0),
                        self.editButton,
                        self.nuevoButton,                        
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),
                        (0,0),(0,0),(0,0),
                        self.eliminarButton,
                       ])
        subMainSizer=wx.BoxSizer(wx.VERTICAL)
        subMainSizer1=wx.BoxSizer(wx.VERTICAL)
        mainSizer=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer.Add(sizer,1, wx.EXPAND | wx.ALL, 20)
        subMainSizer1.Add(sizer1,1, wx.EXPAND | wx.ALL, 20)
        mainSizer.Add(subMainSizer)
        mainSizer.Add(subMainSizer1)
        
        self.SetSizerAndFit(mainSizer)
       
        self.readTable()
    ###############################################################   
            
    def OnCancel(self, evt):
        self.search.Clear()
        self.readTable()
    def OnDoSearch(self, evt):
        term = self.search.GetValue()
        index = self.searchProyectCtrl.GetCurrentSelection()
        field = searchList[index]
        print field
        
        self.proyectsCtrl.DeleteAllItems()
        conn = sqlite3.connect('BDP.db')
        c = conn.cursor()
        if not field == 'robots'and field != 'descripcion'and field != 'fabrica':
            data=c.execute('SELECT * FROM proyectos WHERE %s LIKE ?'% (field), (term,)).fetchall()
          
            index=0
            for i in data:
                
                #loop through and add it
                self.proyectsCtrl.InsertStringItem(index,str(i[0]))
                self.proyectsCtrl.SetStringItem(index,1,str(i[1]))
                self.proyectsCtrl.SetStringItem(index,2,str(i[2]))
                self.proyectsCtrl.SetStringItem(index,3,str(i[4]))
                self.proyectsCtrl.SetStringItem(index,4,str(i[5]))
                index = index + 1 
                 
        elif field == 'descripcion':
            data=c.execute('SELECT * FROM proyectos ').fetchall()
            index=0
            for i in data:
                if (term.lower() in str(i[13]).lower()) or (term.upper() in str(i[13]).upper()):
                    #loop through and add it
                    self.proyectsCtrl.InsertStringItem(index,str(i[0]))
                    self.proyectsCtrl.SetStringItem(index,1,str(i[1]))
                    self.proyectsCtrl.SetStringItem(index,2,str(i[2]))
                    self.proyectsCtrl.SetStringItem(index,3,str(i[4]))
                    self.proyectsCtrl.SetStringItem(index,4,str(i[5]))
                    index = index + 1
        elif field == 'fabrica':
            data=c.execute('SELECT * FROM proyectos ').fetchall()
            index=0
            for i in data:
                if (term.lower() in str(i[5]).lower()) or (term.upper() in str(i[5]).upper()):
                    #loop through and add it
                    self.proyectsCtrl.InsertStringItem(index,str(i[0]))
                    self.proyectsCtrl.SetStringItem(index,1,str(i[1]))
                    self.proyectsCtrl.SetStringItem(index,2,str(i[2]))
                    self.proyectsCtrl.SetStringItem(index,3,str(i[4]))
                    self.proyectsCtrl.SetStringItem(index,4,str(i[5]))
                    index = index + 1
        else:
            
            data=c.execute('SELECT * FROM proyectos ').fetchall()
            index=0
            for i in data:
                if (term.lower() in str(i[11]).lower()) or (term.upper() in str(i[11]).upper()):
                    #loop through and add it
                    self.proyectsCtrl.InsertStringItem(index,str(i[0]))
                    self.proyectsCtrl.SetStringItem(index,1,str(i[1]))
                    self.proyectsCtrl.SetStringItem(index,2,str(i[2]))
                    self.proyectsCtrl.SetStringItem(index,3,str(i[4]))
                    self.proyectsCtrl.SetStringItem(index,4,str(i[5]))
                    index = index + 1

    ###############################################################

    def OnTimeToClose(self, evt):
        
        self.Close()  
            
  
        
    def inicial(self):
        
        if not os.path.isfile('BDP.db'):
            
            conn = sqlite3.connect('BDP.db')
            c = conn.cursor()
            # Create table
            c.execute('''CREATE TABLE proyectos(numProyect text,stateProyect text,tipoProyect text,
                  fechaIniProyect date,cliente text,fabrica text,direccion text,codePostal text,phone text,email text,responsable text,robots text,folder text, descripcion text)''')
        
            # We can also close the connection if we are done with it.
            # Just be sure any changes have been committed or they will be lost.
            conn.close()
    
    def readTable(self):
        self.proyectsCtrl.DeleteAllItems()
        conn = sqlite3.connect('BDP.db')
        c = conn.cursor()
        data=c.execute('SELECT * FROM proyectos ').fetchall()
        index=0
        for i in data:
            #loop through and add it
            self.proyectsCtrl.InsertStringItem(index,str(i[0]))
            self.proyectsCtrl.SetStringItem(index,1,str(i[1]))
            self.proyectsCtrl.SetStringItem(index,2,str(i[2]))
            stringCliente=(i[4]).encode('utf-8')
            self.proyectsCtrl.SetStringItem(index,3,unicode(stringCliente, 'utf-8'))
            stringFab=(i[5]).encode('utf-8')
            self.proyectsCtrl.SetStringItem(index,4,unicode(stringFab, 'utf-8'))
            index = index + 1            
            
            
    def OnShow(self, event):
        index=self.proyectsCtrl.GetFirstSelected()
        
        if index!=-1:
      
            data = self.proyectsCtrl.GetItemText(index)
            conn = sqlite3.connect('BDP.db')
            c = conn.cursor()
            c.execute("""SELECT * FROM proyectos WHERE numProyect = ? """,(data,))
            data = c.fetchone()
            SF= ShowFrame(None,"Dialogo mostrar proyecto")
            SF.Show()
            
            
            SF.numProyectCtrl.SetValue(data[0])
            SF.stateProyectCtrl.SetValue(data[1])
            SF.tipoProyectCtrl.SetValue(data[2])
            SF.fechaProyectCtrl.SetValue(data[3])
            SF.clientProyectCtrl.SetValue(data[4])
            SF.factoryProyectCtrl.SetValue(data[5])
            SF.direccionProyectCtrl.SetValue(data[6])
            SF.codepostalProyectCtrl.SetValue(data[7])
            SF.phoneProyectCtrl.SetValue(data[8])
            SF.emailCtrl.SetValue(data[9])
            SF.responsableCtrl.SetValue(data[10])
            
            for i in list(data[11].split(',')):
                SF.robotsCtrl.Append(i)
            for i in list(data[12].split(',')):
                SF.folderCtrl.Append(i)
            SF.descripCtrl.SetValue(data[13])
            SF.MakeModal(True)
        else:
            dlg = wx.MessageDialog(self, u'Seleccion\xe9 linea!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
            dlg.ShowModal()
            dlg.Destroy()
            
    def OnAdd (self, event):
        useMetal = False
        dlg = AddDialog(self, -1, u"Dialogo a\xf1adir proyecto", size=(350, 200),
                         #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                         style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                         useMetal=useMetal,
                         )
        dlg.CenterOnScreen()

        # this does not return until the dialog is closed.
        val = dlg.ShowModal()
    
        if val == wx.ID_OK:
            print 'Ok pressed'
            
        else:
            print 'cancel pressed'
            

        dlg.Destroy()
        self.readTable()
                    
    def OnEdit (self, event):
        useMetal = False
        index=self.proyectsCtrl.GetFirstSelected()
        
        if index!=-1:
            data = self.proyectsCtrl.GetItemText(index)
            conn = sqlite3.connect('BDP.db')
            c = conn.cursor()
            c.execute("""SELECT * FROM proyectos WHERE numProyect = ? """,(data,))
            data = c.fetchone()
            
            
            editDlg = EditDialog(self, -1, u"Dialogo actualizar proyecto", size=(350, 200),
                             #style=wx.CAPTION | wx.SYSTEM_MENU | wx.THICK_FRAME,
                             style=wx.DEFAULT_DIALOG_STYLE, # & ~wx.CLOSE_BOX,
                             useMetal=useMetal,
                             )
            editDlg.CenterOnScreen()

            editDlg.record=data[0]
            editDlg.numProyectCtrl.SetValue(data[0])
            editDlg.stateProyectCtrl.SetValue(data[1])
            editDlg.tipoProyectCtrl.SetValue(data[2])
            dates=data[3].split('/')
          
            date=wx.DateTime()
           
            date.Set(int(dates[0]),int(dates[1])-1,int(dates[2]))
            date.FormatDate()
            print date
            editDlg.fechaProyectCtrl.SetValue(date)
            editDlg.clientProyectCtrl.SetValue(data[4])
            editDlg.factoryProyectCtrl.SetValue(data[5])
            editDlg.direccionProyectCtrl.SetValue(data[6])
            editDlg.codepostalProyectCtrl.SetValue(data[7])
            editDlg.phoneProyectCtrl.SetValue(data[8])
            editDlg.emailCtrl.SetValue(data[9])
            editDlg.responsableCtrl.SetValue(data[10])
            
            for i in list(data[11].split(',')):
                if i=='KuKa':
                    editDlg.robotsCtrl.Check(0)
                if i=='Fanuc':
                    editDlg.robotsCtrl.Check(1)
                if i=='ABB':
                    editDlg.robotsCtrl.Check(2)
                if i=='Motoman':
                    editDlg.robotsCtrl.Check(3)
                if i=='Staubli':
                    editDlg.robotsCtrl.Check(4)
                if i=='Kawasaki':
                    editDlg.robotsCtrl.Check(5)
                    
                    
            for i in list(data[12].split(',')):
                if i !="":
                    editDlg.folderCtrl.Append(i)
            editDlg.descripCtrl.SetValue(data[13])
            
            val = editDlg.ShowModal()
        
            if val == wx.ID_OK:
                print 'Ok pressed'
                
            else:
                print 'cancel pressed'
                
            editDlg.Destroy()
            self.readTable()
        else:
            dlg = wx.MessageDialog(self, u'Seleccion\xe9 linea!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
            dlg.ShowModal()
            dlg.Destroy()
        
        
    
    def eliminar(self, event):
        
            index = self.proyectsCtrl.GetFirstSelected()
            if index!=-1:
                dlg = wx.MessageDialog(self, u'\xbfQuiere eliminar el proyecto?',
                               'Alerta',
                               #wx.OK | wx.ICON_INFORMATION 
                               wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                               )

                result=dlg.ShowModal()
                dlg.Destroy() 
                if result==5103:
          
                    data = self.proyectsCtrl.GetItemText(index)
                    conn = sqlite3.connect('BDP.db')
                    c = conn.cursor()
                    c.execute("""DELETE  FROM proyectos WHERE numProyect = ? """,(data,))
                    conn.commit()                  
                    # close connection
                    c.close()
                    self.proyectsCtrl.DeleteItem(index)
            else:
                dlg = wx.MessageDialog(self, u'Seleccion\xe9 linea!',
                               'Mensaje',
                               wx.OK | wx.ICON_INFORMATION
                               #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                               )
                dlg.ShowModal()
                dlg.Destroy()
        
        
class AddDialog(wx.Dialog):
   
   
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
        
        
        self.SetBackgroundColour(wx.Colour(100,200,200))
        
     ###--Buttons--##############################################################
    
        self.openFile=wx.Button(self, -1, "Seleccionar directorio", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, self.openFile)
        self.eliminarFile=wx.Button(self, -1, "Eliminar Directorio", (50,50))
        self.Bind(wx.EVT_BUTTON, self.eliminar, self.eliminarFile)
        self.addButton=wx.Button(self, -1, u"A\xf1adir", (50,50))
        self.Bind(wx.EVT_BUTTON, self.addProyecto, self.addButton)
        
  ######################################################################
       
        #row1
        l1=wx.StaticText(self, -1, "Numero de proyecto:")
        self.numProyectCtrl = wx.TextCtrl(self, -1, "",size=(125, -1))
        #row2
        l2=wx.StaticText(self, -1, "Estado del proyecto:")
        self.stateProyectCtrl=wx.ComboBox(self, 500, stateList[0], (90, 50), 
                         (160, -1), stateList,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        #row3
        l3=wx.StaticText(self, -1, "Tipo de proyecto:")
        self.tipoProyectCtrl= wx.ComboBox(self, 500, tipoList[0], (90, 50), 
                         (160, -1), tipoList,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        #row4
        l4=wx.StaticText(self, -1, "Fecha inicio:")
        self.fechaProyectCtrl=wx.GenericDatePickerCtrl(self, size=(120,-1),
                                style = wx.TAB_TRAVERSAL
                                | wx.DP_DEFAULT
                                | wx.DP_SHOWCENTURY
                                | wx.DP_ALLOWNONE )
        #row5
        l5=wx.StaticText(self, -1, "Cliente:")
        self.clientProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        #row6
        l6=wx.StaticText(self, -1, "Fabrica:")
        self.factoryProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        #row7
        l7=wx.StaticText(self, -1, "Direccion:")
        self.direccionProyectCtrl= wx.TextCtrl(self,-1, "",size=(125, -1))
        #row8
        l8=wx.StaticText(self, -1, "Codigo postal:")
        self.codepostalProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        #row9
        l9=wx.StaticText(self, -1, "Telefono:")
        self.phoneProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        # row10
        l10=wx.StaticText(self, -1, "Email:")
        self.emailCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        # row11
        l11=wx.StaticText(self, -1, "Responsable:")
        self.responsableCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        #row12 
        l12=wx.StaticText(self, -1, "Robots:")
        self.robotsCtrl= wx.CheckListBox(self, -1, (50, 50), (100, 80), robotsList)  
        # row13
        l13=wx.StaticText(self, -1, "Carpetas:")
        self.folderCtrl= wx.ListBox(self, 60, (100, 50), (300, 50), [], wx.LB_SINGLE)
        self.folderCtrl.SetBackgroundColour(wx.WHITE)
        #row1 and col2
         # row14
        l14=wx.StaticText(self, -1, "Descripcion")
        self.descripCtrl= wx.TextCtrl(self, -1,
                        "",size=(300, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        
        btn = wx.Button(self, wx.ID_OK,'Cerrar')
        btn.SetDefault()
        
       
        sizer= wx.FlexGridSizer(rows=0,cols=2, hgap=5, vgap=5)
        sizer.AddMany([l1,self.numProyectCtrl,
                       l2,self.stateProyectCtrl,
                       l3,self.tipoProyectCtrl,
                       l4,self.fechaProyectCtrl,
                       l5,self.clientProyectCtrl,
                       l6,self.factoryProyectCtrl,
                       l7,self.direccionProyectCtrl,
                       l8,self.codepostalProyectCtrl,
                       l9,self.phoneProyectCtrl,
                       l10,self.emailCtrl,
                       l11,self.responsableCtrl,
                       l12,self.robotsCtrl,
                       l13,self.folderCtrl,
                       (0,0),self.openFile,
                       (0,0),self.eliminarFile,
                       l14,self.descripCtrl,
                       ])
        
     
        sizer1= wx.FlexGridSizer(rows=0,cols=1, hgap=5, vgap=5)
        sizer1.AddMany([self.addButton,btn,
                        
                       ])
        
        subMainSizer=wx.BoxSizer(wx.VERTICAL)
        subMainSizer1=wx.BoxSizer(wx.VERTICAL)
        mainSizer=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer.Add(sizer,1, wx.EXPAND | wx.ALL, 20)
        subMainSizer1.Add(sizer1,1, wx.EXPAND | wx.ALL, 20)
        mainSizer.Add(subMainSizer)
        mainSizer.Add(subMainSizer1)
        
        self.SetSizerAndFit(mainSizer)
       
    ###############################################################   
            
    def eliminar(self, evt):
        index = self.folderCtrl.GetSelection()
        self.folderCtrl.Delete(index)
        
        
  
    def OnButton(self, evt):
       
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
            paths = dlg.GetPath()
            self.folderCtrl.Append(paths)
            
        dlg.Destroy()
        
    
    
        
    def addProyecto(self, evt):

        """Event handler for the button click."""
       
        dlg = wx.MessageDialog(self, u'\xbfQuiere a\xf1adir proyecto?',
                               'Alerta',
                               #wx.OK | wx.ICON_INFORMATION 
                               wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                               )

        result=dlg.ShowModal()
        dlg.Destroy() 
        print result
        if result==5103:
            ######data gathering###############
            carpetas=self.folderCtrl.GetItems()
            
            carpetas=','.join(carpetas)
            robots=','.join(self.robotsCtrl.GetCheckedStrings())
            
            
            date = str(self.fechaProyectCtrl.GetValue().GetDay()) + '/' + str(self.fechaProyectCtrl.GetValue().GetMonth()+1) + '/' +str(self.fechaProyectCtrl.GetValue().GetYear())
                              
            
            ###################################
            # create sqlite connection            
            conn = sqlite3.connect('BDP.db')
            c = conn.cursor()
           
            data=c.execute('SELECT * FROM proyectos ').fetchall()
            index=0
            bOk=False
            for i in data:
                if (self.numProyectCtrl.GetValue().lower() == str(i[0]).lower()) or \
                (self.numProyectCtrl.GetValue().upper() == str(i[0]).upper()):
                    bOk=True
                index = index + 1  
            
            if not bOk==True and self.numProyectCtrl.GetValue() != '':
                # insert a row
                insertData=(self.numProyectCtrl.GetValue(),self.stateProyectCtrl.GetValue(),self.tipoProyectCtrl.GetValue(),
                             date,self.clientProyectCtrl.GetValue(),self.factoryProyectCtrl.GetValue(),
                             self.direccionProyectCtrl.GetValue(),self.codepostalProyectCtrl.GetValue(),
                             self.phoneProyectCtrl.GetValue(),self.emailCtrl.GetValue(),
                             self.responsableCtrl.GetValue(),robots,carpetas,self.descripCtrl.GetValue())
                
                
                c.execute('INSERT INTO proyectos VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',insertData)
                conn.commit()                  
                # close connection
                c.close()
                
            elif self.numProyectCtrl.GetValue() == '':
                dlg = wx.MessageDialog(self, 'Campo Numero de proyecto no puede estar vacio!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                dlg.ShowModal()
                dlg.Destroy()
                
            else:
                dlg = wx.MessageDialog(self, 'Numero de proyecto existente, elija otro!',
                           'Alerta',
                           wx.OK | wx.ICON_INFORMATION
                           #wx.YES_NO | wx.NO_DEFAULT | wx.CANCEL | wx.ICON_INFORMATION
                           )
                dlg.ShowModal()
                dlg.Destroy()
                        
       
        

class ShowFrame(wx.Frame):
    """
    This is MyFrame.  It just shows a few controls on a wxPanel,
    and has a simple menu.
    """    
    def __init__(self, parent, title):
            
        wx.Frame.__init__(self, parent, -1, title,
                          size=wx.DefaultSize, pos=(100,10), style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
       
        self.Bind(wx.EVT_CLOSE, self.on_close)
    
        
        self.SetBackgroundColour(wx.Colour(100,200,200))
        
         ###--Buttons--##############################################################
    
        self.openFile=wx.Button(self, -1, "Abrir directorio", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, self.openFile)
        
  ######################################################################
        
         #row1
        l1=wx.StaticText(self, -1, "Numero de proyecto:")
        self.numProyectCtrl = wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.numProyectCtrl.SetEditable(False)
        #row2
        l2=wx.StaticText(self, -1, "Estado del proyecto:")
        self.stateProyectCtrl=wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.stateProyectCtrl.SetEditable(False)
        #row3
        l3=wx.StaticText(self, -1, "Tipo de proyecto:")
        self.tipoProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.tipoProyectCtrl.SetEditable(False)
        #row4
        l4=wx.StaticText(self, -1, "Fecha inicio:")
        self.fechaProyectCtrl=wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.fechaProyectCtrl.SetEditable(False)
        #row5
        l5=wx.StaticText(self, -1, "Cliente:")
        self.clientProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.clientProyectCtrl.SetEditable(False)
        #row6
        l6=wx.StaticText(self, -1, "Fabrica:")
        self.factoryProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.factoryProyectCtrl.SetEditable(False)
        #row7
        l7=wx.StaticText(self, -1, "Direccion:")
        self.direccionProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.direccionProyectCtrl.SetEditable(False)
        #row8
        l8=wx.StaticText(self, -1, "Codigo postal:")
        self.codepostalProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.codepostalProyectCtrl.SetEditable(False)
        #row9
        l9=wx.StaticText(self, -1, "Telefono:")
        self.phoneProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.phoneProyectCtrl.SetEditable(False)
        # row10
        l10=wx.StaticText(self, -1, "Email:")
        self.emailCtrl= wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.emailCtrl.SetEditable(False)
        # row11
        l11=wx.StaticText(self, -1, "Responsable:")
        self.responsableCtrl= wx.TextCtrl(self, -1, "",size=(125, -1),style=wx.TE_READONLY)
        self.responsableCtrl.SetEditable(False)
        #row12 
        l12=wx.StaticText(self, -1, "Robots:")
        self.robotsCtrl= wx.ListBox(self, 60, (100, 50), (90, 80), [], wx.LB_SINGLE)
        self.robotsCtrl.SetBackgroundColour(wx.WHITE)  
        # row13
        l13=wx.StaticText(self, -1, "Carpetas:")
        self.folderCtrl= wx.ListBox(self, 60, (100, 50), (300, 50), [], wx.LB_SINGLE)
        self.folderCtrl.SetBackgroundColour(wx.WHITE)
        #row1 and col2
         # row14
        l14=wx.StaticText(self, -1, "Descripcion")
        self.descripCtrl= wx.TextCtrl(self, -1,
                        "",size=(300, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_READONLY)
        self.descripCtrl.SetEditable(False)
        
              
        sizer= wx.FlexGridSizer(rows=0,cols=2, hgap=5, vgap=5)
        sizer.AddMany([l1,self.numProyectCtrl,
                       l2,self.stateProyectCtrl,
                       l3,self.tipoProyectCtrl,
                       l4,self.fechaProyectCtrl,
                       l5,self.clientProyectCtrl,
                       l6,self.factoryProyectCtrl,
                       l7,self.direccionProyectCtrl,
                       l8,self.codepostalProyectCtrl,
                       l9,self.phoneProyectCtrl,
                       l10,self.emailCtrl,
                       l11,self.responsableCtrl,
                       l12,self.robotsCtrl,
                       l13,self.folderCtrl,
                       (0,0),self.openFile,
                       l14,self.descripCtrl,
                       ])
        
             
        mainSizer=wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(sizer,1, wx.EXPAND | wx.ALL, 20)
        self.SetSizerAndFit(mainSizer)
       
        
    def OnButton(self, evt):
        index=self.folderCtrl.GetSelection()
        print index
        if index >= 0:
            path=self.folderCtrl.GetString(index)
            print path
            if path!='':        
                subprocess.call(['explorer', path])
                
    
    def on_close(self, evt):
        self.MakeModal(False)
        evt.Skip()    

class EditDialog(wx.Dialog):
   
   
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
        
        
        self.SetBackgroundColour(wx.Colour(100,200,200))
        
     ###--Buttons--##############################################################
    
        self.openFile=wx.Button(self, -1, "Seleccionar directorio", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, self.openFile)
        self.eliminarFile=wx.Button(self, -1, "Eliminar Directorio", (50,50))
        self.Bind(wx.EVT_BUTTON, self.eliminar, self.eliminarFile)
        self.updateButton=wx.Button(self, -1, "Actualizar", (50,50))
        self.Bind(wx.EVT_BUTTON, self.UpdateProyecto, self.updateButton)
        
  ######################################################################
        self.record=""
        
        #row1
        l1=wx.StaticText(self, -1, "Numero de proyecto:")
        self.numProyectCtrl = wx.TextCtrl(self, -1, "",size=(125, -1))
        self.numProyectCtrl.SetEditable(False)
        #row2
        l2=wx.StaticText(self, -1, "Estado del proyecto:")
        self.stateProyectCtrl=wx.ComboBox(self, 500, stateList[0], (90, 50), 
                         (160, -1), stateList,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        #row3
        l3=wx.StaticText(self, -1, "Tipo de proyecto:")
        self.tipoProyectCtrl= wx.ComboBox(self, 500, tipoList[0], (90, 50), 
                         (160, -1), tipoList,
                         wx.CB_DROPDOWN
                         | wx.TE_PROCESS_ENTER
                         #| wx.CB_SORT
                         )
        #row4
        l4=wx.StaticText(self, -1, "Fecha inicio:")
        self.fechaProyectCtrl=wx.GenericDatePickerCtrl(self, size=(120,-1),
                                style = wx.TAB_TRAVERSAL
                                | wx.DP_DEFAULT
                                | wx.DP_SHOWCENTURY
                                | wx.DP_ALLOWNONE )
        
        
        
        #row5
        l5=wx.StaticText(self, -1, "Cliente:")
        self.clientProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        #row6
        l6=wx.StaticText(self, -1, "Fabrica:")
        self.factoryProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        #row7
        l7=wx.StaticText(self, -1, "Direccion:")
        self.direccionProyectCtrl= wx.TextCtrl(self,-1, "",size=(125, -1))
        #row8
        l8=wx.StaticText(self, -1, "Codigo postal:")
        self.codepostalProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        #row9
        l9=wx.StaticText(self, -1, "Telefono:")
        self.phoneProyectCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        # row10
        l10=wx.StaticText(self, -1, "Email:")
        self.emailCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        # row11
        l11=wx.StaticText(self, -1, "Responsable:")
        self.responsableCtrl= wx.TextCtrl(self, -1, "",size=(125, -1))
        #row12 
        l12=wx.StaticText(self, -1, "Robots:")
        self.robotsCtrl= wx.CheckListBox(self, -1, (50, 50), (100, 80), robotsList)  
        # row13
        l13=wx.StaticText(self, -1, "Carpetas:")
        self.folderCtrl= wx.ListBox(self, 60, (100, 50), (300, 50), [], wx.LB_SINGLE)
        self.folderCtrl.SetBackgroundColour(wx.WHITE)
        #row1 and col2
         # row14
        l14=wx.StaticText(self, -1, "Descripcion")
        self.descripCtrl= wx.TextCtrl(self, -1,
                        "",size=(300, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        
        btn = wx.Button(self, wx.ID_OK,'Cerrar')
        btn.SetDefault()
        
       
        sizer= wx.FlexGridSizer(rows=0,cols=2, hgap=5, vgap=5)
        sizer.AddMany([l1,self.numProyectCtrl,
                       l2,self.stateProyectCtrl,
                       l3,self.tipoProyectCtrl,
                       l4,self.fechaProyectCtrl,
                       l5,self.clientProyectCtrl,
                       l6,self.factoryProyectCtrl,
                       l7,self.direccionProyectCtrl,
                       l8,self.codepostalProyectCtrl,
                       l9,self.phoneProyectCtrl,
                       l10,self.emailCtrl,
                       l11,self.responsableCtrl,
                       l12,self.robotsCtrl,
                       l13,self.folderCtrl,
                       (0,0),self.openFile,
                       (0,0),self.eliminarFile,
                       l14,self.descripCtrl,
                       ])
        
     
        sizer1= wx.FlexGridSizer(rows=0,cols=1, hgap=5, vgap=5)
        sizer1.AddMany([self.updateButton,btn,
                        
                       ])
        
        subMainSizer=wx.BoxSizer(wx.VERTICAL)
        subMainSizer1=wx.BoxSizer(wx.VERTICAL)
        mainSizer=wx.BoxSizer(wx.HORIZONTAL)
        subMainSizer.Add(sizer,1, wx.EXPAND | wx.ALL, 20)
        subMainSizer1.Add(sizer1,1, wx.EXPAND | wx.ALL, 20)
        mainSizer.Add(subMainSizer)
        mainSizer.Add(subMainSizer1)
        
        self.SetSizerAndFit(mainSizer)
       
    ###############################################################   
            
    def eliminar(self, evt):
        index = self.folderCtrl.GetSelection()
        self.folderCtrl.Delete(index)
        
        
  
    def OnButton(self, evt):
       
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
            paths = dlg.GetPath()
            self.folderCtrl.Append(paths)
            
        dlg.Destroy()
        
    
    
        
    def UpdateProyecto(self, evt):

        """Event handler for the button click."""
       
        dlg = wx.MessageDialog(self, u'\xbfQuiere actualizar proyecto?',
                               'Alerta',
                               #wx.OK | wx.ICON_INFORMATION 
                               wx.YES_NO | wx.NO_DEFAULT  | wx.ICON_INFORMATION
                               )

        result=dlg.ShowModal()
        dlg.Destroy()  
        print result 
        if result==5103:
            ######data gathering###############
            carpetas=self.folderCtrl.GetItems()
            
            carpetas=','.join(carpetas)
            robots=','.join(self.robotsCtrl.GetCheckedStrings())
            date = str(self.fechaProyectCtrl.GetValue().GetDay()) + '/' + str(self.fechaProyectCtrl.GetValue().GetMonth()+1) + '/' +str(self.fechaProyectCtrl.GetValue().GetYear())

            
            ###################################
            # create sqlite connection            
            conn = sqlite3.connect('BDP.db')
            cur = conn.cursor()
            # insert a row
            
            cur.execute("UPDATE proyectos SET stateProyect=? WHERE numProyect=?", (self.stateProyectCtrl.GetValue(), self.record)) 
            cur.execute("UPDATE proyectos SET tipoProyect=? WHERE numProyect=?", (self.tipoProyectCtrl.GetValue(), self.record))
            cur.execute("UPDATE proyectos SET fechaIniProyect=? WHERE numProyect=?", (date, self.record))
            cur.execute("UPDATE proyectos SET cliente=? WHERE numProyect=?", (self.clientProyectCtrl.GetValue(), self.record))
            cur.execute("UPDATE proyectos SET fabrica=? WHERE numProyect=?", (self.factoryProyectCtrl.GetValue(), self.record))
            cur.execute("UPDATE proyectos SET direccion=? WHERE numProyect=?", (self.direccionProyectCtrl.GetValue(), self.record))
            cur.execute("UPDATE proyectos SET codePostal=? WHERE numProyect=?", (self.codepostalProyectCtrl.GetValue(), self.record))
            cur.execute("UPDATE proyectos SET phone=? WHERE numProyect=?", (self.phoneProyectCtrl.GetValue(), self.record))
            cur.execute("UPDATE proyectos SET email=? WHERE numProyect=?", (self.emailCtrl.GetValue(), self.record))
            cur.execute("UPDATE proyectos SET responsable=? WHERE numProyect=?", (self.responsableCtrl.GetValue(), self.record))
            cur.execute("UPDATE proyectos SET robots=? WHERE numProyect=?", (robots, self.record))
            cur.execute("UPDATE proyectos SET folder=? WHERE numProyect=?", (carpetas, self.record))
            cur.execute("UPDATE proyectos SET descripcion=? WHERE numProyect=?", (self.descripCtrl.GetValue(), self.record))
          
            conn.commit()                  
            # close connection
            cur.close()
        
        
class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None,"BDP por XF")
        self.SetTopWindow(frame)

        frame.Show(True)
        return True
        
app = MyApp(redirect=False)
app.MainLoop()
