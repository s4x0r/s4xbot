authinfo={
	'disc_token':'discord bot token',
	'redd_id':'reddit bot id',
	'redd_pass':'reddit password',
	'redd_secret':'reddit bot secret',
	'redd_agent':'reddit bot name',
	'redd_name':'reddit username'
}

localdict={
	'stream':0,
	'streamprocess':None,
	'localchannel':None,
	'systemchannel':None,
	'defaultrole':None,
	'reply':'0',
	'nou':0,
	'gay':[],
	'flavor':'niichan',
	'cute':'cute', #cute/anticute
	'joined':{}
}

mods=[179787611148255239]

commands={
	'identifier':'!',
    'cute':['say(message.channel,wordgame.cute(localdict["flavor"], localdict["cute"]))', 'wait', False, 'Gives a compliment to the flavor of the day'],
    '8ball':['say(message.channel, wordgame.ball())', 'wait', False, 'Get advice from the magic 8-ball'],
    'help':['say(message.channel, tools.help(commands))', 'wait', False, 'Displays this message'],
    'insult':['say(message.channel, wordgame.insult())', 'wait', False, 'Generates a random insult'],
    'dice':['say(message.channel, tools.dice(command[1]))', 'wait', False, 'Rolls dice. Usage: `!dice #d#`'],
	'r':['say(message.channel, tools.dice(command[1]))', 'wait', False, 'Shorter form of dice. Usage: `!r #d#`'],
    'say':['saythis(message)', 'wait', False, 'Make me say something'],
	'coin':['say(message.channel, random.choice(["Heads","Tails"]))', 'wait', False, 'Flips a coin'],
	'fresh':['say(message.channel, "Now, this is a story all about how My life got flipped-turned upside down And I\'d like to take a minute Just sit right there I\'ll tell you how I became the prince of a town called Bel-Air")', 'wait', False, 'Fresh Prince rap'],
	#'nou':['say(message.channel, ("no u:[ "+str(localdict["nou"])))', 'wait', False, 'Counts how many times "no u" has been said'],
	#'gay':['say(message.channel, str(localdict["gay"]))', 'wait', False, 'Lets you know who's gay'],
	'lib':['say(message.channel, wordgame.gen())', 'wait', False, 'Generates a random sentence'],
	'getid':['say(message.channel, message.author.id)', 'wait', False, 'Tells you your discord user ID'],
	'haiku':['say(message.channel, wordgame.haiku())', 'wait', False, 'Generates a random haiku'],
	
	'get':['sublist(message)', 'wait', False, 'Gets top posts from a subreddit. Usage: `!get <filter> <subreddit> <number(max 10)>`\nFilters: `hot, new, rising, controversial, top, gilded`'],
	'stream':['stream(command[1], message.channel, int(command[2]))', 'wait', True, 'Gets a constant stream of new posts from a subreddit. Usage: `!stream <subreddit> <ignore existing(0/1)>`'],
	'stopstream':['savetodict("stream", 0)', 'notwait', True, 'Halts a running reddit stream'],
	'booru':['postbooru(message.channel, command)', 'wait', False, 'Dump images from danbooru. Only supports a single search term. Usage: `!booru <search term> <#>`'],
	'4chan':['chan_stream(message.channel, command[1], int(command[2]))', 'wait', True, 'Streams a 4chan thread in real time. Usage:`!4chan <board> <thread id>`'],
	
	#'autoreply':['commands.autoreply[message.author.name]=message.content[10:[]'],
	'setflavor':['savetodict("flavor", message.content[11:)', 'notwait', False, 'Sets the flavor of the day'],
	'localchannel':['setlocalchannel(message.channel)', 'notwait', True, 'Sets the local channel'],
	'systemchannel':['savetodict("systemchannel", message.channel.id)', 'notwait', True, 'Sets the system channel'],
	'defaultrole' :['savetodict("defaultrole", int(command[1][3:-1]))', 'notwait', True, 'Sets the default role'],
	
	'stop':['stop()', 'wait', True, 'Stops the bot'],
	'mod':['mod(command[1])', 'wait', True, 'Add a user ID to the mod list'],
	'save':['saveall()', 'wait', True, 'Saves current configs to file'],
	'load':['loadall()', 'wait', True, 'Loads configs from file'],
	'announce':['say(client.get_channel(int(command[1][2:-1])), message.content.split("&")[1])', 'wait', True, 'Announce a message to a channel. Usage:`!announce #channel &message`']
}