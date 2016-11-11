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
v0.2.1a
-Dungeons(wip)
-Can now roll multiple dice at once
-Updated !buy
-Called an exterminator
''')

buy_list = ('''
Potion - 5g
''')

directions = ['North', 'East', 'South', 'West']

#in order direction, length, width, enemies, doors[0], doors[1]
look_msg = ('''
You stand in a room
Stretching to the {0}, it is {1} feet long, and {2} feet wide
There are {3} enemies here
There are 2 doors in this room
{4} {5}
''')


