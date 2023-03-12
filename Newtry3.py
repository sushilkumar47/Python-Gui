from ctypes.wintypes import SIZE
from tkinter import *
from turtle import width
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import pandas as pd
# plot function is created for
# plotting the graph in
# tkinter window
# the main Tkinter window
window = Tk()
def plot():
    d = pd.read_csv('yunus.csv')
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
	# placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack(side=LEFT)
	# the figure that will contain the plot
	


	# list of squares
	
    

	# adding the subplot
	

	# plotting the graph
	

	# creating the Tkinter canvas
	# containing the Matplotlib figure
	
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
	
def fun():
    d = pd.read_csv('11.csv')
    x=d['Time']
    y=d['acc']
    sk = Figure(figsize = (3,3),
	        dpi = 100)
           
    plot1 = sk.add_subplot(111)
    plot1.plot(x,y)
    print('Mean:', d.mean().values)
    print('Max:', d.max().values)
    print('Min:', d.min().values)
    
    canvas = FigureCanvasTkAgg(sk,
							master = window)
    canvas.draw()

	# placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack(side=LEFT)





# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("1000x1000")

# button that displays the plot
def ok():
    plot_button = Button(master = window,
					command = plot,
					height = 2,
					width = 10,
					text = "yunus")

# place the button
# in main window
    plot_button.pack()
    button=Button(master=window,
    command=sk,height=2,width = 10,text="11"
    )
    button.pack()
    btn=Button(master=window,
    command=fun,height=2,width = 10,text="sk"
    )
    btn.pack()


btn=Button(master=window,
command=ok,height=2,width = 10,text="ok"
)
btn.pack()



# run the gui
window.mainloop()
