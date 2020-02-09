import random

def dice(xdx):
	die = xdx.split('d')
	m = ('Rolling '+die[0]+' d'+die[1])
	total = 0
	for i in range(int(die[0])):
		l = random.randint(1, int(die[1]))
		m += ('\nRolled a '+str(l))
		total+=l
	m+=('\nTotal: '+str(total))
	return m
