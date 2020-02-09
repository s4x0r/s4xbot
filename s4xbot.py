import config
import commands
import clientcommands
import text
import dungeon
import discord
import asyncio
import random
import tools
import wordgame
from time import localtime, strftime

#lists and dicts
msgs=[]
cmds=[]
localdict={
	'reply':'0',
	'nou':0,
	'gay':[],
	'flavor':'niichan',
	'cute':'cute' #cute/anticute
}

client = discord.Client()

#wrapped functions
def savetodict(key, val):
	localdict[key]=val
	print('set <'+key+'> to <'+str(val)+'>')

def printlog(msg):
	print((strftime("%Y-%m-%d %H:%M:%S", localtime()))+str(msg))
	

async def say(channel, msg):
	await client.send_message(channel, msg)

async def help(channel):
	m = ''
	for i in commands.waitcommands.keys():
		m+=('!'+i+'\n')
	await say(channel, m)
	
#discord already has a method for this
async def purge():
	for i in msgs:
		try:
			await client.delete_message(i)
		except:
			pass
	msgs.clear()
	for i in cmds:
		try:
			await client.delete_message(i)
		except:
			pass
	cmds.clear()
	
async def saythis(message):
	#specifically for use with !say
	await say(message.channel, message.content[5:])
	await client.delete_message(message)
	
async def getmsg(channel, id):
	localdict['msg']=await client.get_message(channel, id)

def setflavor(j):
	localdict['flavor'] = j
	print('set flavor to ' + j)

def togglereply(localdict):
	if localdict['reply'] == '1':
		localdict['reply'] = '0'
		return localdict['reply']
	if localdict['reply'] == '0':
		localdict['reply'] = '1'
		return localdict['reply']
    
@client.event
async def on_ready():
	reply = 0
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print((strftime("%Y-%m-%d %H:%M:%S", localtime())))
	print('------')

@client.event
async def on_message(message):
	#bot doesn't reply to itself
	if message.author == client.user:
		msgs.append(message)
		return
		
	#starts with '!'
	if message.content.startswith('!'):
		printlog([message.author.name,message.content])
		cmds.append(message)
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

		elif command[0] in commands.clientcommands:
			await eval(commands.clientcommands[command[0]])

		#hard coded commands
		if command[0] == 'autoreact':
			msg = await client.send_message(message.channel, 'react to me with the autoreact you want')
			res = await client.wait_for_reaction(message=msg)
			await say(message.channel, res.reaction.emoji)
			print(res.reaction.custom_emoji)
			if res.reaction.custom_emoji==True:
				emoji= res.reaction.emoji
			else:
				emoji = res.reaction.emoji
			
			print(emoji)
			commands.nametriggers[message.author.name]=emoji
			
		elif command[0] == 'reply':
			await say(message.channel, togglereply(localdict))
			print(localdict['reply'])
		elif command[0] =='waiteval':
			await eval(message.content[10:])
		elif command[0] == 'eval':
			eval(message.content[5:])

	#auto react
	if message.author.name in commands.nametriggers:
		await client.add_reaction(message, commands.nametriggers[message.author.name])
		printlog([commands.nametriggers[message.author.name]])
	
	if message.author.name in commands.autoreply and localdict['reply'] == '1':
		await say(message.channel, commands.autoreply[message.author.name])
	
	#hard coded chattriggers
	if 'no u' in message.content:
		localdict['nou']+=1
		printlog([message.author.name,'no u',str(localdict['nou'])])
	# elif ("i'm" or "im")in message.content.lower() and 'gay' in message.content.lower():
		# await say(message.channel, '@everyone '+message.author.name+' is gay' )
		# if message.author.name not in localdict['gay']:
			# localdict['gay'].append(message.author.name)
	elif 'y-you, too' in message.content.lower() or 'y-you too' in message.content.lower():
		await say(message.author, 'faggot')
	elif 'is' in message.content:
		msg = message.content.split(' is ')
		await say(message.channel, 'ur mum is '+msg[1])
	elif 'evil' in message.content:
		await say(message.channel, '⛧'+message.author.name+'⛧')
		
	elif 'dick' in message.content.lower():
		await say(message.channel, text.dickmsg)
client.run(config.token)
