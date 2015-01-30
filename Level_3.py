from Tkinter import *
import random
import time

main = Tk(className = "Level 2")
canvas = Canvas(main, width = 1280, height = 720, bg = "Black")
canvas.pack()

global randomColourChangerYellow
randomColourChangerYellow=0
global colourChanger
colourChanger=0
global ScoreW
ScoreW = 0
global ScoreY
ScoreY = 0
global TreasureRemaining
TreasureRemaining = 4
global WCollected
WCollected = 0
global YCollected
YCollected = 0
global robowait
robowait=False
global pausevx ,pausevy
pausevx=0
pausevy=0
global RoboFinished
RoboFinished = False

def breadthFirstSearch(route, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in route[vertex] - set(path):
            if next == end:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def shortestPath(route, start, end):
    try:
        return next(breadthFirstSearch(route, start, end))
    except StopIteration:
        return None

class road:
    def __init__(self,name,x,y,width,height,colour="darkgrey"):
        self.name=name
        self.x1=x
        self.y1=y
        self.x2=x+width
        self.y2=y+height
        self.width=width
        self.height=height
        self.object=canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill=colour, width=0)

class robot:
    def __init__(self,x,y,speed=1.0,size=20,colour='blue'):
        self.x1=x
        self.y1=y
        self.x2=x+size
        self.y2=y+size
        self.colour=colour
        self.speed=speed
        self.size=size
        self.vx=speed
        self.vy=speed
        self.city = {Road1:set([Road2, Road9, Road7, Road4, Road3, Road15]),
                    Road2:set([Road1,Road10,Road5,Road13,Road14,Road16, Road19]),
                    Road3:set([Road1,Road5,Road13,Road14]),
                    Road4:set([Road1,Road5]),
                    Road5:set([Road3, Road4]),
                    Road6:set([Road2,Road11,Road15,Road7]),
                    Road7:set([Road6,Road12,Road1]),
                    Road9:set([Road1,Road10]),
                    Road10:set([Road9,Road2]),
                    Road11:set([Road6,Road13, Road14]),
                    Road12:set([Road7, Road15]),
                    Road13:set([Road2,Road11,Road15,Road3]),
                    Road14:set([Road2,Road17,Road15, Road3,Road11]),
                    Road15:set([Road6,Road13,Road14]),
                    Road16:set([Road2,Road20,Road17,Road21,Road22]),
                    Road17:set([Road14,Road16]),
                    Road19:set([Road19,Road20,Road21,Road22]),
                    Road20:set([Road16,Road19]),
                    Road21:set([Road16,Road19]),
                    Road22:set([Road16,Road19])}
        self.Route=[]
    def drawRobot(self):
        self.canvas=canvas
        self.shape=canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill=self.colour)
    #Give the robot a random position (Use this before drawing the robot)
    def randomPosition(self):
        RandRoad=random.choice(Roads) #Select a random road
        #If road is vertical set robot to be horizontally centered in this road and in a random vertical position
        if RandRoad.width<RandRoad.height:
            self.x1=RandRoad.x1+((RandRoad.width-self.size)/2)
            self.x2=self.x1+self.size
            self.y1=random.randrange((RandRoad.y1+(self.size/2)),(RandRoad.y2-(self.size*1.5)))
            self.y2=self.y1+self.size
        #If road is horizonal set robot to be vertically centered and in a random horizontal position.
        elif RandRoad.height<RandRoad.width:
            self.y1=RandRoad.y1+((RandRoad.height-self.size)/2)
            self.y2=self.y1+self.size
            self.x1=random.randrange((RandRoad.x1+(self.size/2)),(RandRoad.x2-self.size))
            self.x2=self.x1+self.size

    def checkPosition(self):
        for road in Roads:
            if self.x1>=road.x1 and self.x2<=road.x2 and self.y1>=road.y1 and self.y2<=road.y2:
                return road

    def treasureChecker(self):
        ShortestRouteLength=100
        for landmark in ListOfLandmarks:
            if landmark.treasure==True:
                self.Route=shortestPath(self.city,self.checkPosition(),landmark.Road)
                if len(self.Route)<ShortestRouteLength:
                    TreasureA=landmark.Road
                    self.ClosestLandmark=landmark
                    ShortestRouteLength=len(self.Route)
        return TreasureA
    
    def pathfinder(self):
        self.DistancetoLandmark=2000
        self.FindRoute=True
        for landmark in ListOfLandmarks:
            if landmark.treasure==True:
                if self.checkPosition()==landmark.Road:
                    if landmark.x>self.x1:
                        if (landmark.x-self.x1)<self.DistancetoLandmark:
                            self.DistancetoLandmark=landmark.x-self.x1
                            self.ClosestLandmark=landmark
                    elif landmark.x<self.x1:
                        if (self.x1-landmark.x)<self.DistancetoLandmark:
                            self.DistancetoLandmark=self.x1-landmark.x
                            self.ClosestLandmark=landmark
                    self.Route=[]
                    self.FindRoute=False                    
                    self.IteminRoute=1
        if self.FindRoute==True:
            self.Route=shortestPath(self.city, self.checkPosition(), self.treasureChecker())
            self.IteminRoute=1
            
    def move(self):
        global ScoreY
        global YCollected
        global ScoreW
        global WCollected
        global RoboFinished
        global TreasureRemaining
        for i in ListOfTreasures:
            for robot in RobotList:
                #This statement checks if the treasures coordinates are greater than or less that specifc coordinates
                #of one of the robot, if everything is correct
                if (i.x >= c3po.x1 and (i.x+i.width)<=c3po.x2) and (i.y >= c3po.y1 and (i.y+i.length)<=c3po.y2) and i.Found == False:
                    #it then runs this function which is defined later on in the program
                    treasure.clearTreasure1(i,"DarkGrey")
                    #This code updates the variable "TreasureRemaining" so the label for the amount of treasures 
                    #remaining is updated by - 1
                    TreasureRemaining = TreasureRemaining - 1
                    interface.treasureShow_label.config(text = str(TreasureRemaining))
                    #This code updates the variable "YCollected" by + 1 so the label for the amount of treasure that 
                    #robot has collected is updated
                    YCollected = YCollected + 1
                    interface.YCollected_label.config(text = str(YCollected))
                    #This section works the same as the previous statement but with the second robot and all its related 
                    #labels and variables
                if (i.x >= r2d2.x1 and (i.x+i.width)<=r2d2.x2) and (i.y >= r2d2.y1 and (i.y+i.length)<=r2d2.y2) and i.Found == False:
                    treasure.clearTreasure2(i,"DarkGrey")
                    TreasureRemaining = TreasureRemaining - 1
                    interface.treasureShow_label.config(text = str(TreasureRemaining))
                    WCollected = WCollected + 1
                    interface.WCollected_label.config(text = str(WCollected))
                    
                    if ScoreW > 350 or ScoreY > 350:
                        RoboFinished = True
                    else:
                        RoboFinished = False         
        if len(self.Route)-1<self.IteminRoute:
            stopTheBot()
            if self.ClosestLandmark.x>(self.x1+(self.size/2)):
                self.vx=self.speed
                self.vy=0
            elif self.ClosestLandmark.x<(self.x1+(self.size/2)):
                self.vx=-self.speed
                self.vy=0
            else:
                self.ClosestLandmark.treasure=False
                time.sleep(1)
                
                self.ClosestLandmark.treasure=False
                for landmark in ListOfLandmarks:
                    if landmark.treasure==True:
                        self.pathfinder()
                        break
                    else:
                        self.vx=0
                        self.vy=0
        else:
            self.NextRoad=self.Route[self.IteminRoute]
            if self.NextRoad.height>self.NextRoad.width:
                x_destination=self.NextRoad.x1+self.NextRoad.width/2
                if x_destination>(self.x1+(self.size/2)):
                    stopTheBot()
                    self.vx=self.speed
                    self.vy=0
                elif x_destination<(self.x1+(self.size/2)):
                    stopTheBot()
                    self.vx=-self.speed
                    self.vy=0
                else:
                    stopTheBot()
                    self.IteminRoute+=1
            elif self.NextRoad.height<self.NextRoad.width:
                stopTheBot()
                y_destination=self.NextRoad.y1+(self.NextRoad.height/2)
                if y_destination==(self.y1+(self.size/2)):
                    stopTheBot()
                    self.IteminRoute+=1
                elif y_destination>(self.y1+(self.size/2)):
                    stopTheBot()
                    self.vy=self.speed
                    self.vx=0
                elif y_destination<(self.y1+(self.size/2)):
                    stopTheBot()
                    self.vy=-self.speed
                    self.vx=0
        self.x1+=self.vx
        self.x2+=self.vx
        self.y1+=self.vy
        self.y2+=self.vy
        self.canvas.coords(self.shape,self.x1,self.y1,self.x2,self.y2)
        self.canvas.update()

