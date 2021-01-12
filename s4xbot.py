#downloaded api
import discord
import asyncio
import praw
import inflect
import emoji
from pybooru import Danbooru
import basc_py4chan

#built in
import json
import random
import os
from time import localtime, strftime
import sys
import requests
import io
import re
import mimetypes
from requests_toolbelt import MultipartEncoder

#custom api
import tools
import wordgame
import clientcommands
import defaults

#lists and dicts

global localchannel
global localdict
global authinfo
global mods

localchannel = None
systemchannel = None
msgs=[]
cmds=[]
mods=[]
localdict={}
authinfo={}
commands={}

tmpstorage = {}

preload = ['authinfo', 'mods', 'localdict', 'commands']
nums = [':keycap_0;',':keycap_1:',':keycap_2:',':keycap_3:',':keycap_4:',':keycap_5:',':keycap_6:',':keycap_7:',':keycap_8:',':keycap_9:',':keycap_10:']


#reddit = praw.Reddit(client_id=authinfo['redd_id'], client_secret=authinfo['redd_secret'], password=authinfo['redd_pass'], user_agent=authinfo['redd_agent'], username=authinfo['redd_name'])
client = discord.Client()
inflector = inflect.engine()
booru = Danbooru('danbooru')


#---------------------------------------------------------------------------
#wrapped functions
def printlog(msg):
	print((strftime("%Y-%m-%d %H:%M:%S", localtime()))+str(msg))

async def get_message(channel, id):
	tmpstorage['msg'] = await channel.fetch_message(id)

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
	
async def say(channel, msg):
	await channel.send(msg)
	
async def getmsg(channel, id):
	localdict['msg']=await client.get_message(channel, id)
	
async def sublist(message):
	command = message.content.split(' ')
	
	list = tools.getsub(reddit, command[1], command[2], command[3])
	msg = await message.channel.send(list[0])
	
	def check(payload):
		return payload.message_id==msg.id
	
	payload = await client.wait_for('raw_reaction_add', check=check)

	print('got reaction ' +emoji.demojize(payload.emoji.name))
	msglist = tools.getpost(list[nums.index(emoji.demojize(payload.emoji.name))])
	await msg.delete()
	for i in msglist:
		await say(message.channel, i)
	pass

async def stream(sub, channel, existing):
	if localdict['stream']==1:
		say(channel, 'Already streaming. Stop the other stream before starting a new one')
		return
	else:
		localdict['stream']=1

		
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
	
async def postbooru(channel, command):
	if int(command[2]) >10:
		lmt = 10
		await channel.send('List too big, defaulting to list of 10')
	else:
		lmt = int(command[2])
	lst=booru.post_list(tags = command[1], limit=lmt, random = True)
	printlog('returned list of size '+str(len(lst)))
	for i in lst:
		if 'file_url' in i.keys():
			await say(channel, i['file_url'])
		else:
			pass

def mimetype(name):
	exl = name.split()
	ex = exl[len(exl)-1]
	return mimetypes.types_map[ex]

async def chan_stream(channel, board, thread_id):
	#name, timestamp, postno, content
	title_format='**{}** `{}` No.`{}`\n>'
	
	if localdict['stream']==1:
		await say(channel, 'Already streaming. Stop the other stream before starting a new one')
		return
	else:
		localdict['stream']=1

	brd = basc_py4chan.Board(board)
	thread = brd.get_thread(thread_id)
	
	while localdict['stream']==1:
		if not brd.thread_exists(thread_id):
			localdict['stream']=0
			channel.send(":no_entry_sign: Thread has been pruned or deleted")
			return
		new_posts = thread.update()
		for i in range(new_posts):
			post = thread.posts[len(thread.posts)-new_posts+i]
			title_formated = title_format.format(post.name, post.datetime.isoformat(sep=' '), post.post_id)
			msg = discord.Embed(title=title_formated
			                    description=post.text_comment)
			if post.has_file:
				msg.set_image(post.file.thumbnail_url)
				encoder = MultipartEncoder(fields={
					"reqtype": "fileupload",
					"userhash": "",
					"fileToUpload": (post.file.filename_original,io.BytesIO(requests.get(post.file.file_url).content),getmimetype(post.file.filename_original))
				})
				res = requests.post("https://catbox.moe/user/api.php",
				                  data=encoder,
				                  headers={"Content-type": encoder.content_type})
				msg.add_footer(text="Click [here]({}) for the full image".format(res.text))
				await channel.send(embed=msg)
			else:
				await channel.send(post_formated)
		await asyncio.sleep(5)
	pass


async def saveall():
	await say(systemchannel, 'saving all dicts')
	print('saving all dicts')
	
	tools.save(mods, 'mods.json')
	tools.save(localdict, 'localdict.json')
	tools.save(authinfo, 'authinfo.json')
	tools.save(commands, 'commands.json')

