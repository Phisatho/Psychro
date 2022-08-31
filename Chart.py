from tkinter import Tk, Button, Canvas
from collections import namedtuple
import psyfunc as ps

P = 101325
Tmin = 0.0
Tmax = 46.0
Wmin = 0.0
Wmax = 0.03



def drawseries(data, wid, col):
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
    	canvas.create_line(x1, y1, x2, y2, width = wid, fill = col)
    	xtemp = x2
    	ytemp = y2

def drawtext(T, W, Text, col, ang):
    x1 = 15 * T
    y1 = 500 - (16667 * W)
    canvas.create_text(x1, y1, text=Text, angle = ang, fill = col, anchor = 'w')


def motion(event):
    x, y = event.x, event.y
    T, W = round(x/15, 1), round((500-y)/16667, 4)
    if ps.Phi_W(T, W, P)<=1:
        print('{}, {}'.format(T, W))

root = Tk()
#root.resizable(0,0)
root.title("Phisatho Psychro-Chart")

#edge = Canvas(f1, width = 900, height = 600, bg = '#666666',bd = 5,  relief = 'sunken')
edge = Canvas(root, width = 900, height = 600, bg = '#dddddd')
edge.pack()
canvas = Canvas(edge, width = 690, height = 500, bg = 'white', bd = 3, relief = 'sunken')

canvas.place(relx=0.5, rely=0.5, anchor='center')



canvas.bind('<Motion>', motion)

button = Button(root, text = 'Quit', command = root.destroy)
button.pack()

    
Pair = namedtuple("Pair", ["T", "W"])

#Draw W lines
for i in range(31):
    W = 0.001 * i
    WSet = []
    if ps.Tsat_W(W, P) < 0:
        WSet.append(Pair(0, W))
        WSet.append(Pair(46, W))
    else:
        WSet.append(Pair(ps.Tsat_W(W, P), W))
        WSet.append(Pair(46, W))
    drawseries(WSet, 1, '#cccccc')


#Draw RH-10 line
RH10 = []
for T in range(int(Tmax/2) + 1):
    W = ps.W_Phi(2*T, 0.1, P)
    RH10.append(Pair(2*T, W))
drawseries(RH10, 1, 'grey')

#Draw RH-20 line
RH20 = []
for T in range(int(Tmax/2)+1):
    W = ps.W_Phi(2*T, 0.2, P)
    RH20.append(Pair(2*T, W))
drawseries(RH20, 1, 'grey')

#Draw RH-30 line
RH30 = []
for T in range(int(Tmax+1)):
    W = ps.W_Phi(2*T, 0.3, P)
    RH30.append(Pair(2*T, W))
drawseries(RH30, 1, 'grey')

#Draw RH-40 line
RH40 = []
for T in range(int(Tmax+1)):
    W = ps.W_Phi(2*T, 0.4, P)
    RH40.append(Pair(2*T, W))
drawseries(RH40, 1, 'grey')

#Draw RH-50 line
RH50 = []
for T in range(int(Tmax+1)):
    W = ps.W_Phi(2*T, 0.5, P)
    RH50.append(Pair(2*T, W))
drawseries(RH50, 1, 'black')

#Draw RH-60 line
RH60 = []
for T in range(int(Tmax+1)):
    W = ps.W_Phi(2*T, 0.6, P)
    RH60.append(Pair(2*T, W))
drawseries(RH60, 1, 'grey')

#Draw RH-70 line
RH70 = []
for T in range(int(Tmax+1)):
    W = ps.W_Phi(2*T, 0.7, P)
    RH70.append(Pair(2*T, W))
drawseries(RH70, 1, 'grey')

#Draw RH-80 line
RH80 = []
for T in range(int(Tmax+1)):
    W = ps.W_Phi(2*T, 0.8, P)
    RH80.append(Pair(2*T, W))
drawseries(RH80, 1, 'grey')

#Draw RH-90 line
RH90 = []
for T in range(int(Tmax+1)):
    W = ps.W_Phi(2*T, 0.9, P)
    RH90.append(Pair(2*T, W))
drawseries(RH90, 1, 'grey')

#Draw Saturation line
RH100 = []
for T in range(int(Tmax+1)):
    W = ps.W_Phi(2*T, 1.0, P)
    RH100.append(Pair(2*T, W))
drawseries(RH100, 2, 'blue')

#Draw Wet-bulb lines
for Tw in range(5):
    TWSet = []
    Tw = Tw - 5
    W = ps.W_Tw(0, Tw, P)
    TWSet.append(Pair(0, W))
    T2 = ps.T_TwW(Tw, 0.00001, P)
    TWSet.append(Pair(T2, 0.0001))
    drawseries(TWSet, 1, 'skyblue')

for T in range(35):
    TWSet = []
    W = ps.Ws_T(T, P)
    TWSet.append(Pair(T, W))
    T2 = ps.T_TwW(T, 0, P)
    TWSet.append(Pair(T2, 0))
    drawseries(TWSet, 1, 'skyblue')


for H in range (14):
    H = H * 10000
    HSet = []
    T1 = ps.Ts_H(H, P)
    W1 = ps.Ws_T(T1, P)
    HSet.append(Pair(T1, W1))
    T2 = ps.T_HW(H, 0 )
    HSet.append(Pair(T2, 0))
    drawseries(HSet, 1, '#44ff44')
    drawtext(T1+0.5, W1 - 0.0002, 'H='+str(int(H/1000)), '#00aa00', -25)

for V in range(18):
    V = 0.01 * (V) + 0.78
    VSet = []
    T1 = ps.Ts_V(V, P)
    W1 = ps.Ws_T(T1, P)
    VSet.append(Pair(T1, W1))
    T2 = ps.T_VW(V, 0, P)
    VSet.append(Pair(T2, 0))
    drawseries(VSet, 1, '#DA8F44')
#    drawtext(T1+1.1, W1 - 0.0020, 'v='+str(round(V, 3)), '#964B00', -65)
    drawtext(T1+1.1, W1 - 0.0020, 'v='+str(round(V, 3)), '#aaaaaa', -65)

#Draw T lines
for i in range(47):
    x = (i * 15)
    canvas.create_line(x, 550, x, 500 - (16667*ps.Ws_T(i, P)), fill = '#bbbbbb')

#Draw Masks
'''edge.create_rectangle(791, 550, 910, 49, fill='white', outline = 'white')
edge.create_rectangle(0, 00, 910, 49, fill='white', outline = 'white')'''


#Draw T Ticks and labels        
for i in range (24):
	x = 102 + (i * 30)
	edge.create_line(x, 560, x, 565, width = 1)
	edge.create_text(x, 566, text = '%d'%(2*i), anchor = 'n')

#Draw W ticks and labels
for i in range(7):
	y = 547 - (i *83.335)
	edge.create_line(804, y, 809, y, width = 1)
	edge.create_text(810, y, text = '%.3f'% (0.005 * i), anchor = 'w')
   

#Draw Frame 
#edge.create_line(100, 550, 790, 550, width = 2)
#edge.create_line(100, 550, 100,  50, width = 1)
#edge.create_line(100,  50, 790,  50, width = 1)
#edge.create_line(790, 550, 790,  50, width = 2)

    
root.mainloop()

