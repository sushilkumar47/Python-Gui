from ctypes.wintypes import SIZE
from tkinter import *
from turtle import width
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import pandas as pd
window = Tk()
def sk():
    d = pd.read_csv('sk.csv')
    x=d['Time']
    y=d['acc']
    fig = Figure(figsize = (3, 3),
	        dpi = 100)
           
    plot1 = fig.add_subplot(111)
    plot1.plot(x,y)
    print('Mean:', d.mean().values)
    print('Max:', d.max().values)
    print('Min:', d.min().values)
    
    canvas = FigureCanvasTkAgg(fig,
							master = window)
    canvas.draw()

	# placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack(side=LEFT)


btn=Button(master=window,
command=sk,height=2,width = 10,text="sk"
)
btn.pack()

window.mainloop()