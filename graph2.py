import pandas as pd
from tkinter import*
from matplotlib import pyplot as plt


root=Tk()
root.geometry("400x600")

def fun():
    d = pd.read_csv('yunus.csv')
    x=d['Time']
    y=d['acc']
    print('Mean:', d.mean().values)
    print('Max:', d.max().values)
    print('Min:', d.min().values)
    plt.plot(x,y)
    plt.show()

plt.title('graph')
plt.xlabel('Time')
plt.ylabel('acceleration')

Button(root,text="graph it!",command= fun).pack(pady=40,padx=40)
plt.tight_layout()
 
root.mainloop()





 
  
# plt.style.use('seaborn')

# data = pd.read_csv('yunus.csv')
# x=data["Time"]
# y=data['acc']
# plt.plot(x,y)
# plt.show()
    








# data = pd.read_csv('yunus.csv')
# x=data["Time"]
# y=data['acc']

# plt.plot(x,y)

# plt.title('graph')
# plt.xlabel('Time')
# plt.ylabel('acceleration')

