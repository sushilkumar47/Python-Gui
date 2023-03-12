from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import pandas as pd
# plot function is created for
# plotting the graph in
# tkinter window
# the main Tkinter window
window =Tk()

def plot():
    d = pd.read_csv('yunus.csv')
    x=d['Time']
    y=d['acc']
    fig = Figure(figsize = (3,3),
	        dpi = 100)
   
    plot1 = fig.add_subplot(111)
    plot1.plot(x,y, linewidth=0.5)
    
    canvas = FigureCanvasTkAgg(fig,
							master = window)
   

    canvas.draw()

	# placing the canvas on the Tkinter window
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
    fig = Figure(figsize = (3,3),
	        dpi = 100)
           
    plot1 = fig.add_subplot(111)
    plot1.plot(x,y, linewidth=0.5)
    
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
    plot1.plot(x,y, linewidth=0.5)
    
    canvas = FigureCanvasTkAgg(sk,
							master = window)
    
    canvas.draw()

	# placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack(side=LEFT)

	
    


# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("1920x1080")

# button that displays the plot
def ok():
    plot_button = Button(master = window,
					command = plot,
					height = 2,
					width = 10,
					text = "yunus")
   
    # place the button
    # in main window
    plot_button.place(x=0, y=50)
    
    button=Button(master=window,
    command=sk,height=2,width = 10,text="11"
    )
    button.place(x=0, y=90)
    btn=Button(master=window,
    command=fun,height=2,width = 10,text="sk"
    )

    btn.place(x=0, y=130)
    


btn=Button(master=window,
command=ok,height=2,width = 10,text="ok"
)
btn.place(x=0, y=0)
# btn.pack()



# run the gui
window.mainloop()