class Object: #class that defines the objects that populate the map

    def __init__(self,x,y,length,width,colour,canvas):#This is the constructor which generates the objects on the map
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.colour = colour
        self.canvas=canvas
        self.object = canvas.create_rectangle(self.x,self.y,self.x+self.length,self.y+self.width,fill = self.colour)
        
class landmark(Object): #class that defines the Landmarks that may contain treasures - inherits from objects
    def __init__(self,x,y,length,width,colour,canvas,Id,treasure,Road): #This is the constructor which generates the 
                                                                        #landmarks the robot should visit, if a treasure
                                                                        #is present
        Object.__init__(self,x,y,length,width,colour,canvas)
        self.Id=Id
        self.treasure=treasure
        self.Road=Road

class treasure(Object): #class that defines the Treasures that are hidden in selected landmarks - inherits from objects
    
    def __init__(self,x,y,length,width,colour,canvas,Found,points):#This is the constructor which generates the treasures
                                                                    #the robot should collect
        Object.__init__(self,x,y,length,width,colour,canvas)
        
        self.Found = Found
        self.points = points

    def clearTreasure1(self, colour="DarkGrey"):
        # this function is for robot 1, it is run if the robot collects a treasure.
        global ScoreY
        #it then creates the illustion the treasure has been removed from the map
        canvas.itemconfig(self.object, fill=colour,width=0)
        #and updates the variable "ScoreY" by the amount of points that have been given when creating a specific treasure
        ScoreY = self.points + ScoreY
        self.points = 0
        #It then updates the score label
        interface.robot1Score_label.config(text = str(ScoreY))
        #and sets the treasure to "Found"
        self.Found = True
        canvas.update()
        
    def clearTreasure2(self, colour="DarkGrey"):
        #This function works the same as the previous one, only its for robot 2 and all its related labels and variables
        global ScoreW
        canvas.itemconfig(self.object, fill=colour,width=0)
        ScoreW = self.points + ScoreW
        self.points = 0 
        interface.robot2Score_label.config(text = str(ScoreW))
        self.Found = True

        canvas.update()

