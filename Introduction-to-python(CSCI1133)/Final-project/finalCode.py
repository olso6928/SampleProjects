import turtle
turtle.hideturtle()
turtle.speed(0)
fontinfo = ('Arial', 10, 'normal') #font information for turtle.write()

counties = [] #list of county OBJECTS!
stateobs = [] #list of state OBJECTS!

def createAxis(max, half, fourth, thfourth): #create the axes for the graph, bringing in the calculated population values
    turtle.pencolor('black')
    y = 200
    x = -300
    turtle.penup()

    #draw x-axis (just the line)
    turtle.goto(-310, -300)
    turtle.pendown()
    turtle.goto(250, -300)
    turtle.penup()

    #draw y-axis (just the line)
    turtle.goto(-300, -310)
    turtle.pendown()
    turtle.goto(-300, 210)
    turtle.penup()

    #draw y-axis tick marks and write population numbers calculated from State objects
    for i in (max, thfourth, half, fourth):
        turtle.seth(180)
        turtle.goto(-295, y)
        turtle.pendown()
        turtle.fd(10)
        turtle.penup()
        turtle.fd(15)
        turtle.write(i, align = 'center', font = fontinfo)
        y -= 125 #distance between the tick marks

    #draw x-axis tick marks and write years
    for i in ('2010', '2011', '2012', '2013', '2014', '2015'):
        turtle.seth(270)
        turtle.goto(x, -295)
        turtle.pendown()
        turtle.fd(10)
        turtle.penup()
        turtle.fd(20)
        turtle.write(i, align = 'center', font = fontinfo)
        x += 110 #distance between the tick marks

def createClasses(fname): #function to read the file and create the corresponding classes from the data
    allstate = [] #list of all the lines with (just) state data
    file = open(fname, 'r')
    file.readline()
    for line in file:
        newline = line.split(',')
        if len(newline) == 0: #if nothing in the line, break because the file is done
            break
        elif "County" not in newline[0]: #when its a state
            x = newline[0] #set variable x as the state name to be associated with the counties in the state
            allstate.append(newline)
        elif "County" in newline[0]: #when its a county
            newline[0] = County(newline[0],newline[1:], x) #create a County object named the county name and include the data in the line as well as the state is belongs to
            counties.append(newline[0]) #add object to a new list

    #after all the objects have been created (file is done being read)
    for i in allstate:
        indi = allstate.index(i) #find the index of the desired state in the list of state data
        name = allstate[indi][0] #create variable with the name of the state
        name = State(name, allstate[indi][1:]) #create a State object with the corresponding data
        stateobs.append(name) #add object to a new list

class County():
    def __init__(self, countyname, countypops, statein):
        self.name = countyname
        self.pop = countypops
        self.pop = [int(i) for i in self.pop] #make all entries in the population list into integers from strings
        self.state = statein #state that this county is apart of
        self.calcm(self.pop) #calculate the m value
        self.calcb(self.pop) #calculate the b value

    def calcm(self,pop): #using the given equations, calculate the m value for the object and return it
        self.m = (-1/7) * pop[0] + (-3/35) * pop[1] + (-1/35) * pop[2] + (1/35) * pop[3] + (3/35) * pop[4] + (1/7) * pop[5]
        return self.m

    def calcb(self, pop): #using the given equations, calculate the b value for the object and return it
        self.b = (11/21) * pop[0] + (8/21) * pop[1] + (5/21) * pop[2] + (2/21) * pop[3] + (-1/21) * pop[4] + (-4/21) * pop[5]
        return self.b

    def CreateEq(self): #create a string with the equation and truncate at 4 decimal points
        m = '%.4f'%(self.m)
        b = '%.4f'%(self.b)
        return 'y = ' + m + 'x' + ' + ' + b

    def __lt__(self, other): #override the less than operator to compare the  m values of objects
        if self.m < other.m:
            return True
        else:
            return False

    def display(self, incr, pncolor): #general display function that will end up being used for all object types
        turtle.pencolor(pncolor)
        xposit = -190 #xcor where the SECOND data point will be
        turtle.penup()
        turtle.goto(-300, (self.pop[0] / incr) - 300) #first data point calculating what the y-value should be
        turtle.dot() #make a dot on the graph
        turtle.pendown()
        for i in (1,2,3,4,5): #do the same for all data values, moving the xcor to the corresponding position
            yposit = self.pop[i] / incr
            turtle.goto(xposit, yposit - 300)
            turtle.dot()
            xposit += 110
        turtle.write(self.CreateEq(), align = 'left', font = fontinfo) #write the final equation next to the line drawn

