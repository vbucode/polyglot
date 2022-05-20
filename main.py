import tkinter
import re
from polyglot import Polyglot

root = tkinter.Tk()
root.title("Polyglot")
root.geometry("430x180")
root.configure(bg = "black")
flag = 0

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
            lbl3.configure(text = ent.get())
            lbl4.configure(text = txt)
            break
        elif count == len(wl):
            lbl3.configure(text = po[0])
            lbl4.configure(text = "Good!")
    ent.delete(0, "end")

def step():
    global po
    p = Polyglot()
    po = p.onel()
    pt = p.twol()
    pos = " ".join(po[1])
    pts = " ".join(pt)
    lbl1.configure(text = pos)
    lbl2.configure(text = pts)
    lbl3.configure(text = "")
    lbl4.configure(text = "")

def start():
    global flag
    if flag == 0:
        btn1["text"] = "enter"
        flag = 1
        step()
    else:
        btn1["text"] = "next"
        chek()
        flag = 0

lbl1 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl2 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl3 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
lbl4 = tkinter.Label(root, text = "", fg = "yellow", bg = "black")
ent = tkinter.Entry(root, width = 40)
ent.focus()
btn1 = tkinter.Button(root, text = "enter", bg = "gray", command = start)

lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl4.pack()
ent.place(x = 15, y = 100 )
btn1.place(x = 350, y = 96)

start()

if __name__ == "__main__":
    root.mainloop()
