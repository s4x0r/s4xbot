#downloaded api
import discord
import asyncio
import praw
import inflect
import emoji
from pybooru import Danbooru

#built in
import json
import random
import os
from time import localtime, strftime
import sys

#custom api
import tools
import wordgame
import commands
import clientcommands
import text

#lists and dicts

global localchannel
global localdict
global authinfo
global mods

localchannel = None
msgs=[]
cmds=[]
mods=[179787611148255239]
localdict={
	'stream':0,
	'streamprocess':None,
	'localchannel':None,
	'reply':'0',
	'nou':0,
	'gay':[],
	'flavor':'niichan',
	'cute':'cute' #cute/anticute
}
nums = [':keycap_0;',':keycap_1:',':keycap_2:',':keycap_3:',':keycap_4:',':keycap_5:',':keycap_6:',':keycap_7:',':keycap_8:',':keycap_9:',':keycap_10:']

authinfo={
	'disc_token':'discord bot token',
	'redd_id':'reddit bot id',
	'redd_pass':'reddit password',
	'redd_secret':'reddit bot secret',
	'redd_agent':'reddit bot name',
	'redd_name':'reddit username'
}

reddit = praw.Reddit(client_id=authinfo['redd_id'], client_secret=authinfo['redd_secret'], password=authinfo['redd_pass'], user_agent=authinfo['redd_agent'], username=authinfo['redd_name'])
client = discord.Client()
inflector = inflect.engine()
booru = Danbooru('danbooru')

#---------------------------------------------------------------------------
#wrapped functions
def savetodict(key, val):
	localdict[key]=val
	print('set <'+key+'> to <'+str(val)+'>')
	
async def mod(id):
	mods.append(int(id))
	await say(localchannel, 'Added '+client.get_user(id).name+' to mods')
	
def setlocalchannel(channel):
	global localchannel
	localdict['localchannel'] = channel.id
	localchannel = channel
	pass

def setflavor(j):
	localdict['flavor'] = j
	print('set flavor to ' + j)
	
def printlog(msg):
	print((strftime("%Y-%m-%d %H:%M:%S", localtime()))+str(msg))
	

async def say(channel, msg):
	await channel.send(msg)

	
async def getmsg(channel, id):
	localdict['msg']=await client.get_message(channel, id)
	
	
def getsub(filter, sub, number):
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

async def stream(sub, channel, existing):
	subreddit = reddit.subreddit(sub)
	for post in subreddit.stream.submissions(skip_existing = existing, pause_after = 0):
		await channel.trigger_typing()
		if localdict['stream']==0:
			printlog('stream stopped')
			break
		elif post is None:
			pass
		else:
			await say(channel, post.title+'\n'+post.url)
			printlog(' post')
	
def save(data, file): #dict, string
	j = json.dumps(data)
	f = open(file, 'w')
	f.write(j)
	f.close()
	pass

async def saveall():
	await say(localchannel, 'saving all dicts')
	print('saving all dicts')
	save(mods, 'mods.json')
	save(localdict, 'localdict.json')
	save(authinfo, 'authinfo.json')

def load(file): #string
	if not os.path.isfile(file):
		print('error: '+file+' missing')
		return
	f = open(file, 'r')
	j = json.load(f)
	f.close()
	return j
	pass
	
async def stop():
	printlog('stopping')
	await saveall()
	try:
		await say(localchannel, 'stopping')
	except:
		pass
	sys.exit(0)
#---------------------------------------------------------------------------
#events

# @client.event
# async def on_reaction_add(reaction, user):
	# print(emoji.demojize(reaction.emoji))
	# await say(reaction.message.channel, reaction.emoji)

@client.event
async def on_member_remove(member):
	await say(localchannel, 'Goodbye '+member.display_name)
	pass
@client.event	
async def on_member_join(member):
	await say(localchannel, 'Hello '+member.display_name)
	pass

	
@client.event
async def on_ready():
	global localchannel
	localchannel = client.get_channel(localdict['localchannel'])
	print('Logged in as')
	print('discord: '+ client.user.name + ' ' + str(client.user.id))
	print('reddit: '+ str(reddit.user.me()))
	print('localchannel @ '+str(localchannel))
	print((strftime("%Y-%m-%d %H:%M:%S", localtime())))
	print('------')
	


@client.event
async def on_message(message):
	#bot doesn't reply to itself
	if message.author == client.user:
		#msgs.append(message)
		return
		
	#starts with '!'
	if message.content.startswith('!'):
		printlog([message.author.name,message.content])
		#cmds.append(message)
		#convert message to list
		command = message.content.split(' ')
		#remove '!'       
		command[0]=command[0][1:]


		#check command[0] in dict
		#corresponding value = do stuff
		if command[0] in commands.waitcommands:
			await eval(commands.waitcommands[command[0]])
		elif command[0] in commands.notwaitcommands:
			eval(commands.notwaitcommands[command[0]])
		elif command[0] in commands.modcommands and message.author.id in mods:
			await eval(commands.modcommands[command[0]])
			

		#hard coded commands
		if command[0] =='waiteval' and message.author.id in mods:
			await eval(message.content[10:])
		elif command[0] == 'eval' and message.author.id in mods:
			eval(message.content[5:])
		
		elif command[0]=='get':
			if len(command) != 4:
				await say(message.channel, 'Usage: `!get filter subreddit number(max 10)`')
			elif int(command[3]) > 10:
				await say(message.channel, 'Usage: `!get filter subreddit number(max 10)`')
			else:
				list = getsub(command[1], command[2], command[3])
				msg = await message.channel.send(list[0])
				
				def check(payload):
					return payload.message_id==msg.id
				
				payload = await client.wait_for('raw_reaction_add', check=check)

				print('got reaction ' +emoji.demojize(payload.emoji.name))
				msglist = getpost(list[nums.index(emoji.demojize(payload.emoji.name))])
				await msg.delete()
				for i in msglist:
					await say(message.channel, i)
		
		elif command[0] == 'stream':
			localdict['stream']=1
			await stream(command[1], message.channel, int(command[2]))
		elif command[0] == 'stopstream':
			localdict['stream'] = 0
		
		elif command[0] =='booru':
			lst=booru.post_list(tags = command[1], limit=int(command[2]))
			printlog('returned list of size '+str(len(lst)))
			for i in lst:
				if 'file_url' in i.keys():
					await say(message.channel, i['file_url'])
				else:
					pass
		
		elif command[0] == 'gettitle':
			if len(command) != 3:
				await say(message.channel, 'Usage: `!gettitle subreddit number`')
			else:
				for post in reddit.subreddit(command[1]).hot(limit = int(command[2])):
					await say(message.channel, post.title)
	pass


	

if not os.path.isfile('authinfo.json'):
	save(authinfo, 'authinfo.json')
	print('saving authinfo default value')
else:
	authinfo = load('authinfo.json')

if not os.path.isfile('localdict.json'):
	save(localdict, 'localdict.json')
	print('saving localdict default value')
else:
	localdict = load('localdict.json')

if not os.path.isfile('mods.json'):
	save(mods, 'mods.json')
	print('saving mods default value')
else:
	mods = load('mods.json')

reddit = praw.Reddit(client_id=authinfo['redd_id'], client_secret=authinfo['redd_secret'], password=authinfo['redd_pass'], user_agent=authinfo['redd_agent'], username=authinfo['redd_name'])

if authinfo['disc_token'] == 'discord bot token':
	print('Error: Authinfo set to default values. Please edit authinfo.json and reload')
else:
	client.run(authinfo['disc_token'])
