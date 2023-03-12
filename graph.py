from tkinter import*
import matplotlib.pyplot as plt

root=Tk()
root.title("sushil project")
root.geometry("800x600")

def graph():
    # house_prices=np.random.normal(2000,3000,5000)
    with open('yunus.csv') as f: 
        # f = csv.reader(f, delimiter=',') 
          t=f.read()
        #   print(t)
          f.close()       
    plt.plot(t)
    plt.show()

my_buttom=Button(root,text="graph it!",command=graph)
my_buttom.pack()
root.mainloop()