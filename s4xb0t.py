#Link to join a server
#https://discordapp.com/oauth2/authorize?client_id=217887176308817920&scope=bot&permissions=0

import dungeon
import discord
import asyncio
import random

client = discord.Client()

directions = {0:'North', 1:'East', 2:'South', 3:'West'}
insult1 = ["a Lazy", "a Stupid", "an Insecure", "an Idiotic", "a Slimy", "a Slutty", "a Smelly", "a Pompous", "a Communist", "a Dicknose", "a Pie-eating", "a Racist", "an Elitist", "a White Trash", "a Drug-Loving", "a Butterface", "a Tone Deaf", "an Ugly", "a Creepy"]
insult2 = ["Douche", "Ass", "Turd", "Rectum", "Butt", "Cock", "Shit", "Crotch", "Bitch", "Prick", "Slut", "Taint", "Fuck", "Dick", "Boner", "Shart", "Nut", "Sphincter" ]
insult3 = ["Pilot", "Canoe", "Captain", "Pirate", "Hammer", "Knob", "Box", "Jockey", "Nazi", "Waffle", "Goblin", "Blossum", "Biscuit", "Clown", "Socket", "Monster", "Hound", "Dragon", "Balloon"]
ball = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
help_msg = ('''\
!help - Displays this message
!changelog
!insult person - Generates a random insult
!coin - Flips a coin
!encounter - Fight a random monster
!wtf
!fresh
!inventory - See what you've got
!8ball - Ask it a question
!give - Give a mentioned user gold
-ex !give 5 @s4x0r
!whisper - psst
!buy potion 5

-Dice-
!1d#
ex: 1d2, 1d6, 1d20
''')

#in order direction, length, width, enemies, doors[0], doors[1]
look_msg = ('''
You stand in a room
Stretching to the {0}, it is {1} feet long, and {2} feet wide
There are {3} enemies here
There are 2 doors in this room
{4} {5}
''')

changelog = ('''
v0.2.1a
-Dungeons(wip)
-Rewrote !inventory
-Fixed giving negative money
-Added !buy
-Released bugs back into their natrual habitat
''')

players = {}
user_gold = {}
user_potions={}
busy_users=[]


@client.event
@asyncio.coroutine
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

"""
@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith(''):
"""
 