class interface:

    def __init__(self, name):
        self.start_button = Button(name, text="Start", width = 20, command=self.start, bg = "Green")
        self.start_button.place(x = 1110, y = 150)

        self.level1_button = Button(name, text="Level 1", width = 20, command=self.level1, bg = "Yellow")
        self.level1_button.place(x = 1110, y = 200)

        self.level2_button = Button(name, text="Level 2", width = 20, command=self.level2, bg = "Yellow")
        self.level2_button.place(x = 1110, y = 250)

        self.timerShow_label = Label(name, text = "", width = 7, font = ("Arial", 16))
        self.timerShow_label.place(x = 1170, y = 30)

        self.timer_label= Label(name,text ="Timer", width = 5, font = ("Arial", 16))
        self.timer_label.place(x = 1110, y = 30)

        self.treasures_label = Label(name, text = "Treasure Remaining: ", width = 16, height = 2, font = ("Arial", 12), anchor = N)
        self.treasures_label.place(x = 1110, y = 70)

        self.treasureShow_label = Label(name, text = TreasureRemaining, width = 16, font = ("Arial", 12))
        self.treasureShow_label.place(x = 1110, y = 100)

        self.robot1Score_label = Label(name, text = "Yellow Robot Score: ", width = 16, height = 1, font = ("Arial", 12), anchor = N)
        self.robot1Score_label.place(x = 1110, y = 300)

        self.robot1Score_label = Label(name, text = ScoreY, width = 16, font = ("Arial", 12))
        self.robot1Score_label.place(x = 1110, y = 320)

        self.robot2Score_label = Label(name, text = "White Robot Score: ", width = 16, height = 1, font = ("Arial", 12), anchor = N)
        self.robot2Score_label.place(x = 1110, y = 360)

        self.robot2Score_label = Label(name, text = ScoreW, width = 16, font = ("Arial", 12))
        self.robot2Score_label.place(x = 1110, y = 380)
        
        self.YCollected_label = Label(name, text = "Yellow Collected: ", width = 16, height = 1, font = ("Arial", 12), anchor = N)
        self.YCollected_label.place(x = 1110, y = 420)

        self.YCollected_label = Label(name, text = YCollected, width = 16, font = ("Arial", 12))
        self.YCollected_label.place(x = 1110, y = 440)

        self.WCollected_label = Label(name, text = "White Collected: ", width = 16, height = 1, font = ("Arial", 12), anchor = N)
        self.WCollected_label.place(x = 1110, y = 480)

        self.WCollected_label = Label(name, text = WCollected, width = 16, font = ("Arial", 12))
        self.WCollected_label.place(x = 1110, y = 500)

    def start(self):
        global RoboFinished
        interface.start_button.place_forget()
        interface.counterLabel(interface)
        while TreasureRemaining>0:
            for robot in RobotList:
                robot.move()
                time.sleep(0.0025)

    def level1(self):
        main.destroy()
        import Level_1

    def level2(self):
        main.destroy()
        import Level_2

    def count(main):
        global counter, colourChanger
        counter==counter
        global RoboFinished
        if (RoboFinished != True):
            counter=counter+1
            if colourChanger!=3:
                colourChanger=colourChanger+1
            else:
                colourChanger=0
            main.timerShow_label.config(text = str(counter))
            flipColour()
            main.timerShow_label.after(1000, main.count) 
        else:
            main.counterStop()

    def counterStop(main,self):
        return True

    def counterLabel(main,self):
            global counter, RoboFinished
            counter=0
            RoboFinished=False
            if counter!=1000000:
                interface.count()

