import random
import re
import json

listforhelp = ["i you he she we they it",
               "am are is",
               "be was were",
               "have has had",
               "do did does",
               "this that their"]

d = json.loads(data)

def main():
    wl = []
    count = 0
    engvar, ruvar = random.choice(list(d.items()))
    print("\n{}\n".format(ruvar))
    ispl = spliting(engvar)
    for i in ispl:
        for j in listforhelp:
            x = j.split(" ")
            tlist = []
            if i in x:
                c = 2
                tlist.append(i)
                while c > 0:
                    y = random.choice(x)
                    if y not in tlist:
                        tlist.append(y)
                        c -= 1
                print(tlist)
    tr = input("\ntranslate: ")
    if tr == "exit":
        leave()
    wl = spliting(tr)
    for i in wl:
        count += 1
        if i != ispl[count-1]:
            print("\nright answer: {}".format(engvar))
            break
        elif count == len(wl):
            print("\ngood!")
def spliting(text):
    wlist = []
    wlist = re.split("[\W\s]", text)
    return wlist
def leave():
    exit()
while True:
    main()
