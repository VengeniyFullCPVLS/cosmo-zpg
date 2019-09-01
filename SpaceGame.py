import random
class Field:
    def __init__(self): 
        self.x=1000
        self.y=1000
    def getxy(self):
        return self.x,self.y

class Starship:
    def __init__(self,x,y,speed): 
        self.x=x
        self.y=y 
        self.speed=speed
    def print_speed(self):
        print("ship speed={}".format(self.speed))
    def distance_between_ship_and_task(self,mission):
        return ((self.x-mission.x)**2+(self.y-mission.y)**2)**(1/2) 
    def print_ship_position(self):
        print("ship_coordiates:x={} y={}".format(self.x,self.y))
    def make_step_to_destination(self,mission): 
        if(self.speed<self.distance_between_ship_and_task(mission)):
            self.x=self.x+(self.speed*(mission.x-self.x))/self.distance_between_ship_and_task(mission)
            self.y=self.y+(self.speed*(mission.y-self.y))/self.distance_between_ship_and_task(mission)
        else:
            self.x=mission.x
            self.y=mission.y
        self.print_ship_position()
    
class Mission:
    def __init__(self):
        self.x=random.randint(0,1000)
        self.y=random.randint(0,1000)

class Game:
    def __init__(self):
        self.starship=Starship(random.randint(0,1000),random.randint(0,1000),random.normalvariate(40,10))
        self.field=Field()
    def create_mission(self):
        self.mission=Mission()
    def pass_mission(self):
        self.starship.print_speed()
        print("\n")
        self.starship.print_ship_position()
        self.create_mission()
        while self.starship.x!=self.mission.x:
            self.starship.make_step_to_destination(self.mission)
game=Game()
game.pass_mission()
        