class light(interface):
    def __init__(self,x0,y0,x1,y1,colour):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.colour = colour
        self.object = canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill = self.colour)
        
    def change_colour(self, colour):
        canvas.itemconfig(self.object, fill=colour)
        canvas.update()

interface = interface(main)

#Top Row
#This section of code utilises the constructor in the object class to generate objects the robot should avoid
pave1 = Object(10.0,10.0,1070.0,35.0, "Light Grey",canvas)
#everything encased in the brackets relates to a variable pre-defined in the Object class
object1 = Object(10.0,15.0,200.0, 25.0, "Red",canvas)
object2 = Object(290.0,15.0,200.0,25.0, "Red",canvas)
object3 = Object(580.0,15.0,200.0,25.0, "Red",canvas)
object4 = Object(870.0,15.0,210.0,25.0, "red",canvas)

#second row
pave2 = Object(50.0,85.0,354.0,35.0, "Light Grey",canvas)
object5 = Object(55.0,90.0,344.0,25.0,"Red",canvas)
pave3 = Object(444.0,85.0,35.0,110.0,"Light Grey",canvas)
object6 = Object(449.0,90.0,25.0,100.0, "Red",canvas)
pave4 = Object(519.0,85.0,351.0,35.0,"Light Grey",canvas)
object7 = Object(524.0,90.0,341.0,25.0,"Red",canvas)
pave5 = Object(910.0,85.0,35.0,150.0,"Light Grey",canvas)
object8 = Object(915.0,90.0,25.0,140.0,"Red",canvas)
pave6 = Object(985.0,85.0,35.0,110.0,"Light Grey",canvas)
object9 = Object(990.0,90.0,25.0,100.0, "Red",canvas)

#Third Row
pave7 = Object(50.0,160.0,394.25,35.0,"Light Grey",canvas)
object10 = Object(55.0,165.0,384.0,25.0,"Red",canvas)
pave9 = Object(519.0,160.0,351.0,35.0,"Light Grey",canvas)
object12 = Object(524.0,165.0,341.0,25.0,"Red",canvas)

