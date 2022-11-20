# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 14:53:47 2021

@author: User
"""
from tkinter import Tk, E, Canvas, Label, StringVar, Toplevel
from tkinter import W as West
from tkinter.ttk import Frame, Button, Entry
import psyfunc as ps
from collections import namedtuple
from tksheet import Sheet
from math import nan, isnan

Pair = namedtuple("Pair", ["T", "W"])

P = 101325
Tmax = 46.0
sheetdata = []
chartdata = []



class Chart(Frame):

    def __init__(self):
        """
        Returns
        -------
        None.

        """
        super().__init__()

        self.initUI()
    
    def drawseries(self, data, wid, col):
        """
        Draws a line series
        
        Parameters
        ----------
        data :  List of lists
                X,Y coordinates
        wid :   Int
                Line Width
        col :   String
                Colour

        Returns
        -------
        None.

        """
        T1, W1 = data[0]
        x1 = 15 * T1
        y1 = 500 - (16667 * W1)
            
        xtemp = x1
        ytemp = y1
        
        for T2, W2 in data:
        	x1 = xtemp
        	y1 = ytemp
        	x2 = 15 * T2
        	y2 = 500 - (16667*W2)
        	#canvas.create_oval(x2-6, y2-6, x2+6, y2+6, width=1, outline='black', fill='skyBlue2')
        	self.canvas.create_line(x1, y1, x2, y2, width = wid, fill = col)
        	xtemp = x2
        	ytemp = y2
            
    def drawtext(self, T, W, Text, col, ang):
        """
        Draws Text
        Parameters
        ----------
        T :     Float
                X-coordinate as T
        W :     Float
                Y coordinate as W
        Text :  String
                Text to display
        col :   String
                Colour
        ang :   Int
                Text angle

        Returns
        -------
        None.

        """
        x1 = 15 * T
        y1 = 500 - (16667 * W)
        self.canvas.create_text(x1, y1, text=Text, angle = ang, fill = col, anchor = 'w')
    
    def drawdot(self, T, W):
        """
        Marks a point.

        Parameters
        ----------
        T : Float
            X-coordinate as T
        W : Float
            Y-coordinate as W

        Returns
        -------
        None.

        """
        if ps.Phi_W(T, W, P)<=1 and W>=0:
            x = 15*T
            y = 500-(16667*W)
            self.canvas.create_oval(x-3, y-3, x+3, y+3, outline='red', fill='#ff8888', tags=('point', 'circle'))
            self.canvas.create_rectangle( (x, y)*2, tags=('point', 'dot') )
        
    def motion(self, event):
        x, y = event.x, event.y
        T, W = round(x/15, 1), round((500-y)/16667, 4)
        
        if ps.Phi_W(T, W, P)<=1 and W>0:
            #print('{}, {}'.format(T, W))
            self.canvas.config(cursor="tcross")
            T = round(T, 1)
            W1 = round(W * 1000, 2)
            Tw = round(ps.Tw_W(T, W, P), 2)
            RH = round(ps.Phi_W(T, W, P)*100, 1)
            Td = round(ps.Tdp_W(T, W, P),1)
            H  = round(ps.H_W(T, W), 1)
            V  = round(ps.V_W(T, W, P), 3)
            
            self.TVar.set('T='+format(T, '.1f')+u"\N{DEGREE SIGN}"+'C')
            self.WVar.set(' W='+format(W1, '.2f')+'g/kg')
            self.TwVar.set(' Tw='+format(Tw, '.2f')+u"\N{DEGREE SIGN}"+'C')
            self.RHVar.set(' RH='+format(RH, '.1f')+'%')
            self.TdVar.set(' Td='+format(Td, '.1f')+u"\N{DEGREE SIGN}"+'C')
            self.HVar.set(' H='+format(H, ',.1f')+'Cal/kg')
            self.VVar.set(' V='+format(V, '.3f')+u"m\u00b3"+'/kg')
        else:
            '''self.canvas.config(cursor="fleur")
            self.TVar.set('T=____'+u"\N{DEGREE SIGN}"+'C')
            self.WVar.set('W=______g/kg')
            self.TwVar.set(' Tw=_____'+u"\N{DEGREE SIGN}"+'C')
            self.RHVar.set(' RH=____'+'%')
            self.TdVar.set(' Td=_____'+u"\N{DEGREE SIGN}"+'C')
            self.HVar.set(' H=______'+'Cal/kg')
            self.VVar.set(' V=_____'+u"m\u00b3"+'/kg')'''
            self.canvas.config(cursor="fleur")
            self.TVar.set('')
            self.WVar.set('')
            self.TwVar.set('')
            self.RHVar.set('')
            self.TdVar.set('')
            self.HVar.set('')
            self.VVar.set('')

    def initUI(self):
        self.master.title("Phisatho Psychro-chart")
        #Style().configure("TButton", padding=(0, 5, 0, 5),
        #    font='serif 10')
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.columnconfigure(4, pad=3)
        
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        edge = Canvas(self, width = 900, height = 600, bg = '#bbbbbb')
        edge.grid(row=0, columnspan=5,rowspan=2, sticky=West+E)
        button1 = Button(self, text = 'Add', command = self.dataentry)
        button1.grid(row=2, column=1)
        button2 = Button(self, text = 'Quit', command = self.quit)
        button2.grid(row=2, column=3)
        
        self.canvas = Canvas(edge, width = 690, height = 500, bg = 'white', bd = 1, relief = 'sunken')
        self.canvas.place(relx=0.5, rely=0.5, anchor='center')
        
        self.canvas.bind('<Motion>', self.motion)
        
        f1 = Frame(self, width=550, height=25)
        self.TVar    = StringVar()
        self.WVar    = StringVar()
        self.TwVar   = StringVar()
        self.RHVar   = StringVar()
        self.TdVar   = StringVar()
        self.HVar    = StringVar()
        self.VVar    = StringVar()
        self.Tlabel  = Label(f1, textvariable=self.TVar).pack(side="left")
        self.WLabel  = Label(f1, textvariable=self.WVar).pack(side="left")
        self.Twlabel = Label(f1, textvariable=self.TwVar).pack(side="left")
        self.RHLabel = Label(f1, textvariable=self.RHVar).pack(side="left")
        self.TdLabel = Label(f1, textvariable=self.TdVar).pack(side="left")
        self.HLabel  = Label(f1, textvariable=self.HVar).pack(side="left")
        self.VLabel  = Label(f1, textvariable=self.VVar).pack(side="left")
        
        f1.grid(row=2, column=4)
        f1.pack_propagate(False)
        
        self.pack()
         
        Pair = namedtuple("Pair", ["T", "W"])

        #Draw W lines
        for i in range(31):
            W = 0.001 * i
            WSet = []
            if ps.Tsat_W(W, P) < 0:
                #print(ps.Tsat_W(W, P))
                WSet.append(Pair(0, W))
                WSet.append(Pair(46, W))
            else:
                WSet.append(Pair(ps.Tsat_W(W, P), W))
                WSet.append(Pair(46, W))
            self.drawseries(WSet, 1, '#cccccc')

        #Draw RH-10 line
        RH10 = []
        for T in range(int(Tmax) + 1):
            W = ps.W_Phi(T, 0.1, P)
            RH10.append(Pair(T, W))
        self.drawseries(RH10, 1, 'grey')

        #Draw RH-20 line
        RH20 = []
        for T in range(int(Tmax)+1):
            W = ps.W_Phi(T, 0.2, P)
            RH20.append(Pair(T, W))
        self.drawseries(RH20, 1, 'grey')

        #Draw RH-30 line
        RH30 = []
        for T in range(int(Tmax+1)):
            W = ps.W_Phi(T, 0.3, P)
            RH30.append(Pair(T, W))
        self.drawseries(RH30, 1, 'grey')

        #Draw RH-40 line
        RH40 = []
        for T in range(int(Tmax+1)):
            W = ps.W_Phi(T, 0.4, P)
            RH40.append(Pair(T, W))
        self.drawseries(RH40, 1, 'grey')

        #Draw RH-50 line
        RH50 = []
        for T in range(int(Tmax+1)):
            W = ps.W_Phi(T, 0.5, P)
            RH50.append(Pair(T, W))
        self.drawseries(RH50, 1, 'black')

        #Draw RH-60 line
        RH60 = []
        for T in range(int(Tmax+1)):
            W = ps.W_Phi(T, 0.6, P)
            RH60.append(Pair(T, W))
        self.drawseries(RH60, 1, 'grey')

        #Draw RH-70 line
        RH70 = []
        for T in range(int(Tmax+1)):
            W = ps.W_Phi(T, 0.7, P)
            RH70.append(Pair(T, W))
        self.drawseries(RH70, 1, 'grey')

        #Draw RH-80 line
        RH80 = []
        for T in range(int(Tmax+1)):
            W = ps.W_Phi(T, 0.8, P)
            RH80.append(Pair(T, W))
        self.drawseries(RH80, 1, 'grey')

        #Draw RH-90 line
        RH90 = []
        for T in range(int(Tmax+1)):
            W = ps.W_Phi(T, 0.9, P)
            RH90.append(Pair(T, W))
        self.drawseries(RH90, 1, 'grey')

        #Draw Saturation line
        RH100 = []
        for T in range(int(Tmax+1)):
            W = ps.W_Phi(T, 1.0, P)
            RH100.append(Pair(T, W))
        self.drawseries(RH100, 2, 'blue')

        #Draw Wet-bulb lines
        for Tw in range(5):
            TWSet = []
            Tw = Tw - 5
            W = ps.W_Tw(0, Tw, P)
            TWSet.append(Pair(0, W))
            T2 = ps.T_TwW(Tw, 0.00001, P)
            TWSet.append(Pair(T2, 0.0001))
            self.drawseries(TWSet, 1, 'skyblue')

        for T in range(35):
            TWSet = []
            W = ps.Ws_T(T, P)
            TWSet.append(Pair(T, W))
            T2 = ps.T_TwW(T, 0, P)
            TWSet.append(Pair(T2, 0))
            self.drawseries(TWSet, 1, 'skyblue')

        for H in range (14):
            H = H * 10000
            HSet = []
            T1 = ps.Ts_H(H, P)
            W1 = ps.Ws_T(T1, P)
            HSet.append(Pair(T1, W1))
            T2 = ps.T_HW(H, 0 )
            HSet.append(Pair(T2, 0))
            self.drawseries(HSet, 1, '#44ff44')
            self.drawtext(T1+0.5, W1 - 0.0002, 'H='+str(int(H/1000)), '#00aa00', -25)

        for V in range(18):
            V = 0.01 * (V) + 0.78
            VSet = []
            T1 = ps.Ts_V(V, P)
            W1 = ps.Ws_T(T1, P)
            VSet.append(Pair(T1, W1))
            T2 = ps.T_VW(V, 0, P)
            VSet.append(Pair(T2, 0))
            self.drawseries(VSet, 1, '#DA8F44')
        #    drawtext(T1+1.1, W1 - 0.0020, 'v='+str(round(V, 3)), '#964B00', -65)
            self.drawtext(T1+1.1, W1 - 0.0020, 'v='+str(round(V, 3)), '#aaaaaa', -65)

        #Draw T lines
        for i in range(47):
            x = (i * 15)
            self.canvas.create_line(x, 550, x, 500 - (16667*ps.Ws_T(i, P)), fill = '#bbbbbb')
        
        #Draw T Ticks and labels        
        for i in range (24):
        	x = 103 + (i * 30)
        	edge.create_line(x, 560, x, 565, width = 1)
        	edge.create_text(x, 566, text = '%d'%(2*i), anchor = 'n')
        edge.create_text(447, 580, text='T ('+u"\N{DEGREE SIGN}"+'C)', anchor='n')

        #Draw W ticks and labels
        for i in range(7):
        	y = 549 - (i *83.335)
        	edge.create_line(804, y, 809, y, width = 1)
        	edge.create_text(810, y, text = '%.1f'% (5 * i), anchor = 'w')
        edge.create_text(820, 275, text='W (g/kg)', anchor='w')
                
    def quit(self):
        self.master.destroy()
        
    def dataentry(self):
          
        self.dataentry = Toplevel(self)
        self.dataentry.geometry('1000x300')
        self.dataentry.title('States and Processes')
        self.dataentry.columnconfigure(0, weight = 10)
        self.dataentry.rowconfigure(0, weight = 1)
        self.frame = Frame(self.dataentry)
        self.frame.grid(row = 0, column = 0, sticky = "nswe")
        self.frame.grid_columnconfigure(0, weight = 1)
        self.frame.grid_columnconfigure(1, weight = 1)
        self.frame.grid_columnconfigure(2, weight = 1)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.sheet = Sheet(self.frame,
                      page_up_down_select_row = True,
                      expand_sheet_if_paste_too_big = True,
                      row_index_align = "e",
                      headers = ['Name', 'T ('+u"\N{DEGREE SIGN}"+'C)', 'Tw ('+u"\N{DEGREE SIGN}"+'C)', 'RH (%)', 'W (g/kg)', 'Tdp ('+u"\N{DEGREE SIGN}"+'C)', 'H (J/kg)', 'V (m\u00b3/kg)', 'Process from']
                      )
        self.sheet.enable_bindings(("single_select", #"single_select" or "toggle_select"
                                "drag_select",   #enables shift click selection as well
                                "select_all",
                                "column_drag_and_drop",
                                "row_drag_and_drop",
                                "column_select",
                                "row_select",
                                "column_width_resize",
                                "double_click_column_resize",
                                "row_width_resize",
                                "column_height_resize",
                                "arrowkeys",
                                "row_height_resize",
                                "double_click_row_resize",
                                "right_click_popup_menu",
                                "rc_select",
                                "rc_insert_column",
                                "rc_delete_column",
                                "rc_insert_row",
                                "rc_delete_row",
                                "copy",
                                "cut",
                                "paste",
                                "delete",
                                "undo",
                                "edit_cell"
                                    ))
        self.sheet.grid(row = 0,  columnspan = 3, sticky = "nswe")
        self.sheet.insert_row() 
        self.sheet.insert_row() 
        self.sheet.insert_row() 
        self.sheet.insert_row() 
        self.buttonadd = Button(self.frame, text = 'Add', command = lambda:[self.sheet.insert_row(), self.sheet.redraw()])
        self.buttonadd.grid(row = 1, column=0, padx=10, pady=5)#, sticky='nswe')
        self.buttonupdate = Button(self.frame, text = 'Update', command = self.updatesheet)
        self.buttonupdate.grid(row = 1, column=1, padx=10, pady=5)#, sticky='nswe')
        self.buttonclose = Button(self.frame, text = 'Close', command = self.dataentry.destroy)
        self.buttonclose.grid(row = 1, column=2, padx=10, pady=5)#, sticky='nswe')
        self.sheet.set_sheet_data(chartdata)
        if not bool(chartdata):
            self.sheet.insert_row()
        self.sheet.redraw()
        
    def updatesheet(self):
        dataset = self.sheet.get_sheet_data()
        chartdata = []
        sheetdata = []
        validpoint = False
        for i in range(len(dataset)):
            pointdata = []
            tempdata = dataset[i]
            for j in range(len(tempdata)):
                if j == 0:
                    pointdata.append(tempdata[j])
                else:
                    try:
                        pointdata.append(float(tempdata[j]))
                    except:
                        pointdata.append(nan)
            sheetdata.append(pointdata)
        #print(sheetdata)
        for i in range(len(sheetdata)):
            pd = sheetdata[i]
            nametemp = pd[0]
            if (pd[1]>=0 and pd[1]<=46):
                if ((pd[2]>=-6) and (pd[2]<=33)): #T, Tw
                    if ps.Phi_Tw(pd[1], pd[2], P)<=1:
                        validpoint = True
                        ttemp  = round(pd[1], 2)
                        twtemp = round(pd[2], 2)
                        rhtemp = round(100.0*ps.Phi_Tw(ttemp, twtemp, P), 2)
                        wtemp  = round(1000.0*ps.W_Tw(ttemp, twtemp, P), 2)
                        tdtemp = round(ps.Tdp_Tw(ttemp, twtemp, P), 2)
                        htemp  = round(ps.H_W(ttemp, wtemp/1000.0), 2)
                        vtemp  = round(ps.V_W(ttemp, wtemp/1000.0, P), 3)
                elif (pd[3]>=0 and pd[3]<=100.0): #T, RH
                    validpoint = True    
                    ttemp  = round(pd[1], 2)
                    rhtemp = round(pd[3], 2)
                    twtemp = round(ps.Tw_Phi(ttemp, rhtemp/100.0, P), 2)
                    wtemp  = round(1000.0*ps.W_Phi(ttemp, rhtemp/100.0, P), 2)
                    tdtemp = round(ps.Tdp_Phi(ttemp, rhtemp/100.0), 2)
                    htemp  = round(ps.H_W(ttemp, wtemp/1000.0), 2)
                    vtemp  = round(ps.V_W(ttemp, wtemp/1000.0, P), 3)
                elif (pd[4]>=0 and pd[4]<=30): #T, W
                    if ps.Phi_W(pd[1], pd[4]/1000.0, P)<=1:
                        validpoint = True
                        ttemp  = round(pd[1], 2)
                        wtemp  = round(pd[4], 2)
                        twtemp = round(ps.Tw_W(ttemp, wtemp/1000.0, P), 2)
                        rhtemp = round(100.0*ps.Phi_W(ttemp, wtemp/1000.0, P), 2)
                        tdtemp = round(ps.Tdp_W(ttemp, wtemp/1000.0, P), 2)
                        htemp  = round(ps.H_W(ttemp, wtemp/1000.0), 2)
                        vtemp  = round(ps.V_W(ttemp, wtemp/1000.0, P), 3)
                else:
                    ttemp  = round(pd[1], 2)
                    twtemp = nan
                    rhtemp = nan
                    wtemp  = nan
                    tdtemp = nan
                    htemp  = nan
                    vtemp  = nan
                
            else:
                ttemp  = nan
                twtemp = nan
                rhtemp = nan
                wtemp  = nan
                tdtemp = nan
                htemp  = nan
                vtemp  = nan
            pd = []
            pd.append(nametemp)
            if not isnan(ttemp):
                pd.append(ttemp)
            else:
                pd.append('')
            if not isnan(twtemp):
                pd.append(twtemp)
            else:
                pd.append('')
            if not isnan(rhtemp):
                pd.append(rhtemp)
            else:
                pd.append('')
            if not isnan(wtemp):
                pd.append(wtemp)
            else:
                pd.append('')
            if not isnan(tdtemp):
                pd.append(tdtemp)
            else:
                pd.append('')
            if not isnan(htemp):
                pd.append(htemp)
            else:
                pd.append('')
            if not isnan(vtemp):
                pd.append(vtemp)
            else:
                pd.append('')
            
            print(pd)
            
            chartdata.append(pd)
        self.canvas.delete("point")
        for i in range(len(chartdata)):
            pointdata = chartdata[i]
            try:
                self.drawdot(pointdata[1], pointdata[4]/1000.0)
            except:
                pass
        self.sheet.set_sheet_data(chartdata)
                
            

def main():
    root = Tk()
    app = Chart()
    root.mainloop()

if __name__ == '__main__':
    main()
