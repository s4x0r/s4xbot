import random
import asyncio

player_x=0
player_y=0



@asyncio.coroutine
def create_dungeon():
    dungeon = {}
    x=0
    y=0
    x_max=3
    y_max=3
    entrance = 2
        
    while x<x_max and y<y_max:
        c=(str(x)+str(y))
        print('creating room '+c)
        dungeon[c]=room()
        if x == x_max:
            dungeon[c].doors.append(entrance)
            dungeon[c].doors.append(1)
            y+=1
            entrance = 3

        elif y == y_max:
            dungeon[c].doors.append(entrance)
            dungeon[c].doors.append(0)
            x+=1
            entrance = 2

        else:
            j=random.randint(0,1)
            if j==0:
                dungeon[c].doors.append(entrance)
                dungeon[c].doors.append(0)
                x+=1
                entrance=2
            else:
                dungeon[c].doors.append(entrance)
                dungeon[c].doors.append(1)
                y+=1
                entrance = 3
        return dungeon
    
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
        self.room_direction = random.randint(0,3)
        self.no_of_enemies = random.randint(0,2)
        self.doors=[]
        #self.doors = create_doors()
        print('Done')

    def look(self):
        print('You stand in a room')
        print('Extending to the '+str(self.room_direction)+', it is '+str(self.length)+' feet long, and '+str(self.width)+' feet wide.')
        print('There are '+str(self.no_of_enemies)+' enemies here')
        print('Doors:')
        for i in doors:
            print(str(doors[i]))

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
        self.items = []

    inv_msg = ('''

        {}
Level:{}        XP:{}
Max HP:{}       HP:{}
Gold:{}    Potions:{}
''')

    def inventory(self):
        return self.inv_msg.format(self.name, self.level, self.xp, self.max_hp, self.hp, self.gold, self.potions)

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
        


class item():
    pass
        
        

        