#Fourth Row
pave10 = Object(50.0,235.0,180.25,105.0,"Light Grey", canvas)
object13 = Object(55.0,240.0,170.25,95.0, "Red", canvas)
pave12 = Object(270.25,235.0,765.75,105.0, "Light Grey", canvas)
object15 = Object(275.0,240.0,755.75,95.0, "Red", canvas)

#Fifth Row
pave21 = Object(50.0,380.0,180.25,105.0, "Light Grey",canvas)
object27 = Object(55.0,385.0,170.25,95.0, "Red",canvas)
pave22 = Object(270.25, 380.0, 180.25,105.0, "Light Grey",canvas)
object28 = Object(275.0, 385.0,170.0,95.0, "Red",canvas)
pave23 = Object(490.25,380.0,549.75,105.0, "Light Grey",canvas)
object29 = Object(495.25,385.0,539.75,95.0, "Red",canvas)

#Sixth Row
pave13 = Object(50.0,525.0,276.5,35.0, "Light Grey",canvas)
object16 = Object(55.0,530.0,266.5,25.0, "Red",canvas)
pave14 = Object(366.0,525.0,544.0,35.0, "Light Grey",canvas)
object17 = Object(371.0,530.0,534.0,25.0,"Red",canvas)
pave16 = Object(910.0,525.0,170.0,150.0, "Light Grey",canvas)
object19 = Object(915.0,530.0,160.0,140.0, "red",canvas)

#Seventh Row
pave17 = Object(50.0,600.0,180.25,35.0,"Light Grey",canvas)
object20 = Object(55.0,605.0,170.0,25.0, "red",canvas)
pave18 = Object(271.25,600.0,207.75,35.0, "Light Grey",canvas)
object21 = Object(276.25,605.0,197.75,25.0, "Red",canvas)
pave19 = Object(519.0,600.0,351.0,35.0,"Light Grey",canvas)
object22 = Object(524,605,341.0,25.0, "Red",canvas)

#Eighth Row
pave20 = Object(10.0,675.0,1070.0,35.0, "Light Grey",canvas)
object23 = Object(10.0,680.0,200.0, 25.0, "Red",canvas)
object24 = Object(290.0,680.0,200.0,25.0, "Red",canvas)
object25 = Object(580.0,680.0,500.0,25.0, "Red",canvas)

#Roads
Road1=road('Road1',10,45,1070,40) 
Road2=road('Road2',10,45,40,630)
Road3=road('Road3',1040,45,40,480)
Road4=road('Road4',945,45,40,190)
Road5=road('Road5',945,195,135,40)
Road6=road('Road6',10,195,900,40)
Road7=road('Road7',870,45,40,190)
Road8=road('Road8',450.25,340,40,145)
Road9=road('Road9',404,45,40,115)
Road10=road('Road10',10,120,434,40)
Road11=road('Road11',231.25,195,40,330)
Road12=road('Road12',479,120,431,40)
Road13=road('Road13',10,340,1070,40)
Road14=road('Road14',10,485,1070,40)
Road15=road('Road15',479,45,40,190)
Road16=road('Road16',10,560,900,40)
Road17=road('Road17',326,485,40,115)
Road19=road('Road19',10,635,900,40)
Road20=road('Road20',230.25,560,40,115)
Road21=road('Road21',479,560,40,115) 
Road22=road('Road22',870,560,40,115) 

Roads=[Road1,Road2,Road3,Road4,Road5,Road6,Road7,Road8,Road9,Road10,Road11,Road12,Road13,Road14,Road16,Road17,Road19,Road20,Road21,Road22]

#Landmarks
#This section of code uses the constructor in the the landmark class to generate the landmarks the robot should visit
#if a treasure is present
Landmark1 = landmark(55.0,67.0,10.0,20.0,"blue",canvas,"Dave",False,Road1)
#Everything encased in brackets relates to variables pre-defined in the landmark class
Landmark2 = landmark(200.0,583.0,10.0,20.0,"blue",canvas,"Jason",True,Road16)
Landmark3 = landmark(383.0,508.0,10.0,20.0,"blue",canvas,"Kim",False,Road14)
Landmark4 = landmark(860.25,363.0,10.0,20.0,"blue",canvas,"Matt",False,Road13)
Landmark5 = landmark(990.0,67.0,10.0,20.0,"blue",canvas,"Pete",False,Road1)
Landmark6 = landmark(519.0,143.0,10.0,20.0,"blue",canvas,"Rose",True,Road12)
Landmark7 = landmark(590.25,363.0,10.0,20.0,"blue",canvas,"Mark",False,Road13)
Landmark8 = landmark(90.0,143.0,10.0,20.0,"blue",canvas,"Roshel",True,Road10)
Landmark9 = landmark(366.0,583.0,10.0,20.0,"blue",canvas,"Lucy",False,Road16)
Landmark10 = landmark(800,583.0,10.0,20.0,"BLUE",canvas,"Ben",True,Road16)

