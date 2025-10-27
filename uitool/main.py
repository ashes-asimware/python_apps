import tkinter as tk

BACKGROUNDS=["red","green","blue","yellow","orange"]
FOREGROUNDS=["white","black","gray","purple","pink"]
m=tk.Tk()
for i in range(5):
    b=tk.Button(m,text=" "*10,
                bg=BACKGROUNDS[i],
                fg=FOREGROUNDS[i])
    b.grid(row=i,column=i)
m.mainloop()