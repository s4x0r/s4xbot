import wordlist
import random

adlibs = []
class adlib:
    def __init__(self, name, parts, body):
        self.name = name
        self.parts = parts
        self.body = body
    def rand(self):
        j=[]
        for x in range(len(self.parts)):
            if self.parts[x] == "noun":
                j.append(random.choice(wordlist.noun))
            elif self.parts[x] == "nouns":
                j.append(random.choice(wordlist.nouns))
            elif self.parts[x] == "schoolsubject":
                j.append(random.choice(wordlist.schoolsubject))
                
            elif self.parts[x] == "bodypart":
                j.append(random.choice(wordlist.bodypart))
            elif self.parts[x] == "bodyparts":
                j.append(random.choice(wordlist.bodyparts))
            elif self.parts[x] == "verb":
                j.append(random.choice(wordlist.verb))
            elif self.parts[x] == "verbs":
                j.append(random.choice(wordlist.verbs))
            elif self.parts[x] == "verbed":
                j.append(random.choice(wordlist.verbed))
            elif self.parts[x] == "verbing":
                j.append(random.choice(wordlist.verbing))
            elif self.parts[x] == "occupation":
                j.append(random.choice(wordlist.occupation))
            
            elif self.parts[x] == "adjective":
                j.append(random.choice(wordlist.adjective))
            elif self.parts[x] == "number":
                j.append(str(random.randint(0, 100)))
        return self.body.format(*j)


adlibs.append(adlib("Proverbs", ["adjective", "verb"], "A woman's advice is no {0} thing, but he who won't {1} it is a fool."))
adlibs.append(adlib("Proverbs", ["noun", "adjective"], "Absence makes the {0} grow {1} -er."))
adlibs.append(adlib("Proverbs", ["noun", "verbs", "noun"], "A(n) {0} never {1} far from the {2}."))
adlibs.append(adlib("Proverbs", ["noun", "adjective"], "Anyone can hold the {0} when the sea is {1} ."))
adlibs.append(adlib("Proverbs", ["noun", "number", "noun"], "A(n) {0} in hand is worth {1} in the {2} ."))
adlibs.append(adlib("Proverbs", ["adjective", "verbs"], "A(n) {0} mouth {1} no feet."))
adlibs.append(adlib("Proverbs", ["adjective", "noun", "adjective", "nouns"], "A(n)A/An {0} {1} believes anything, but a {2} {1} gives thought to his {3}."))
adlibs.append(adlib("Proverbs", ["noun", "verbs"], "A {0} in time {1} nine." ))
adlibs.append(adlib("Einstien", ["adjective", "adjective", "noun", "nouns"], "Any intelligent fool can make things {0} , more {1}, and more violent. It takes a touch of genius -- and a lot of {2} -- to move in the opposite {3}."))
adlibs.append(adlib("Einstien", ["noun", "adjective"], "Reality is merely a/an {0}, albeit a very {1} one."))
adlibs.append(adlib("Einstien", ["nouns", "nouns"], "Great {0} have often encountered violent opposition from weak {1}."))
adlibs.append(adlib("Einstien", ["noun", "occupation"], "Technological progress is like an {0} in the hands of a pathological {1}."))
adlibs.append(adlib("Einstien", ["noun", "verb", "schoolsubject", "adjective"], "No, this {0} won`t work... How on earth are you ever going to {1} in terms of chemistry and {2} so important a biological phenomenon as {3} love?"))
adlibs.append(adlib("Einstien", ["noun", "verbing", "bodypart", "occupation"], "The release of {0} power has changed everything except our way of {1}... the solution to this problem lies in the {2} of mankind. If only I had known, I should have become a/an {3}."))


def rand():
    d=random.choice(adlibs)
    return d.rand()
