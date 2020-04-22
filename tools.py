import random
import json
import praw
import emoji
import os

nums = [':keycap_0;',':keycap_1:',':keycap_2:',':keycap_3:',':keycap_4:',':keycap_5:',':keycap_6:',':keycap_7:',':keycap_8:',':keycap_9:',':keycap_10:']

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
	
def help(d):
	#Identifier, command, mod, description
	template = """
		> {0}{1}    Mod:{2}
		> {3}
	"""
	m=''
	
	for i in d.keys():
	#"trigger":["command", "type", "mod(true/false)", "help message"]
		if i == 'identifier':
			continue
		m+=template.format(d['identifier'], i, str(d[i][2]), d[i][3])
	return m
	
def getsub(reddit, filter, sub, number):
	msg = ''
	sublist = [msg]
	link = ''
	gensub = ''
	
	gensub=eval('reddit.subreddit(sub).'+filter+'(limit=int(number))')
	#reddit.subreddit(sub).hot(limit=int(number)
	
	for post in gensub:
		sublist.append(post)
		if post.is_self:
			link = 'self'
		else:
			link = 'link'
		#emoji number, post title
		#is_self, upvotes
		msg += emoji.emojize(nums[len(sublist)-1])+post.title+' \n> '+link+'-post '+str(post.score)+' upvotes \n\n'
	msg += 'React with the number post you want me to fetch'
	sublist[0]=msg
	return sublist
	
	
def getpost(post):
	txtlst = []
	charlimit = 2000
	tmp =''
	if post.is_self:
		tmp = '> '+post.title+'\n'
		text = post.selftext.split('\n')
		for i in text:
			if (len(tmp) + len(i)) > charlimit:
				txtlst.append(tmp)
				tmp = i +'\n'
			else:
				tmp += i + '\n'
				
		if not tmp in txtlst:
			txtlst.append(tmp)
				
	else:
		txtlst.append('> '+post.title+'\n'+post.url)

	return txtlst
	
def save(data, file): #dict, string
	j = json.dumps(data, indent=0)
	f = open(file, 'w')
	f.write(j)
	f.close()
	pass
	
def load(file): #string
	if not os.path.isfile(file):
		print('error: '+file+' missing')
		return
	f = open(file, 'r')
	j = json.load(f)
	f.close()
	return j
	pass