ListOfLandmarks=[Landmark1,Landmark2,Landmark3,Landmark4,Landmark5,Landmark6,Landmark7,Landmark8,Landmark9,Landmark10]

#Treasures
#This section utilises the constructor in the treasure class to create the treasures the robot should collect
Treasure1 = treasure(200.0,578.0,10.0,5.0,"dark green",canvas,False,100)
#everything encased in brackets relates to a variable pre-defined in the treasure class
Treasure3 = treasure(519.0,138.0,10.0,5.0,"dark green",canvas,False,100)
Treasure4 = treasure(90.0,138.0,10.0,5.0,"dark green", canvas, False,100)
Treasure5 = treasure(800.0,578.0,10.0,5.0,"dark green",canvas,False,100)
ListOfTreasures = [Treasure1,Treasure3,Treasure4,Treasure5]
Total = Treasure1.points  + Treasure3.points + Treasure4.points + Treasure5.points
Distribution = Total / 4

#Lights
#Column 1
Light1 = light(20, 130, 40, 150, "Green")
Light2 = light(20, 205, 40, 225, "Green")
Light3 = light(20, 350, 40, 370, "Green")
Light4 = light(20, 495, 40, 515, "Green")
Light5 = light(20.0, 570, 40, 590, "Green")

#Column 2
Light6 = light(240, 130, 260, 150, "Green")
Light7 = light(240, 205, 260, 225, "Green")
Light8 = light(240, 350, 260, 370, "Green")
Light9 = light(240, 495, 260, 515, "Green")
Light10 = light(240, 570, 260, 590, "Green")
Light11 = light(240, 645, 260, 665, "Green")

#Column 3
Light12 = light(415, 55, 435, 75, "Green")
Light13 = light(335, 495, 355, 515, "Green")
Light14 = light(335, 570, 355, 590, "Green")

#Column 4
Light15 = light(490, 55, 510, 75, "Green")
Light16 = light(490, 130, 510, 150, "Green")
Light17 = light(490, 210, 510, 230, "Green")
Light18 = light(490, 350, 510, 370, "Green")
Light19 = light(490, 495, 510, 515, "Green")
Light20 = light(490, 570, 510, 590, "Green")
Light21 = light(490, 645, 510, 665, "Green")

#Column 5
Light24 = light(880, 55, 900, 75, "Green")
Light25 = light(880, 130, 900, 150, "Green")

#Column 6
Light26 = light(955, 55, 975, 75, "Green")

#Column 7
Light27 = light(1040, 205, 1060, 225, "Green")
Light28 = light(1040, 350, 1060, 370, "Green")

