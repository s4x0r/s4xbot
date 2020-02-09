waitcommands={
    'cute':'say(message.channel,wordgame.cute(localdict["flavor"], localdict["cute"]))',
    'changelog':'say(message.channel, text.changelog)',
    '8ball':'say(message.channel, random.choice(text.ball))',
    'help':'help(message.channel)',
    'insult':'say(message.channel, wordgame.insult())',
    'dice':'say(message.channel, tools.dice(command[1]))',
	'r':'say(message.channel, tools.dice(command[1]))',
    'purge':'purge()',
    'say':'saythis(message)',
	'coin':'say(message.channel, random.choice(["Heads","Tails"]))',
	'fresh':'say(message.channel, "Now, this is a story all about how My life got flipped-turned upside down And I\'d like to take a minute Just sit right there I\'ll tell you how I became the prince of a town called Bel-Air")',
	'nou':'say(message.channel, ("no u: "+str(localdict["nou"])))',
	'gay':'say(message.channel, str(localdict["gay"]))',
	'lib':'say(message.channel, wordgame.gen())'
    }

notwaitcommands={
	'autoreply':'commands.autoreply[message.author.name]=message.content[10:]',
	'stop':'exit()',
	'setflavor':'setflavor(message.content[11:])',
	'localchannel':'savetodict("channel", message.channel)'
    }

nametriggers={
    '1The Love Box':':pomfthicc:544378144019316738',
    '1kase': ':kaseiscuteandilovehimsomuch:544711648368132106',
	'#Mordred':'☕'
    }

autoreply={
	'#emo queen supreme':'I get off to imagining that I go back in time to maybe medievaw time ow anceint wome and then i wick the cownews of the houses (the outside that is pointing to the stweet) and i just get aww the diwt and dust in my mouth i mean it just feews so humbew',
	'Atalanta':'desu nya~~',
	'Chi-chan':'Y-you, too'
}

chattriggers={
    'beer':''
    }

complexcommands={
    }

clientcommands={
    'react':'clientcommands.react(client, message.channel)',
    'repeat':'clientcommands.repeat(client, message.channel, msgs)'
    }
