from tkinter import *
from math import sin,cos,radians
import json
def key(e):
    k=e.keysym
    if k=="Escape":
        root.destroy()
def load():
    f=open("words.json")
    return json.load(f)
data=load()
root=Tk()
root.title("言葉のグラフ")
c=Canvas(root,width=1000,height=800)
c.pack()

for i,j in zip(range(0,360,int(360/len(data["words"]))),data["words"]):
    x=cos(radians(i))*
root.bind("<Key>",key)
root.mainloop()