def stopTheBot():
    global robowait
    if ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>110) and(c3po.y1<170) and (robowait==True)) or ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>199) and(c3po.y1<231) and (robowait==True)) or ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>310) and(c3po.y1<360) and (robowait==True)) or ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>490) and(c3po.y1<520) and (robowait==True)) or ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>550) and(c3po.y1<600) and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>110) and(c3po.y1<170) and (robowait==True)) or ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>195) and(c3po.y1<210) and (robowait==True)) or ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>330) and(c3po.y1<390)and (robowait==True))  or ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>485) and(c3po.y1<530)and (robowait==True)) or ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>555) and(c3po.y1<605)and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>625) and(c3po.y1<675) and (robowait==True)) or ( (c3po.x1>400) and (c3po.x1<450) and (c3po.y1>40) and(c3po.y1<90) and (robowait==True)) or ( (c3po.x1>320) and (c3po.x1<370) and (c3po.y1>480) and(c3po.y1<525) and (robowait==True)) or ( (c3po.x1>320) and (c3po.x1<370) and (c3po.y1>550) and(c3po.y1<605) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>45) and(c3po.y1<90) and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>115) and(c3po.y1<105) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>195) and(c3po.y1<245) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>335) and(c3po.y1<385) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>480) and(c3po.y1<530) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>555) and(c3po.y1<605) and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>630) and(c3po.y1<680) and (robowait==True)) or ( (c3po.x1>865) and (c3po.x1<915) and (c3po.y1>40) and(c3po.y1<90) and (robowait==True)) or ( (c3po.x1>865) and (c3po.x1<915) and (c3po.y1>110) and(c3po.y1<170) and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (c3po.x1>940) and (c3po.x1<990) and (c3po.y1>40) and(c3po.y1<90) and (robowait==True)) or ( (c3po.x1>1020) and (c3po.x1<1080) and (c3po.y1>190) and(c3po.y1<240) and (robowait==True)) or ( (c3po.x1>1020) and (c3po.x1<1080) and (c3po.y1>330) and(c3po.y1<390) and (robowait==True)):
        time.sleep(1)
        flipColour()
    if ( (r2d2.x1>10) and (r2d2.x1<60) and (r2d2.y1>110) and(r2d2.y1<170) and (robowait==True)) or ( (r2d2.x1>10) and (r2d2.x1<60) and (r2d2.y1>199) and(r2d2.y1<231) and (robowait==True)) or ( (r2d2.x1>10) and (r2d2.x1<60) and (r2d2.y1>310) and(r2d2.y1<360) and (robowait==True)) or ( (r2d2.x1>10) and (r2d2.x1<60) and (r2d2.y1>490) and(r2d2.y1<520) and (robowait==True)) or ( (r2d2.x1>10) and (r2d2.x1<60) and (r2d2.y1>550) and(r2d2.y1<600) and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (r2d2.x1>225) and (r2d2.x1<275) and (r2d2.y1>110) and(r2d2.y1<170) and (robowait==True)) or ( (r2d2.x1>225) and (r2d2.x1<275) and (r2d2.y1>195) and(r2d2.y1<210) and (robowait==True)) or ( (r2d2.x1>225) and (r2d2.x1<275) and (r2d2.y1>330) and(r2d2.y1<390)and (robowait==True))  or ( (r2d2.x1>225) and (r2d2.x1<275) and (r2d2.y1>485) and(r2d2.y1<530)and (robowait==True)) or ( (r2d2.x1>225) and (r2d2.x1<275) and (r2d2.y1>555) and(r2d2.y1<605)and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (r2d2.x1>225) and (r2d2.x1<275) and (r2d2.y1>625) and(r2d2.y1<675) and (robowait==True)) or ( (r2d2.x1>400) and (r2d2.x1<450) and (r2d2.y1>40) and(r2d2.y1<90) and (robowait==True)) or ( (r2d2.x1>320) and (r2d2.x1<370) and (r2d2.y1>480) and(r2d2.y1<525) and (robowait==True)) or ( (r2d2.x1>320) and (r2d2.x1<370) and (r2d2.y1>550) and(r2d2.y1<605) and (robowait==True)) or ( (r2d2.x1>475) and (r2d2.x1<520) and (r2d2.y1>45) and(r2d2.y1<90) and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (r2d2.x1>475) and (r2d2.x1<520) and (r2d2.y1>115) and(r2d2.y1<105) and (robowait==True)) or ( (r2d2.x1>475) and (r2d2.x1<520) and (r2d2.y1>195) and(r2d2.y1<245) and (robowait==True)) or ( (r2d2.x1>475) and (r2d2.x1<520) and (r2d2.y1>335) and(r2d2.y1<385) and (robowait==True)) or ( (r2d2.x1>475) and (r2d2.x1<520) and (r2d2.y1>480) and(r2d2.y1<530) and (robowait==True)) or ( (r2d2.x1>475) and (r2d2.x1<520) and (r2d2.y1>555) and(r2d2.y1<605) and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (c3po.x1>475) and (r2d2.x1<520) and (r2d2.y1>630) and(r2d2.y1<680) and (robowait==True)) or ( (r2d2.x1>865) and (r2d2.x1<915) and (r2d2.y1>40) and(r2d2.y1<90) and (robowait==True)) or ( (r2d2.x1>865) and (r2d2.x1<915) and (r2d2.y1>110) and(r2d2.y1<170) and (robowait==True)):
        time.sleep(1)
        flipColour()
    elif ( (c3po.x1>940) and (r2d2.x1<990) and (r2d2.y1>40) and(r2d2.y1<90) and (robowait==True)) or ( (r2d2.x1>1020) and (r2d2.x1<1080) and (r2d2.y1>190) and(r2d2.y1<240) and (robowait==True)) or ( (r2d2.x1>1020) and (r2d2.x1<1080) and (r2d2.y1>330) and(r2d2.y1<390) and (robowait==True)):
        time.sleep(1)
        flipColour()

