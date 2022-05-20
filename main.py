import tkinter
import re
from polyglot import Polyglot

root = tkinter.Tk()
root.title("Polyglot")
root.geometry("405x230")
root.configure(bg = "black")

def chek():
    global po
    tr = ""
    wl = []
    count = 0
    tr = ent.get()
    wl = re.split("[\W\s]", tr)
    pol = re.split("[\W\s]", po[0])
    for i in wl:
        count += 1
        if i != pol[count-1]:
            txt = "right answer: " + po[0]
            lbl3.configure(text = txt)
            break
        elif count == len(wl):
            lbl3.configure(text = "Good!")

def step1():
    global po
    p = Polyglot()
    po = p.onel()
    pt = p.twol()
    pos = " ".join(po[1])
    pts = " ".join(pt)
    lbl1.configure(text = pos)
    lbl2.configure(text = pts)

lbl1 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl2 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl3 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
ent = tkinter.Entry(root, width = 40)
ent.focus()
btn1 = tkinter.Button(root, text = "next", bg = "gray", command = chek)

lbl1.pack()
lbl2.pack()
lbl3.pack()
ent.place(x = 5, y = 190 )
btn1.place(x = 340, y = 185)

step1()

if __name__ == "__main__":
    root.mainloop()
