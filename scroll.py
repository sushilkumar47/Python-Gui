from tkinter import *

root = Tk()
root.geometry("150x200")

w = Label(root, text ='GeeksForGeeks',
		font = "50")

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack( side = RIGHT,
				fill = Y )

Canvas = Canvas(root,
				yscrollcommand = scroll_bar.set )


	

Canvas.pack( side = LEFT, fill = BOTH )

scroll_bar.config( command = Canvas.yview )

root.mainloop()