def flipColour():
    global robowait
    if colourChanger==1:
        robowait=True
        Light1.change_colour("Red")
        Light2.change_colour("Red")
        Light3.change_colour("Red")
        Light4.change_colour("Red")
        Light5.change_colour("Red")
        Light6.change_colour("Red")
        Light7.change_colour("Red")
        Light8.change_colour("Red")
        Light9.change_colour("Red")
        Light10.change_colour("Red")
        Light11.change_colour("Red")
        Light12.change_colour("Red")
        Light13.change_colour("Red")
        Light14.change_colour("Red")
        Light15.change_colour("Red")
        Light16.change_colour("Red")
        Light17.change_colour("Red")
        Light18.change_colour("Red")
        Light19.change_colour("Red")
        Light20.change_colour("Red")
        Light21.change_colour("Red")
        Light24.change_colour("Red")
        Light25.change_colour("Red")
        Light26.change_colour("Red")
        Light27.change_colour("Red")
        Light28.change_colour("Red")
        canvas.update()
    if colourChanger==2:
        c3po.speed=1
        robowait=False
        Light1.change_colour("Green")
        Light2.change_colour("Green")
        Light3.change_colour("Green")
        Light4.change_colour("Green")
        Light5.change_colour("Green")
        Light6.change_colour("Green")
        Light7.change_colour("Green")
        Light8.change_colour("Green")
        Light9.change_colour("Green")
        Light10.change_colour("Green")
        Light11.change_colour("Green")
        Light12.change_colour("Green")
        Light13.change_colour("Green")
        Light14.change_colour("Green")
        Light15.change_colour("Green")
        Light16.change_colour("Green")
        Light17.change_colour("Green")
        Light18.change_colour("Green")
        Light19.change_colour("Green")
        Light20.change_colour("Green")
        Light21.change_colour("Green")
        Light24.change_colour("Green")
        Light25.change_colour("Green")
        Light26.change_colour("Green")
        Light27.change_colour("Green")
        Light28.change_colour("Green")
    if colourChanger==3:
        c3po.speed=1
        robowait=False
        Light1.change_colour("Yellow")
        Light2.change_colour("Yellow")
        Light3.change_colour("Yellow")
        Light4.change_colour("Yellow")
        Light5.change_colour("Yellow")
        Light6.change_colour("Yellow")
        Light7.change_colour("Yellow")
        Light8.change_colour("Yellow")
        Light9.change_colour("Yellow")
        Light10.change_colour("Yellow")
        Light11.change_colour("Yellow")
        Light12.change_colour("Yellow")
        Light13.change_colour("Yellow")
        Light14.change_colour("Yellow")
        Light15.change_colour("Yellow")
        Light16.change_colour("Yellow")
        Light17.change_colour("Yellow")
        Light18.change_colour("Yellow")
        Light19.change_colour("Yellow")
        Light20.change_colour("Yellow")
        Light21.change_colour("Yellow")        
        Light24.change_colour("Yellow")
        Light25.change_colour("Yellow")
        Light26.change_colour("Yellow")
        Light27.change_colour("Yellow")
        Light28.change_colour("Yellow")

c3po = robot(0, 0, speed = 1, size=20, colour='yellow')
c3po.randomPosition()
c3po.drawRobot()
c3po.pathfinder()
r2d2 = robot(0,0,speed = 1, size=20, colour='White')
r2d2.randomPosition()
r2d2.drawRobot()
r2d2.pathfinder()
RobotList = [c3po,r2d2]

main.mainloop()
