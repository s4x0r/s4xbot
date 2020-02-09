import text
import random
import asyncio
import items

player_x=0
player_y=0



@asyncio.coroutine
class dungeon:
    def __init__(self):
        self.rooms = {}
        self.x = 0
        self.y = 0
        self.x_max=3
        self.y_max=3
        self.entrance = 2 
        while self.x<self.x_max and self.y<self.y_max:
            c=(str(self.x)+str(self.y))
            print('creating room '+str(c))
            self.rooms[c]=room()
            if self.x == self.x_max:
                self.rooms[c].doors.append(self.entrance)
                self.rooms[c].doors.append(1)
                self.y+=1
                self.entrance = 3
            elif self.y == self.y_max:
                self.rooms[c].doors.append(self.entrance)
                self.rooms[c].doors.append(0)
                self.x+=1
                self.entrance = 2

            else:
                j=random.randint(0,1)
                if j==0:
                    self.rooms[c].doors.append(self.entrance)
                    self.rooms[c].doors.append(0)
                    self.x+=1
                    self.entrance=2
                else:
                    self.rooms[c].doors.append(self.entrance)
                    self.rooms[c].doors.append(1)
                    self.y+=1
                    self.entrance = 3
                    

class room:
    def __init__(self):
        self.length = random.randint(6, 20)
        self.width = random.randint(6, 20)
        self.direction = random.randint(0,3)
        self.no_of_enemies = random.randint(0,2)
        self.doors=[]
        #self.doors = create_doors()
        #print('Done')

    def look(self):
        direct = text.directions[self.direction]
        door_1 = text.directions[self.doors[0]]
        door_2 = text.directions[self.doors[1]]
        return text.look_msg.format(direct,
                                        str(self.length),
                                        str(self.width),
                                        str(self.no_of_enemies),
                                        door_1,
                                        door_2)

class monster:
    monster_list=['zombie', 'skeleton', 'enderman', 'endermite', 'silverfish', 'husk', 'tiny magma cube', 'skeleton rider', 'stray', 'baby zombie', 'chicken jockey']
    pic_list=['http://vignette1.wikia.nocookie.net/monster/images/b/b6/Minecraft-zombie-4.png','http://vignette2.wikia.nocookie.net/minecraft/images/2/23/Skeleton.png','http://vignette4.wikia.nocookie.net/minecraftstorymode/images/2/28/Enderman.png','http://vignette3.wikia.nocookie.net/minecraft/images/c/cf/Endermite.png', 'https://hydra-media.cursecdn.com/minecraft.gamepedia.com/b/b9/Silverfish.png', 'https://hydra-media.cursecdn.com/minecraft.gamepedia.com/1/17/HuskCropped.png', 'https://hydra-media.cursecdn.com/minecraft.gamepedia.com/e/ed/Magma_Cube.png', 'http://i.imgur.com/qXHd5De.png', 'https://hydra-media.cursecdn.com/minecraft.gamepedia.com/0/07/Stray.png', 'https://hydra-media.cursecdn.com/minecraft.gamepedia.com/e/e2/Baby_Zombie.PNG', 'https://hydra-media.cursecdn.com/minecraft.gamepedia.com/d/d3/Chicken_Jockey.png']
    hp_list=[15,15, 20, 5, 5, 15, 1, 25, 15, 15, 18]
    def __init__(self):
        k = random.randint(0,10)
        self.name=self.monster_list[k]
        self.pic=self.pic_list[k]
        self.hp=self.hp_list[k]

    def damage(self, i):
        self.hp-=i
    def heal(self, i):
        self.hp+=i
    def is_dead(self):
        if self.hp < 1:
            return True
        else:
            return False
        
class player:
    def __init__(self, name):
        self.name = name
        self.max_hp = 20
        self.hp = 20
        self.xp = 0
        self.level = 1
        self.gold = 0
        self.potions = 0
        self.items = [items.weapons['Fist']]
        self.equip = items.weapons['Fist']
        

    inv_msg = ('''

        {}
Level:{}        XP:{}
+HP:{}/{}
Gold:{}    Potions:{}
''')

    def inventory(self):
        m = self.inv_msg.format(self.name, self.level, self.xp, self.hp, self.max_hp, self.gold, self.potions)
        n = '\n-Items:'
        for i in range(len(self.items)):
            n += ('\n'+self.items[i].name)
        return ('```diff'+m+n+'```')

    def use_potion(self):
        self.potions-=1
        self.hp+=5

    def damage(self, j):
        self.hp-=j

    def is_dead(self):
        if self.hp < 1:
            return True
        else:
            return False
        
    def respawn(self):
        self.hp = self.max_hp - int(self.max_hp/4)
        self.gold -=int(random.randint(0, self.gold/4))
        
        

        
