#Link to join a server
#https://discordapp.com/oauth2/authorize?client_id=217887176308817920&scope=bot&permissions=0

import config
import text
import dungeon
import discord
import asyncio
import random
import tools
import wordgame
from time import gmtime, strftime

client = discord.Client()

directions = {0:'North', 1:'East', 2:'South', 3:'West'}
ball = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']


players = {}
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

    if message.author.name in config.mods:
        if message.content.startswith('!stop'):
            print ((strftime("%Y-%m-%d %H:%M:%S", gmtime()))+' Stopped by '+message.author.name)
            exit()
        elif message.content.startswith('!show busy'):
            if len(busy_users)==0:
                yield from client.send_message(message.author, 'None')
                return
            for i in busy_users:
                m+=busy_users[i].name
            yield from client.send_message(message.author, m)
        elif message.content.startswith('!clear busy'):
            busy_users.clear()
        elif message.content.startswith('!mint'):
            l=message.content.split(' ')
            if message.author not in players:
                players[message.author] = dungeon.player(message.author.name)
            players[message.author].gold += int(l[1])
            yield from client.send_message(message.author, 'Minted '+str(l[1])+' gold')
            print ((strftime("%Y-%m-%d %H:%M:%S", gmtime()))+' '+message.author.name+' Minted '+str(l[1])+' gold')

    if message.author == client.user:
        return
    elif message.author.name in busy_users:
        return

    elif message.content.startswith('!help'):
        yield from client.send_message(message.channel, text.help_msg)
        if message.author.name in config.mods:
            yield from client.send_message(message.author, text.mod_help)

    elif message.content.startswith('!changelog'):
        yield from client.send_message(message.channel, text.changelog)

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
        yield from client.send_message(message.channel, text.ball[j])

    elif message.content.startswith('!lib'):
        if " " not in message.content:
            d = wordgame.rand()
            parts = []
            yield from client.send_message(message.author, 'This lib has ' + str(len(d.parts))+' parts')
            for x in d.parts:
                yield from client.send_message(message.author, 'Enter a(n) '+x)
                msg = yield from client.wait_for_message(author=message.author)

                parts.append(msg.content)

            yield from client.send_message(message.channel, d.body.format(*parts))
            return
        else:
            j = message.content.split(' ')
            if j[1].lower() in 'random':
                m = wordgame.gen()
                yield from client.send_message(message.channel, m)
                
            #elif adlib search
            elif j[1].lower() in 'search':
                l=[]
                l = wordgame.search(j[2])
                yield from client.send_message(message.channel, "Search returned "+str(len(l))+" results \nPick: 1-"+str(len(l)))
                msg = yield from client.wait_for_message(author=message.author)
                if int(msg.content)-1 not in range(len(l)):
                    yield from client.send_message(message.channel, "Invalid choice")
                    return
                else:
                    d = l[int(msg.content)-1]
                    parts = []
                    yield from client.send_message(message.author, 'This lib has ' + str(len(d.parts))+' parts')

                    for x in d.parts:
                        yield from client.send_message(message.author, 'Enter a(n) '+x)
                        msg = yield from client.wait_for_message(author=message.author)

                        parts.append(msg.content)

                    yield from client.send_message(message.channel, d.body.format(*parts))
                    return
                
            else:
                return

            
    elif message.content.startswith('!rps'):
        rpsmsg = '{0} threw {1}\n{2} threw {3}'
        accept=['rock', 'paper', 'scissors']
        rpsdict = {'rock':0, 'r':0, 'paper':1, 'p':1, 'scissors':2, 's':2}
        user_from = message.author
        
        if ' ' not in message.content:
            user_to=client.user
            yield from client.send_message(user_from, 'Pick Rock, Paper, or Scissors')
            msg = yield from client.wait_for_message(author=user_from)
            while msg.content.lower() not in rpsdict.keys():
                client.send_message(message.author, 'Invalid choice\nPick Rock, Paper, or Scissors')
                msg = yield from client.wait_for_message(author=user_from)
            user_from_in = rpsdict[msg.content.lower()]
            i = random.choice(accept)
            user_to_in = rpsdict[i]

        else:
            user_to = message.mentions[0]
             
            #p1 input
            yield from client.send_message(user_from, 'Pick Rock, Paper, or Scissors')
            msg = yield from client.wait_for_message(author=user_from)
            while msg.content.lower() not in rpsdict.keys():
                yield from client.send_message(message.author, 'Invalid choice\nPick Rock, Paper, or Scissors')
                msg = yield from client.wait_for_message(author=user_from)
            user_from_in = rpsdict[msg.content.lower()]

            #p2 input
            yield from client.send_message(user_to, user_from.name+' has challenged you to RPS!\nPick Rock, Paper, or Scissors')
            msg = yield from client.wait_for_message(author=user_to)
            while msg.content.lower() not in rpsdict.keys():
                yield from client.send_message(user_to, 'Invalid choice\nPick Rock, Paper, or Scissors')
                msg = yield from client.wait_for_message(author=user_to)
            user_to_in = rpsdict[msg.content.lower()]

        #results 
        g= user_from_in - user_to_in
        m = rpsmsg.format(user_from.name, accept[user_from_in], user_to.name, accept[user_to_in])

        if g == 0:
            #draw
            m+='\nIt\'s a draw!'
        elif g == -2 or g == 1:
            #p1 win
            m+=('\n'+user_from.name+' wins!')
        elif g == -1 or g == 2:
            #p2 win
            m+=('\n'+user_to.name+' wins!')
        else:
            #error
            pass

        yield from client.send_message(message.channel, m)
        
        
    elif message.content.startswith('!insult'):
        yield from client.send_message(message.channel, wordgame.insult())
        
    elif message.content.startswith('!coin'):
        j = random.randint(1,2)
        if j == 1:
            yield from client.send_message(message.channel, '```Heads!```')
        else:
            yield from client.send_message(message.channel, '```Tails!```')
            
    elif message.content.startswith('!dice'):
        k = message.content.split(' ')
        j = k[1].split('d')
        l = int(j[0])
        m = int(j[1])
        yield from client.send_message(message.channel, tools.dice(l, m))

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

        while m.hp > 0 and players[message.author].hp > 0:
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
                yield from client.send_message(message.channel, '```The '+m.name+' overpowers '+message.author.name+' and they black out\nThey wake up some time later missing some health and gold```')
                players[message.author].respawn()
                busy_users.remove(message.author.name)
                break

        busy_users.remove(message.author.name)

    elif message.content.startswith('!buy'):
        if message.author not in players:
            players[message.author] = dungeon.player(message.author.name)
        msg = message.content.split(' ')
        if len(msg) > 1:
            if msg[1].lower() == 'list':
                yield from client.send_message(message.channel, text.buy_list)
            elif msg[1].lower() == 'potion':
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
            yield from client.send_message(message.channel, '```Invalid order\nTry !buy list```')

    elif message.content.startswith('!dungeon') and message.author.name == 's4x0r':
        player_hp = 20
        monsters=[]
        busy_users.append(message.author.name)
        d=dungeon.dungeon()
        x=0
        y=0

        c=(str(x)+str(y))
        yield from client.send_message(message.channel, d.rooms[c].look())

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
client.run(config.token)


