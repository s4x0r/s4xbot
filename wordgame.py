import wordlist
import random
import libs

adlibs = []
class adlib:
    def __init__(self, name, parts, body):
        self.name = name
        self.parts = parts
        self.body = body
    def rand(self):
        j=[]
        for x in range(len(self.parts)):
                
            if self.parts[x] == "number":
                j.append(str(random.randint(0, 100)))

            else:
                j.append(random.choice(wordlist.wlist[self.parts[x]]))
        return self.body.format(*j)

#generate random lib
def gen():
    d=random.choice(libs.adlibs)
    return adlib(*d).rand()

def rand():
    d=random.choice(libs.adlibs)
    return adlib(*d)
    

def insult():
    #r = random.randint(1, 3)
    r=2
    if r == 1:
        m=[]
        m.append(random.choice(wordlist.wlist['insult0']))
        m.append(random.choice(wordlist.wlist['insult1']))
        m.append(random.choice(wordlist.wlist['insult2']))
        m.append(random.choice(wordlist.wlist['insult3']))

        insult ="{0} {1} {2} {3}"
        return insult.format(*m)

    elif r == 2:
        m=[]
        m.append(random.choice(wordlist.wlist['shinsult0']))
        m.append(random.choice(wordlist.wlist['shinsult1']))
        m.append(random.choice(wordlist.wlist['shinsult2']))
        m.append(random.choice(wordlist.wlist['shinsult3']))

        insult ="{0} {1} {2} {3}"
        return insult.format(*m)
    
    elif r == 3:
        lib = rand()
        while lib.name != "Insults":
            lib = rand()
        return lib.rand()
    
def search(term):
    l=[]
    for i in libs.adlibs:
        if term.lower() in i[0].lower():
            l.append(adlib(*i))
    return l

def searchrand(term):
    l=[]
    for i in libs.adlibs:
        if i[0] == term:
            l.append(adlib(*i))
    return random.choice(l)
    
