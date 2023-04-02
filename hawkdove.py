import random
import tkinter
random.seed()

def plot(xvals, yvals):
    # This is a function for creating a simple scatter plot.  You will use it,
    # but you can ignore the internal workings.
    root = tkinter.Tk()
    c = tkinter.Canvas(root, width=700, height=400, bg='white') #was 350 x 280
    c.grid()
    #create x-axis
    c.create_line(50,350,650,350, width=3)
    for i in range(5):
        x = 50 + (i * 150)
        c.create_text(x,355,anchor='n', text='%s'% (.5*(i+2) ) )
    #y-axis
    c.create_line(50,350,50,50, width=3)
    for i in range(5):
        y = 350 - (i * 75)
        c.create_text(45,y, anchor='e', text='%s'% (.25*i))
    #plot the points
    for i in range(len(xvals)):
        x, y = xvals[i], yvals[i]
        xpixel = int(50 + 300*(x-1))
        ypixel = int(350 - 300*y)
        c.create_oval(xpixel-3,ypixel-3,xpixel+3,ypixel+3, width=1, fill='red')
    root.mainloop()

#Constants: setting these values controls the parameters of your experiment.
injurycost = 10 #Cost of losing a fight  
displaycost = 1 #Cost of displaying   
foodbenefit = 8 #Value of the food being fought over   
init_hawk = 0
init_dove = 0
init_defensive = 0
init_evolving = 150

########
# Your code here
########

class World:
    def __init__(self):
        self.birdlist = []
    def update(self):
        for i in self.birdlist:
            i.update()
    def free_food(self, number):
        n = 0
        while n <= number:
            i = random.choice(self.birdlist)
            i.eat()
            n+=1
    def conflict(self, encounter):
        n = 0
        while n <= encounter:
            i = random.choice(self.birdlist)
            j = random.choice(self.birdlist)
            i.encounter(j)
            n+=1
    def status(self):
        count1 = 0
        count2 = 0
        count3 = 0
        for i in self.birdlist:
            if i.species == "Hawk":
                count1 +=1
            elif i.species == "Dove":
                count2 +=1
            elif i.species == "Defensive":
                count3 +=1
        return [count1, count2, count3]
    def evolvingPlot(self):
        weight = []
        aggressiveness = []
        for i in self.birdlist:
            weight.append(i.weight)
            aggressiveness.append(i.aggressiveness)
        plot(weight, aggressiveness)

class Bird:
    def __init__(self, world):
        self.world = world
        self.health = 100
        self.world.birdlist.append(self)
    def eat(self):
        self.health += foodbenefit
    def injure(self):
        self.health -= injurycost
    def display(self):
        self.health -= displaycost
    def update(self):
        self.health -=1
        if self.health <= 0:
            self.die()
    def die(self):
        self.world.birdlist.remove(self)

class Dove(Bird):
    species = "Dove"
    def update(self):
        Bird.update(self)
        if self.health > 200:
            self.world.birdlist.append(Dove(self.world))
            self.health -=100
    def defend_choice(self):
        return False
    def encounter(self, another):
        if another.defend_choice() == True:
            another.eat()
        else:
            self.display()
            another.display()
            random.choice([self,another]).eat()
    
class Hawk(Bird):
    species = "Hawk"
    def update(self):
        Bird.update(self)
        if self.health > 200:
            self.world.birdlist.append(Hawk(self.world))
            self.health -=100
    def defend_choice(self):
        return True
    def encounter(self, another):
        if another.defend_choice() == False:
            self.eat()
        else:
            fighting = [self,another]
            winner = random.choice(fighting)
            winner.eat()
            fighting.remove(winner)
            fighting[0].injure()

class Defensive(Bird):
    species = "Defensive"
    def update(self):
        Bird.update(self)
        if self.health > 200:
            self.world.birdlist.append(Defensive(self.world))
            self.health -=100
    def defend_choice(self):
        return True
    def encounter(self, another):
        if another.defend_choice() == True:
            another.eat()
        else:
            self.display()
            another.display()
            random.choice([self,another]).eat()

class Evolving(Bird):
    def __init__(self, world, weight = None, aggressiveness = None):
        Bird.__init__(self,world)
        if weight == None:
            self.weight = random.uniform(1,3)
        else:
            self.weight = weight + random.uniform(-0.1, 0.1)
            if self.weight < 1:
                self.weight = 1
            elif self.weight > 3:
                self.weight = 3
        if aggressiveness == None:
            self.aggressiveness = random.random()
        else:
            self.aggressiveness = aggressiveness + random.uniform(-0.05, 0.05)
            if self.aggressiveness < 0:
                self.aggressiveness = 0
            elif self.aggressiveness > 1:
                self.aggressiveness = 1
    def defend_choice(self):
        if random.random() <= self.aggressiveness:
            return True
        else:
            return False
    def encounter(self,another):
        if self.defend_choice() == False and another.defend_choice() == False:
            self.display()
            another.display()
            random.choice([self,another]).eat()
        elif self.defend_choice() == True and another.defend_choice() == False:
            self.eat()
        elif self.defend_choice() == False and another.defend_choice() == True:
            another.eat()
        else:
            probabilitywin = self.weight/(self.weight + another.weight)
            if random.random() <= probabilitywin:
                self.eat()
                another.injure()
            else:
                self.injure()
                another.eat()
    def update(self):
        self.health -= 0.4 + 0.6*self.weight
        if self.health <= 0:
            self.die()        
        if self.health >= 200:
            self.health -= 100
            self.world.birdlist.append(Evolving(self.world,self.weight,self.aggressiveness))

########
# The code below actually runs the simulation.  You shouldn't have to do anything to it.
########

w = World()

for i in range(init_dove):
    Dove(w)
for i in range(init_hawk):
    Hawk(w)
for i in range(init_defensive):
    Defensive(w)
for i in range(init_evolving):
    Evolving(w)
for t in range(10000):
    w.free_food(10) 
    w.conflict(50)
    w.update()

# print(w.status())
w.evolvingPlot()  #This line adds a plot of evolving birds. Uncomment it when needed.