async def loadall():
	global authinfo
	global mods
	global localdict
	global localchannel
	global systemchannel
	global commands
	
	authinfo = tools.load('authinfo.json')
	mods = tools.load('mods.json')
	localdict = tools.load('localdict.json')
	commands = tools.load('commands.json')
	
	localchannel = client.get_channel(localdict['localchannel'])
	systemchannel = client.get_channel(localdict['systemchannel'])
	
	await say(systemchannel, 'reloaded configs')
	
async def stop():
	printlog('stopping')
	await saveall()
	try:
		await say(systemchannel, 'stopping')
	except:
		pass
	sys.exit(0)

def fill_joined():
	for i in client.get_all_members():
		localdict['joined'][i.id]='the beginning of time'
	

#---------------------------------------------------------------------------
#events

# @client.event
# async def on_reaction_add(reaction, user):
	# print(emoji.demojize(reaction.emoji))
	# await say(reaction.message.channel, reaction.emoji)

@client.event
async def on_member_remove(member):
	await say(localchannel, 'Goodbye '+member.display_name+'\n'+member.display_name+' was a member of the server since '+localdict['joined'][member.id])
	pass
@client.event	
async def on_member_join(member):
	if member.name.lower().startswith('yobro'):
		await member.add_roles(discord.utils.get(member.guild.roles, name='lost forever'))
		await say(localchannel, 'Sweater guy joined again, so I sent him to a better future')
		pass
	else:
		await say(localchannel, 'Hello '+member.display_name)
		await member.add_roles(discord.utils.get(member.guild.roles, id=localdict['defaultrole']))
	localdict['joined'][member.id]=strftime("%Y-%m-%d %H:%M:%S", localtime())
	pass
	
@client.event
async def on_ready():
	global localchannel
	global systemchannel
	
	localchannel = client.get_channel(localdict['localchannel'])
	systemchannel = client.get_channel(localdict['systemchannel'])
	
	print('Logged in as')
	print('discord: '+ client.user.name + ' ' + str(client.user.id))
	print('reddit: '+ str(reddit.user.me()))
	print('localchannel @ '+str(localchannel))
	print('systemchannel @ '+str(systemchannel))
	print((strftime("%Y-%m-%d %H:%M:%S", localtime())))
	print('------')
	


@client.event
async def on_message(message):
	#bot doesn't reply to itself
	if message.author == client.user:
		#msgs.append(message)
		return
		
	#starts with command identifier
	if message.content.startswith(commands["identifier"]):
		printlog([message.author.name,message.content])
		#cmds.append(message)
		#convert message to list
		command = message.content.split(' ')
		#remove '!'       
		command[0]=command[0][1:]


		#check command[0] in dict
		#corresponding value = do stuff
		#"trigger":["command", "type", "mod(true/false)", "help message"]
		if command[0] in commands:
			if commands[command[0]][2]==True:
				if not message.author.id in mods:
					await say(message.channel,"You don't have permission to use this command")
			if commands[command[0]][1]=='wait':
				await eval(commands[command[0]][0])
			elif commands[command[0]][1]=='notwait':
				eval(commands[command[0]][0])

		#hard coded commands
		if command[0] =='waiteval' and message.author.id in mods:
			await eval(message.content[10:])
		elif command[0] == 'eval' and message.author.id in mods:
			eval(message.content[5:])
			
	pass
	

for i in preload:
	if not os.path.isfile(i+'.json'):
		eval('tools.save(defaults.'+i+', "'+i+'.json")')
		exec(i+'=defaults.'+i, globals())
		print('saving '+i+' default value')
	else:
		exec(i+'= tools.load("'+i+'.json")', globals())
		print('preloaded '+i+'.json')
	
# if not os.path.isfile('authinfo.json'):
	# tools.save(defaults.authinfo, 'authinfo.json')
	# authinfo = defaults.authinfo
	# print('saving authinfo default value')
# else:
	# authinfo = tools.load('authinfo.json')

# if not os.path.isfile('localdict.json'):
	# tools.save(defaults.localdict, 'localdict.json')
	# localdict = defaults.localdict
	# print('saving localdict default value')
# else:
	# localdict = tools.load('localdict.json')

# if not os.path.isfile('mods.json'):
	# tools.save(defaults.mods, 'mods.json')
	# mods = defaults.mods
	# print('saving mods default value')
# else:
	# mods = tools.load('mods.json')
	
# if not os.path.isfile('commands.json'):
	# tools.save(defaults.commands, 'commands.json')
	# commands = defaults.commands
	# print('saving commands default value')
# else:
	# commands = tools.load('commands.json')

reddit = praw.Reddit(client_id=authinfo['redd_id'], client_secret=authinfo['redd_secret'], password=authinfo['redd_pass'], user_agent=authinfo['redd_agent'], username=authinfo['redd_name'])

if authinfo['disc_token'] == 'discord bot token':
	print('Error: Authinfo set to default values. Please edit authinfo.json and reload')
else:
	client.run(authinfo['disc_token'])
