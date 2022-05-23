import random
import re
import json

listforhelp = ["i you he she we they",
               "me him her us them",
               "am are is",
               "be was were",
               "have has had",
               "will, not, shall",
               "do doesn't did't did does",
               "this that their",
               "what who where when why how"]

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
        ispl = re.split("\s", engvar)
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
