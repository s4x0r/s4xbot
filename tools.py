import random

def dice(amt, die):
    m = ('Rolling '+str(amt)+' d'+str(die))
    for i in range(amt):
            l = random.randint(1, die)
            m += ('\nRolled a '+str(l))
    return m
