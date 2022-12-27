import random


class Character:
    def __init__(self, gp, np, name):   # gp - good point / np - negative point
        self.gp = gp
        self.np = np
        self.name = name


class Red_questions(Character):
    def __init__(self):
        Character.__init__(self, 75, 25, "red")

class Blue_questions(Character):
    def __init__(self):
        Character.__init__(self, 50, 50,"blue")

class Green_questions(Character):
    def __init__(self):
        Character.__init__(self, 25, 75,"green")               
    

class Player(Character):
    def __init__(self,name, gp, np):
        Character.__init__(self, gp, np, name)
        self.gp = gp
        self.np = np

class Field:
    def __init__(self, questions):
        self.questions = questions
    
    
    def print_state(self):
        print("It is 2055 and you have a decision to make ")
        for i in self.questions:
            print(i.name)
            
        
    @staticmethod
    def gen_random():
        rand = random.randint(0,2)
        if rand == 0:
            return Field([Green_questions()])
        if rand == 1:
            return Field([Red_questions()])
        if rand == 2:
            return Field([Blue_questions()])
        return Field()

class World:
    def __init__(self):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
                fields.append(Field.gen_random())
            self.state.append(fields)    
    
    def get_questions(self):
        return self.state[self.x][self.y].questions        
            
   
def go(self):
    questions = world.get_questions()
    
    


def print_state(self):  
    self.state[self.x][self.y].print_state()

def forward(self):
    if self.x == len(self.state):
        print("You have to refuse here. Or you can also hesitate")              
    else:
        self.x = self.x + 1
        
def backwards(self):
    if self.x == 0:
        print("You are not allowed to hesitate here") 
    else:
        self.x = self.x - 1

def right(self):
    if self.y == len(self.state[self.x]) - 1:
       print("You have to accept here. Or you can hesitate")
    else:
        self.y = self.y + 1
 
 
def left(self):
    if self.y == 0:
       print("You have to take a decision")
    else:
        self.y = self.y - 1                                        

def accept(player, world):
    world.forward()
    
def refuse(player,world):
    world.right() 
    
def decision_made(player,world):
    world.left()

def hesitate(player, world):
    world.backwards()          

def exit_game(player, world):
    print("You are about leave the game. The game will restart at your last saving spot.")
    exit(0)


def help_game(player, world):
    print(Commands.keys())
    
def save():
    pass

def load():
    pass   




Commands = {
    'help': help_game,
    'quit': exit_game,
    'accept': accept,
    'refuse': refuse,
    'hesitate': hesitate,
    'go': go,
    'NoDecision': decision_made,
    'feelings': feelings, # later: sad, angry, rejoice
    
    'save': save,
    'load': load,
}






if __name__ == '__main__':
    name = input("Welcome to the Decision game!\nPlease enter your username: ")
    player = Player(name, 100, 50)
    world = World(50,50)
    print("(type help to list the commands available)\n")
    while True:
        command = input("- ").lower().split(" ")# command should look like this: do (this)
        if command[0] in Commands:
                Commands[command[0]](player, world)
        else:
            print("Please enter a valid decision")
        world.print_state()    
            
                        
                
        
    