help_msg = ('''
`!help` - Displays this message
`!changelog`
`!insult <person>` - Generates a random insult
`!coin` - Flips a coin
`!encounter` - Fight a random monster
`!wtf`
`!fresh`
`!inventory` - See what you've got
`!8ball` - Ask it a question
`!give <ammount> @user`- Give a mentioned user gold
`!whisper` - psst
`!buy <item> <ammount>` -try `!buy list` for a list of things you can buy
`!lib` -Madlibs
`!lib rand` - Generate a random madlib

-Dice-
!dice #d#
ex: !dice 1d20, !dice 2d10
''')

mod_help = ('''
These are commands that only mods of s4xbot can use:

`!mint <ammount>` -Give yourself free gold
`!clear busy` -Use this if someone seems to be unable to use any commands
`!stop` -Stops s4xbot
''')

changelog = ('''
v0.3a
-added !lib
-Called an exterminator
''')

buy_list = ('''
Potion - 5g
''')

insult0 = ['Your face looks like', 'You\'re', 'Your mom is']
insult1 = ["a Lazy", "a Stupid", "an Insecure", "an Idiotic", "a Slimy", "a Slutty", "a Smelly", "a Pompous", "a Communist", "a Dicknose", "a Pie-eating", "a Racist", "an Elitist", "a White Trash", "a Drug-Loving", "a Butterface", "a Tone Deaf", "an Ugly", "a Creepy"]
insult2 = ["Douche", "Ass", "Turd", "Rectum", "Butt", "Cock", "Shit", "Crotch", "Bitch", "Prick", "Slut", "Taint", "Fuck", "Dick", "Boner", "Shart", "Nut", "Sphincter" ]
insult3 = ["Pilot", "Canoe", "Captain", "Pirate", "Hammer", "Knob", "Box", "Jockey", "Nazi", "Waffle", "Goblin", "Blossum", "Biscuit", "Clown", "Socket", "Monster", "Hound", "Dragon", "Balloon"]
ball = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']

directions = ['North', 'East', 'South', 'West']

#in order direction, length, width, enemies, doors[0], doors[1]
look_msg = ('''
You stand in a room
Stretching to the {0}, it is {1} feet long, and {2} feet wide
There are {3} enemies here
There are 2 doors in this room
{4} {5}
''')