class State(County):
    def __init__(self, namein, statepops):
        self.name = namein
        self.pop = statepops
        self.pop = [int(i) for i in self.pop] #make all entries in the population list into integers from strings
        self.countyob = [] #list of all county OBJECTS in state
        self.cntynamelst = [] #list of all county NAMES in state
        County.calcm(self, self.pop) #calculate the m value using the inherited function
        County.calcb(self, self.pop) #calculate the b value using the inherited function
        self.countylst()

    def countylst(self): #match counties state with the state object and make list of all county OBJECTS in state
        for i in counties:
            if self.name == i.state:
                self.countyob.append(i)
        return self.countyob

    def greatestCnty(self): #find county with greatest growthrate
        self.maxcnty = max(self.countyob)
        return self.maxcnty

    def leastCnty(self): #find county with the lowest growthrate
        self.mincnty = min(self.countyob)
        return self.mincnty

    def getCountyLst(self): #makes a list of all county NAMES (no other info!)
        self.countylst()
        for i in self.countyob:
            self.cntynamelst.append(i.name)
        return self.cntynamelst

    def CalcAxis(self): #calculate the values for the y-axis
        self.ymax = max(self.pop)
        self.half = self.ymax / 2
        self.fourth = self.half / 2
        self.threefourth = self.half + self.fourth
        return (self.ymax, self.half, self.fourth, self.threefourth)

    def display(self, cnty = None): #first half of the display function (other is in County class) mainly used to initialize
        self.CalcAxis() #call the function to calculate the axis numbers
        createAxis(self.ymax, int(self.half), int(self.fourth), int(self.threefourth)) #create the axis using the global function and the calculated variables
        increment = self.ymax / 500 #create the increment - each pixel will correspond to one set of the increment (aka how much population each pixel corresponds to) use 500 because the total y-axis is 500 long
        County.display(self, increment, 'blue') #call the county display function with blue as the color
        turtle.penup()
        turtle.goto(250,250)
        turtle.write(self.name, align = 'left', font = fontinfo) #move and write the state name
        if cnty != None: #if there was a county listed in the State.display(), call the County display and use red as the color
            County.display(cnty, increment, 'red')
            turtle.penup()
            turtle.goto(250,230)
            turtle.write(cnty.name, align = 'left', font = fontinfo) #move and write the county name

class Analysis(State):
    def __init__(self, stateobs):
        self.statelst = stateobs #list of state OBJECTS!

    def greatestState(self): #find the maximum state and return it
        maxim = max(self.statelst)
        return maxim.name

    def leastState(self): #find the minimum state and return it
        minim = min(self.statelst)
        return minim.name

    def findState(self, state): #find the state object with that name and return the index of that object in the list of objects for later use
        for i in self.statelst:
            if i.name == state:
                self.stind = self.statelst.index(i)
                return self.stind

    def displayState(self, name): #basic display state - find the correct state object index and call the State display function to draw it
        self.findState(name)
        State.display(self.statelst[self.stind])

    def displayStateGreatestCounty(self, name):
        self.findState(name)
        grcnty = State.greatestCnty(self.statelst[self.stind]) #call the function to determine the greatest state using the desired state object
        State.display(self.statelst[self.stind], grcnty) #call the State display with the state object and the county object to both be drawn

    def displayStateLeastCounty(self, name):
        self.findState(name)
        lscnty = State.leastCnty(self.statelst[self.stind]) #call the function to determine the least state using the desired state object
        State.display(self.statelst[self.stind], lscnty) #call the State display with the state object and the county object to both be drawn

    def clear(self): #clear the turtle window
        turtle.clear()

createClasses('censusdata.csv') #call the functions to create the classes with the corresponding file
analysis = Analysis(stateobs) #create Analysis object named analysis, passing in the list of state objects