@client.event
@asyncio.coroutine
def on_message(message):

    if message.author.name == 's4x0r':
        if message.content.startswith('!stop'):
            exit()
        elif message.content.startswith('!clear busy'):
            busy_users.clear()
        elif message.content.startswith('!mint'):
            l=message.content.split(' ')
            if message.author not in players:
                players[message.author].gold = 0
            players[message.author].gold += int(l[1])

    if message.author == client.user:
        return
    elif message.author.name in busy_users:
        return

    elif message.content.startswith('!help'):
        yield from client.send_message(message.channel, help_msg)

    elif message.content.startswith('!changelog'):
        yield from client.send_message(message.channel, changelog)

    elif message.content.startswith('s4xb0t, introduce yourself'):
        yield from client.send_message(message.channel, '```Hi everyone! I\'m s4x0r\'s little buddy, s4xb0t. Nice to meet you all```')

    elif message.content.startswith('!wtf'):
        yield from client.send_message(message.channel, '```Wtf did you just fucking say about me, you little admin? I’ll have you know I graduated top of my class at Shadowvale, and I’ve been involved in numerous raids on River City I have over 300 confirmed mob kills. I am trained in Dual Weilding and I’m the top sniper in the all of Arcane. You are nothing to me but just another mob. I will wipe you out with precision the likes of which has never been seen before on this map mark my words. You think you can get away with saying that to me over the chat? Think again. As we speak I am contacting my secret network of Mojang employees and your IP is being traced right now so you better prepare for the storm, endermite. The storm that wipes out the pathetic little thing you call your base. You’re dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of Mytos Corp and I will use it to its full extent to wipe you off the face of the map If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your tongue. But you couldn’t, you didn’t, and now you’re paying the price, you idiot. I will rain fury all over you and you will drown in it. You’re dead, kiddo```')

    elif message.content.startswith('!fresh'):
        yield from client.send_message(message.channel, '```Now, this is a story all about how \nMy life got flipped-turned upside down \nAnd I\'d like to take a minute \n Just sit right there \nI\'ll tell you how I became the prince of a town called Bel-Air```')

    elif message.content.startswith('!whisper'):
        yield from client.send_message(message.author, 'psst')

    elif message.content.startswith('!say'):
        msg = message.content[5:]
        yield from client.send_message(message.channel, msg)

    elif message.content.startswith('!8ball'):
        j = random.randint(0,11)
        yield from client.send_message(message.channel, ball[j])
        
    elif message.content.startswith('!insult'):
        name = message.content[8:]
        j = random.randint(0,18)
        k = random.randint(0,17)
        l = random.randint(0,18)
        if name == None:
            yield from client.send_message(message.channel, '```You\'re ' + insult1[j] + ' ' + insult2[k] + ' ' + insult3[l] + '```')
        else:
            yield from client.send_message(message.channel, '```'+name+' is '+insult1[j]+' '+insult2[k]+' '+insult3[l]+'```')

    elif message.content.startswith('!coin'):
        j = random.randint(1,2)
        if j == 1:
            yield from client.send_message(message.channel, '```Heads!```')
        else:
            yield from client.send_message(message.channel, '```Tails!```')
            
    elif message.content.startswith('!1d'):
        k = int(message.content[3:])
        j = random.randint(1,k)
        yield from client.send_message(message.channel, '```Rolling a d'+str(k)+'\nRolled a ' + str(j) + '```')

    elif message.content.startswith('!swing'):
        j = random.randint(0,1)
        if j == 0:
            msg = 'They miss, burrying their sword into the ground'
        elif j == 1:
            msg = 'They hit. Cleaving the enemy in two'
        yield from client.send_message(message.channel,'```' +  message.author.name + ' swings their mighty sword\n' +msg+'```')

    elif message.content.startswith('!test'):
        yield from client.send_message(message.channel,message.mentions[0])

    elif message.content.startswith('!give'):
        msg = message.content.split(' ')
        amt = int(msg[1])
        if amt<0:
            yield from client.send_message(message.channel, 'You can\'t give away money you don\'t own')
            return
        user_to = message.mentions[0]
        user_from = message.author

        if user_from not in players:
            players[user_from] = dungeon.player(message.author.name)
        if user_to not in players:
            players[user_to] = dungeon.player(message.mentions[0].name)
        
        if players[user_from].gold < amt:
            yield from client.send_message(message.channel, '```You don\'t have enough money```')
        else:
            players[user_from].gold-=amt
            players[user_to].gold+=amt
            yield from client.send_message(message.channel, '```Gave '+str(amt)+' gold```')

    elif message.content.startswith('!inventory'):
        if message.author not in players:
            players[message.author] = dungeon.player(message.author.name)

        yield from client.send_message(message.channel, players[message.author].inventory())

    elif message.content.startswith('!encounter'):
        busy_users.append(message.author.name)
        if message.author not in players:
            players[message.author] = dungeon.player(message.author.name)
            
        m=dungeon.monster()
        player_dmg = 0
        enemy_dmg = 0
        
        yield from client.send_message(message.channel, m.pic+'\n```A '+m.name+' appears!```')

        while enemy_hp_l > 0 and player_hp > 0:
            yield from client.send_message(message.channel, '```The '+m.name+' has ' + str(m.hp) + ' hp \n'+message.author.name+' has ' + str(players[message.author].hp) + ' hp```')
            msg = yield from client.wait_for_message(author=message.author)
            if msg.content.lower() == 'attack' or msg.content.lower() == '!attack':
                player_dmg = random.randint(1,12)
                m.damage(player_dmg)
                if m.is_dead():
                    gold = random.randint(1, 8)
                    yield from client.send_message(message.channel, '```'+message.author.name+' defeats the '+m.name+' and finds '+ str(gold) + ' gold!```')
                    players[message.author].gold += gold
                    break
            elif msg.content.lower() == 'potion' or message.content.lower()== '!potion':
                if players[message.author].potions > 0:
                    players[message.author].use_potion()
                    yield from client.send_message(message.channel, '```'+message.author.name+' used a potion. Their hp went up by 5```')
                    continue
                elif players[message.author].potions == 0:
                    yield from client.send_message(message.channel, '```'+message.author.name+' fumbles around in their bag for a potion that isn\'t there')
            elif msg.content.lower() == 'run' or msg.content.lower()=='!run':
                yield from client.send_message(message.channel, '```Got away safely```')
                break
            else:
                yield from client.send_message(message.channel, '```Accepted input, attack, potion, run```')

            
            
            enemy_dmg = random.randint(1,12)
            players[message.author].damage(enemy_dmg)
            yield from client.send_message(message.channel, '```'+message.author.name+' swings, dealing ' + str(player_dmg) + ' damage.\nThe '+m.name+' swings, dealing '+ str(enemy_dmg) +' damage.```')  
        
            if players[message.author].is_dead():
                yield from client.send_message(message.channel, '```The '+m.name+' overpowers '+message.author.name+' and they black out```')
        busy_users.remove(message.author.name)

    elif message.content.startswith('!buy'):
        if message.author not in players:
            players[message.author] = player()
        msg = message.content.split(' ')
        if msg[1].lower() == 'potion':
            j=(int(msg[2])*5)
            if int(msg[2]) < 0:
                yield from client.send_message(message.channel, '```You can\'t buy negative potions```')
            if players[message.author].gold < j:
                yield from client.send_message(message.channel, '```You don\'t have enough gold for that```')
            else:
                players[message.author].gold -=j
                players[message.author].potions += int(msg[2])
                yield from client.send_message(message.channel, 'Bought '+msg[2]+' potions for '+str(j)+' gold')
        else:
            yield from client.send_message(message.channel, '```Invalid order\nTry !buy potion 1```')
    elif message.content.startswith ('!shop'):
        busy_users.append(message.author.name)
        if message.author not in players:
            players[message.author] = player()
        yield from client.send_message(message.channel, '```Welcome to the shop!```\nPotion - 5g')
        msg = yield from client.wait_for_message(author=message.author)
        if msg.content.lower() == 'potion' or msg.content.lower() == '!potion':
            if players[message.author].gold <5:
                yield from client.send_message(message.channel, '```You don\'t have enough gold to buy this item\nThank you for visiting the shop!```')
            else:
                players[message.author].potions+=1
                players[message.author].gold-=5
                yield from client.send_message(message.channel, '```'+message.author.name+' bought a potion.\nThank you for visiting the shop!```')
        busy_users.remove(message.author.name)

    elif message.content.startswith('!dungeon') and message.author.name == 's4x0r':
        player_hp = 20
        monsters=[]
        busy_users.append(message.author.name)
        d=dungeon.dungeon()
        x=0
        y=0

        c=(str(x)+str(y))
        di=directions[d.rooms[c].room_direction]
        le=str(d.rooms[c].length)
        wi=str(d.rooms[c].width)
        en=str(d.rooms[c].no_of_enemies)
        doo=directions[d.rooms[c].doors[0]]
        r=directions[d.rooms[c].doors[1]]
        yield from client.send_message(message.channel, look_msg.format(di,le,wi,en,doo,r))

        if d.rooms[c].no_of_enemies > 0:
            for i in range(d.rooms[c].no_of_enemies):
                monsters.append(dungeon.monster())
                
        
        while len(monsters) > 0:
            #print there are _ monsters here
            msg = ('There are '+str(len(monsters))+' monsters here')
            for i in range(len(monsters)):
                msg += ('\n'+monsters[i].name)
            msg += ('\n'+message.author.name+' has '+str(player_hp)+' hp')
            yield from client.send_message(message.channel, msg)
            
            #player turn
            msg_in = yield from client.wait_for_message(author=message.author)
            l=msg_in.content.split(' ')

            if l[0].lower()=='attack' or l[0].lower()=='!attack':
                j = random.randint(1, 12)
                monsters[int(l[1])].damage(j)
                if monsters[int(l[1])].hp<=0:
                    yield from client.send_message(message.channel, 'The '+monsters[int(l[1])].name+' dies')
                    monsters.pop(int(l[1]))
                else:
                    yield from client.send_message(message.channel, message.author.name+' deals '+str(j)+' damage to the '+monsters[int(l[1])].name)
            else:
                yield from client.send_message(message.channel, l[0])
                
            #monster turn
            for i in range(len(monsters)):
                j = random.randint(0,2)
                if j == 0:
                    yield from client.send_message(message.channel, 'The '+monsters[i].name+' shuffles about')
                elif j == 1:
                    yield from client.send_message(message.channel, 'The '+monsters[i].name+' swings, but misses')                               
                elif j == 2:
                    k = random.randint(1,12)
                    player_hp -= k
                    yield from client.send_message(message.channel, 'The '+monsters[i].name+' swing and deals '+str(k)+' damage')
                #if monster hp = 0, remove
            
  

        busy_users.remove(message.author.name)
client.run('token')


