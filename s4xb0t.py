#Link to join a server
#https://discordapp.com/oauth2/authorize?client_id=217887176308817920&scope=bot&permissions=0


import discord
import asyncio
import random

client = discord.Client()


insult1 = ["a Lazy", "a Stupid", "an Insecure", "an Idiotic", "a Slimy", "a Slutty", "a Smelly", "a Pompous", "a Communist", "a Dicknose", "a Pie-eating", "a Racist", "an Elitist", "a White Trash", "a Drug-Loving", "a Butterface", "a Tone Deaf", "an Ugly", "a Creepy"]
insult2 = ["Douche", "Ass", "Turd", "Rectum", "Butt", "Cock", "Shit", "Crotch", "Bitch", "Prick", "Slut", "Taint", "Fuck", "Dick", "Boner", "Shart", "Nut", "Sphincter" ]
insult3 = ["Pilot", "Canoe", "Captain", "Pirate", "Hammer", "Knob", "Box", "Jockey", "Nazi", "Waffle", "Goblin", "Blossum", "Biscuit", "Clown", "Socket", "Monster", "Hound", "Dragon", "Balloon"]
ball = ['It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Don\'t count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful']
help_msg = ('''\
!help - Displays this message
!insult - Generates a random insult
!coin - Flips a coin
!encounter - Fight a random monster
!wtf
!fresh
!changelog
!inventory - See what you've got
!8ball - Ask it a question
!give - Give a mentioned user gold
ex !give @s4x0r 5
!whisper - psst

-Dice-
!1d#
ex: 1d2, 1d6, 1d20
''')

changelog = ('''
v0.1.3a
-changed !gold to !inventory
-Added !shop
-Added !whisper
-Added potions
-Added !8ball
-Added !give
-Fixed dice
-Added bugs
''')

user_gold = {}
user_potions={}


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

    if message.author == client.user:
        return
    elif message.content.startswith('!stop') and message.author.name == 's4x0r':
        exit()

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
        amt = int((len(msg)-1))
        user_to = message.mentions[0]
        user_from = message.author

        if user_from not in user_gold:
            user_gold[user_from] = 0
        if user_to not in user_gold:
            user_gold[user_to] = 0
        
        if user_gold[user_from] < amt:
            yield from client.send_message(message.channel, '```You don\'t have enough money```')
        else:
            user_gold[user_from]-=amt
            user_gold[user_to]+=amt
            yield from client.send_message(message.channel, '```Gave '+str(amt)+' gold```')

    elif message.content.startswith('!inventory'):
        if message.author not in user_gold:
           user_gold[message.author] = 0
        if message.author not in user_potions:
            user_potions[message.author] = 0

        yield from client.send_message(message.channel, '```'+message.author.name+' has '+str(user_gold[message.author])+' gold and '+str(user_potions[message.author])+' potions```')

    elif message.content.startswith('!encounter'):
        k = random.randint(0,3)
        enemy = ['zombie', 'skeleton', 'enderman', 'endermite']
        enemy_pic = ['http://vignette1.wikia.nocookie.net/monster/images/b/b6/Minecraft-zombie-4.png','http://vignette2.wikia.nocookie.net/minecraft/images/2/23/Skeleton.png','http://vignette4.wikia.nocookie.net/minecraftstorymode/images/2/28/Enderman.png','http://vignette3.wikia.nocookie.net/minecraft/images/c/cf/Endermite.png']
        enemy_hp = [15,15, 20, 5]
        enemy_hp_l = int(enemy_hp[k])
        player_hp = 20
        player_dmg = 0
        enemy_dmg = 0
        yield from client.send_message(message.channel, enemy_pic[k]+'\n```A '+enemy[k]+' appears!```')

        while enemy_hp_l > 0 and player_hp > 0:
            yield from client.send_message(message.channel, '```The '+enemy[k]+' has ' + str(enemy_hp_l) + ' hp \n'+message.author.name+' has ' + str(player_hp) + ' hp```')
            msg = yield from client.wait_for_message(author=message.author)
            if msg.content == 'attack' or msg.content == '!sttack':
                player_dmg = random.randint(1,12)
                enemy_hp_l = (enemy_hp_l - player_dmg)
                if enemy_hp_l < 0:
                    enemy_hp_l = 0
            elif msg.content == 'potion':
                if message.author not in user_potions:
                    user_potions[message.author] = 0
                if user_potions[message.author] > 0:
                    user_potions[message.author] -=1
                    player_hp +=10
                    yield from client.send_message(message.channel, '``` '+message.author.name+' used a potion. Their hp went up by 5```')
                    continue
                elif user_potions[message.author] == 0:
                    yield from client.send_message(message.channel, '```'+message.author.name+' fumbles around in their bag for a potion that isn\'t there')
            elif msg.content == 'run':
                yield from client.send_message(message.channel, '```Got away safely```')
                break
            else:
                yield from client.send_message(message.channel, '```Accepted input, attack, potion, run```')

            if enemy_hp_l <= 0:
                gold = random.randint(1, 8)
                yield from client.send_message(message.channel, '```'+message.author.name+' defeats the '+enemy[k]+' and finds ' + str(gold) + ' gold!```')
                if message.author not in user_gold:
                    user_gold[message.author] = gold
                else:
                    user_gold[message.author] += gold
                break
            
            enemy_dmg = random.randint(1,12)
            player_hp = (player_hp - enemy_dmg)
            yield from client.send_message(message.channel, '```'+message.author.name+' swings, dealing ' + str(player_dmg) + ' damage.\nThe '+enemy[k]+' swings, dealing '+ str(enemy_dmg) +' damage.```')  
        
            if player_hp <= 0:
                yield from client.send_message(message.channel, '```The '+enemy[k]+' overpowers '+message.author.name+' and they black out```')

    elif message.content.startswith ('!shop'):
        if message.author not in user_gold:
            user_gold[message.author] = 0
        if message.author not in user_potions:
            user_potion[message.author] = 0
        yield from client.send_message(message.channel, '```Welcome to the shop!```\nPotion - 5g')
        msg = yield from client.wait_for_message(author=message.author)
        if msg.content == 'potion' or msg.content == 'Potion':
            if user_gold[message.author]<5:
                yield from client.send_message(message.channel, 'You don\'t have enough gold to buy this item')
            user_potions[message.author]+=1
            user_gold[message.author]-=5
            yield from client.send_message(message.channel, '```'+message.author.name+' bought a potion.\nThank you for visiting the shop!```')

client.run('token')


