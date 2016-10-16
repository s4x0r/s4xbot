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
        

        
