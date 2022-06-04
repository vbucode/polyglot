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
    xlist = []
    tlist = []
    engvar = ""
    ruvar = ""
    def load(self):
        self.engvar, self.ruvar = random.choice(list(d.items()))
        self.xlist.append(self.engvar)
        self.xlist.append(self.ruvar)
        ispl = re.split("\s", self.engvar)
        for i in ispl:
            for j in listforhelp:
                x = j.split(" ")
                if i in x:
                    c = 2
                    self.tlist.append(i)
                    while c > 0:
                        y = random.choice(x)
                        if y not in self.tlist:
                            self.tlist.append(y)
                            c -= 1
        return self.xlist, self.tlist
