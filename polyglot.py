import random
import re
import json

listforhelp = ["i you he she we they it",
               "am are is",
               "be was were",
               "have has had",
               "do did does",
               "this that their"]

with open("data.json", "r") as file:
    d = json.load(file)

class Polyglot:
    def _init_(self):
        pass
    def onel(self):
        xlist = []
        global engvar
        global ruvar
        engvar, ruvar = random.choice(list(d.items()))
        xlist.append(engvar)
        xlist.append(ruvar)
        return xlist
    def twol(self):
        global engvar
        tlist = []
        ispl = re.split("[\W\s]", engvar)
        for i in ispl:
            for j in listforhelp:
                x = j.split(" ")
                if i in x:
                    c = 2
                    tlist.append(i)
                    while c > 0:
                        y = random.choice(x)
                        if y not in tlist:
                            tlist.append(y)
                            c -= 1
        return tlist
