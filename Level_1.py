from Tkinter import *
import random
import math
import time

main = Tk(className = "Level 1")
canvas = Canvas(main, width = 1280, height = 720, bg = "Black")
canvas.pack()

global resetpressed
resetpressed=False
global pausepressed
pausepressed=False
global programispaused
programispaused= False
global paused
paused = False
global randomColourChangerYellow
randomColourChangerYellow=0
global colourChanger
colourChanger=0
global robowait
robowait=False
global RoboFinished
RoboFinished = False
global Score
Score=0

def BFS(route, start, end):
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
        return next(BFS(route, start, end))
    except StopIteration:
        return None

class Object: #This class is used for the obstacles the robot needs to avoid
    def __init__(self,x,y,length,width,colour,canvas): #This is the constructor which is used to actually create the obstacles
        global ObjectList
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.colour = colour
        self.canvas=canvas   
        self.object = canvas.create_rectangle(self.x,self.y,self.x+self.length,self.y+self.width,fill = self.colour)

class landmark(Object): #This is the class which is used for the landmarks the robot needs to visit
    def __init__(self,x,y,length,width,colour,canvas,Id,treasure,Road):# This is the constructor which is used to generate the landmarks and place them on the map
        Object.__init__(self,x,y,length,width,colour,canvas)
        self.Id=Id
        self.treasure=treasure
        self.Road=Road
        
class treasure(Object): # This is the class which is used for the treasure that the robot needs to collect
    def __init__(self,x,y,length,width,colour,canvas,Found,points):#This is the constructor which is used to generate the treasure for the robot to find
        Object.__init__(self,x,y,length,width,colour,canvas)
        self.Found = Found
        self.points = points
        
class interface: #This is the class for all interface elements
    def __init__(self, name):
        self.start_button = Button(name, text="Start", width = 20, command=self.start, bg = "Green")#This is the constructor for the start button 
        self.start_button.place(x = 1110, y = 150)#Places the button at those x & y coords       

        self.Level2_button = Button(name, text="Level 2", width = 20, command=self.level2, bg = "Yellow")
        self.Level2_button.place(x = 1110, y = 250)

        self.Level3_button = Button(name, text="Level 3", width = 20, command=self.level3, bg = "Yellow")
        self.Level3_button.place(x = 1110, y = 300)

        self.timerShow_label = Label(name, text = "", width = 7, font = ("Arial", 16))
        self.timerShow_label.place(x = 1170, y = 30)

        self.timer_label= Label(name,text ="Timer", width = 5, font = ("Arial", 16))
        self.timer_label.place(x = 1110, y = 30)

        self.treasures_label = Label(name, text = "Treasure Remaining: ", width = 16, height = 2, font = ("Arial", 12), anchor = N)
        self.treasures_label.place(x = 1110, y = 70)

        self.treasureShow_label = Label(name, text = "1", width = 16, font = ("Arial", 12))
        self.treasureShow_label.place(x = 1110, y = 100)

        self.robot1Score_label = Label(name, text = "Robot Score: ", width = 16, height = 1, font = ("Arial", 12), anchor = N)
        self.robot1Score_label.place(x = 1110, y = 350)

        self.robot1Score_label = Label(name, text = "0", width = 16, font = ("Arial", 12))
        self.robot1Score_label.place(x = 1110, y = 370)
        
    def start(self):#Starts the robot and timer
        global resetpressed, RoboFinished
        interface.start_button.place_forget()#Makes the button disappear when the button is pressed
        interface.counterLabel(interface)
        for t in range (0,10000):
            for robot in RobotList:
                if robot.vx==0 and robot.vy==0:
                    break
                else:
                    robot.move()
                    time.sleep(0.0025)

    def level2():
        destroy.main()#Destroys the window
        import Level_2 #Imports Level 2

    def level3():
        destroy.main()
        import Level_3

    def count(main):
        global counter, resetpressed, pausepressed, colourChanger
        counter==counter
        global RoboFinished
        if (RoboFinished != True):
            counter=counter+1
            if colourChanger!=2:
                colourChanger=colourChanger+1
            else:
                colourChanger=0
            main.timerShow_label.config(text = str(counter))
            flipColour()
            main.timerShow_label.after(1000, main.count) 
        else:
            main.counterStop()

    def counterStop(main):
        Score=100
        interface.robot1Score_label.config(text = str(Score))
        interface.treasureShow_label.config(text= "0")

    def counterLabel(main,self):
        
            global counter, RoboFinished
            counter=0
            RoboFinished=False
            if counter!=1000000:
                interface.count()
                
    def negcounter(main):
        global programispaused, counter, pausebuffer
        if programispaused==True:
            counter=counter-1
            pausebuffer=pausebuffer-1
            if pausebuffer<0:
                main.pause_button.place(x = 1110, y = 200)
            main.timerShow_label.after(1000, main.negcounter)
        else: print "placeholder"

class light(interface):#This class is used for the lights that the robot has to obey
    def __init__(self,x0,y0,x1,y1,colour):#This is the constructor which is used to actually create the lights
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.colour = colour
        self.object = canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill = self.colour)

    def changeColour(self, colour):#This is the function that changes the lights colour
        canvas.itemconfig(self.object, fill=colour)
        canvas.update()

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
        self.Route=[]
        self.city = {Road1:set([Road2, Road9, Road7, Road4, Road3, Road15]),
                    Road2:set([Road1,Road10,Road5,Road13,Road14,Road16, Road19]),
                    Road3:set([Road1,Road5,Road13,Road14]),
                    Road4:set([Road1,Road5]),
                    Road5:set([Road3, Road4]),
                    Road6:set([Road2,Road11,Road15,Road7]),
                    Road7:set([Road6,Road12,Road1]),
                    Road9:set([Road1,Road10]),
                    Road10:set([Road9,Road2,Road11]),
                    Road11:set([Road10,Road6,Road13, Road14]),
                    Road12:set([Road7, Road15]),
                    Road13:set([Road2,Road11,Road15,Road3]),
                    Road14:set([Road2,Road17,Road15,Road18, Road3,Road11]),
                    Road15:set([Road6,Road13,Road14]),
                    Road16:set([Road2,Road20,Road17,Road21,Road22]),
                    Road17:set([Road14,Road16]),
                    Road18:set([Road14,Road16]),
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
        if len(self.Route)-1<self.IteminRoute:
            stopTheBot()          
            if self.ClosestLandmark.x>(self.x1+(self.size/2)):
                self.vx=self.speed
                self.vy=0
            elif self.ClosestLandmark.x<(self.x1+(self.size/2)):
                self.vx=-self.speed
                self.vy=0
            else:
                self.vx=0
                self.vy=0
        else:
            self.NextRoad=self.Route[self.IteminRoute]
            if self.NextRoad.height>self.NextRoad.width:
                stopTheBot()
                x_destination=self.NextRoad.x1+self.NextRoad.width/2
                if x_destination>(self.x1+(self.size/2)):
                    self.vx=self.speed
                    self.vy=0
                elif x_destination<(self.x1+(self.size/2)):
                    self.vx=-self.speed
                    self.vy=0
                else:
                    self.IteminRoute+=1
            elif self.NextRoad.height<self.NextRoad.width:
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

interface = interface(main)

#Roads
Road1=road('Road1',10,45,1070,40) 
Road2=road('Road2',10,45,40,630)
Road3=road('Road3',1040,45,40,480)
Road4=road('Road4',945,45,40,190)
Road5=road('Road5',945,195,135,40)
Road6=road('Road6',10,195,900,40)
Road7=road('Road7',870,45,40,190)
Road9=road('Road9',404,45,40,115)
Road10=road('Road10',10,120,434,40)
Road11=road('Road11',231.25,120,40,405)
Road12=road('Road12',479,120,431,40)
Road13=road('Road13',10,340,1070,40)
Road14=road('Road14',10,485,1070,40)
Road15=road('Road15',479,45,40,480)
Road16=road('Road16',10,560,900,40)
Road17=road('Road17',326,485,40,115)
Road18=road('Road18',717,485,40,115)
Road19=road('Road19',10,635,900,40)
Road20=road('Road20',230.25,560,40,115)
Road21=road('Road21',479,560,40,115) 
Road22=road('Road22',870,560,40,115) 
Road20=road('Road20',230.25,560,40,115)

Roads=[Road1,Road2,Road3,Road4,Road5,Road6,Road7,Road9,Road10,Road11,Road12,Road13,Road14,Road15,Road16,Road17,Road18,Road19,Road20,Road21,Road22]

#Objects & Landmarks
#The following section of code utilises the constructor saw earlier on in the program to create objects for the robot to avoid
#Top Row
pave1 = Object(10.0,10.0,1070.0,35.0, "Light Grey",canvas)
#Everything encased in brackets relates to a variable pre defined in the constructor
object1 = Object(10.0,15.0,200.0, 25.0, "Red",canvas)
object2 = Object(290.0,15.0,200.0,25.0, "Red",canvas)
object3 = Object(580.0,15.0,200.0,25.0, "Red",canvas)
object4 = Object(870.0,15.0,210.0,25.0, "Red",canvas)

#second row
pave2 = Object(50.0,85.0,354.0,35.0, "Light Grey",canvas)
object5 = Object(55.0,90.0,344.0,25.0,"Red", canvas)
pave3 = Object(444.0,85.0,35.0,110.0,"Light Grey",canvas)
object6 = Object(449.0,90.0,25.0,100.0, "Red",canvas)
pave4 = Object(519.0,85.0,351.0,35.0,"Light Grey",canvas)
object7 = Object(524.0,90.0,341.0,25.0,"Red",canvas)
pave5 = Object(910.0,85.0,35.0,150.0,"Light Grey",canvas)
object8 = Object(915.0,90.0,25.0,140.0,"Red",canvas)
pave6 = Object(985.0,85.0,55.0,110.0,"Light Grey",canvas)
object9 = Object(990.0,90.0,45.0,100.0, "Red",canvas)

#Third Row
pave7 = Object(50.0,160.0,180.25,35.0,"Light Grey", canvas)
object10 = Object(55.0,165.0,170.0,25.0,"Red", canvas)
pave8 = Object(271.25,160,172.75,35.0, "Light Grey", canvas)
object11 = Object(276.25,165.0,162.75,25.0, "Red",  canvas)
pave9 = Object(519.0,160.0,351.0,35.0,"Light Grey",canvas)
object12 = Object(524.0,165.0,341.0,25.0,"Red",canvas)

#Fourth Row
pave10 = Object(50.0,235.0,180.25,105.0, "Light Grey", canvas)
object13 = Object(55.0,240.0,170.25,95.0, "red", canvas)
pave11 = Object(270.25, 235.0, 208.75,105.0, "Light Grey",canvas)
object14 = Object(275.0, 240.0,198.5,95.0, "Red",canvas)
pave12 = Object(524.25,235.0,515.75,105.0, "Light Grey",canvas)
object15 = Object(529.25,240.0,505.75,95.0, "Red",canvas)

#Fifth Row
pave21 = Object(50.0,380.0,180.25,105.0, "Light Grey",canvas)
object27 = Object(55.0,385.0,170.25,95.0, "Red", canvas)
pave22 = Object(270.25, 380.0, 208.75,105.0, "Light Grey",canvas)
object28 = Object(275.0, 385.0,198.5,95.0, "Red",canvas)
pave23 = Object(524.25,380.0,515.75,105.0, "Light Grey",canvas)
object29 = Object(529.0,385.0,505.75,95.0, "Red",canvas)

#Sixth Row
pave13 = Object(50.0,525.0,276.5,35.0, "Light Grey",canvas)
object16 = Object(55.0,530.0,266.5,25.0, "Red",canvas)
pave14 = Object(366.0,525.0,351.0,35.0, "Light Grey",canvas)
object17 = Object(371.0,530.0,341.0,25.0,"Red",canvas)
pave15 = Object(757.0,525.0,153.0,35.0, "Light Grey", canvas)
object18 = Object(762.0,530.0,143.0,25.0,"Red",canvas)
pave16 = Object(910.0,525.0,170.0,150.0, "Light Grey",canvas)
object19 = Object(915.0,530.0,160.0,140.0, "Red",canvas)

#Seventh Row
pave17 = Object(50.0,600.0,180.25,35.0,"Light Grey",canvas)
object20 = Object(55.0,605.0,170.0,25.0, "Red",canvas)
pave18 = Object(271.25,600.0,207.75,35.0, "Light Grey",canvas)
object21 = Object(276.25,605.0,197.75,25.0, "Red",canvas)
pave19 = Object(519.0,600.0,351.0,35.0,"Light Grey",canvas)
object22 = Object(524,605,341.0,25.0, "Red",canvas)

#Eighth Row
pave20 = Object(10.0,675.0,1070.0,35.0, "Light Grey",canvas)
object23 = Object(10.0,680.0,200.0, 25.0, "Red",canvas)
object24 = Object(290.0,680.0,200.0,25.0, "Red",canvas)
object25 = Object(580.0,680.0,200.0,25.0, "Red",canvas)
object26 = Object(870.0,680.0,210.0,25.0, "Red",canvas)

#Landmarks
#This section of code relates to the constructor in the landmark class, it generates landmarks that the robot should visit
#if a treasure is present
Landmark1 = landmark(55.0,67.0,10.0,20.0,"blue",canvas,"Dave",True,Road1)
#Everything encased in brackets relates to a variable pre-defined in the constructor
Landmark2 = landmark(200.0,583.0,10.0,20.0,"blue",canvas,"Jason",False,Road16)
Landmark3 = landmark(383.0,508.0,10.0,20.0,"blue",canvas,"Kim",False,Road14)
Landmark4 = landmark(860.25,363.0,10.0,20.0,"blue",canvas,"Matt",False,Road13)
Landmark5 = landmark(990.0,67.0,10.0,20.0,"blue",canvas,"Pete",False,Road1)
Landmark6 = landmark(519.0,143.0,10.0,20.0,"blue",canvas,"Rose",False,Road12)
ListOfLandmarks=[Landmark1,Landmark2,Landmark3,Landmark4,Landmark5,Landmark6]
#Treasures
#This section of code relates to the constructor in the Treasure class, it generates treasures that the robot should
#collected
Treasure1 = treasure(55.0,62.0,10.0,5.0,"dark green",canvas,False,100)
#Everything encased in brackets relates to a variable pre-defined in the constructor

#Lights
#The following section of code utilises the constructor in the light class used to create lights for the robot to obey
#Column 1
Light1 = light(20.0,130.0,40,150,"Green")
#Everything encased in brackets relates to a variable pre defined in the constructor
Light2 = light(20.0,205.0,40,225,"Green") 
Light3 = light(20.0, 350.0, 40, 370.0, "Green")
Light4 = light(20.0, 495, 40, 515, "Green")
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
Light22 = light(725, 495, 745, 515, "Green")
Light23 = light(725, 570, 745, 590, "Green")

#Column 6
Light24 = light(880, 55, 900, 75, "Green")
Light25 = light(880, 130, 900, 150, "Green")

#Column 7
Light26 = light(955, 55, 975, 75, "Green")

#Column 8
Light27 = light(1040, 205, 1060, 225, "Green")
Light28 = light(1040, 350, 1060, 370, "Green")

def stopTheBot(): #Stops the robot if a red light is present at its coords
    global robowait
    global RoboFinished
   
    if ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>110) and(c3po.y1<170) and (robowait==True)) or ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>199) and(c3po.y1<231) and (robowait==True)) or ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>310) and(c3po.y1<360) and (robowait==True)) or ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>490) and(c3po.y1<520) and (robowait==True)) or ( (c3po.x1>10) and (c3po.x1<60) and (c3po.y1>550) and(c3po.y1<600) and (robowait==True)):
        time.sleep(1)
        
    elif ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>110) and(c3po.y1<170) and (robowait==True)) or ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>195) and(c3po.y1<210) and (robowait==True)) or ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>330) and(c3po.y1<390)and (robowait==True))  or ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>485) and(c3po.y1<530)and (robowait==True)) or ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>555) and(c3po.y1<605)and (robowait==True)):
        time.sleep(1)
        
    elif ( (c3po.x1>225) and (c3po.x1<275) and (c3po.y1>625) and(c3po.y1<675) and (robowait==True)) or ( (c3po.x1>400) and (c3po.x1<450) and (c3po.y1>40) and(c3po.y1<90) and (robowait==True)) or ( (c3po.x1>320) and (c3po.x1<370) and (c3po.y1>480) and(c3po.y1<525) and (robowait==True)) or ( (c3po.x1>320) and (c3po.x1<370) and (c3po.y1>550) and(c3po.y1<605) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>45) and(c3po.y1<90) and (robowait==True)):
        time.sleep(1)
        
    elif ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>115) and(c3po.y1<105) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>195) and(c3po.y1<245) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>335) and(c3po.y1<385) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>480) and(c3po.y1<530) and (robowait==True)) or ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>555) and(c3po.y1<605) and (robowait==True)):
        time.sleep(1)
       
    elif ( (c3po.x1>475) and (c3po.x1<520) and (c3po.y1>630) and(c3po.y1<680) and (robowait==True)) or ( (c3po.x1>710) and (c3po.x1<760) and (c3po.y1>480) and(c3po.y1<500) and (robowait==True)) or ( (c3po.x1>710) and (c3po.x1<760) and (c3po.y1>555) and(c3po.y1<605) and (robowait==True))  or ( (c3po.x1>865) and (c3po.x1<915) and (c3po.y1>40) and(c3po.y1<90) and (robowait==True)) or ( (c3po.x1>865) and (c3po.x1<915) and (c3po.y1>110) and(c3po.y1<170) and (robowait==True)):
        time.sleep(1)
        
    elif ( (c3po.x1>940) and (c3po.x1<990) and (c3po.y1>40) and(c3po.y1<90) and (robowait==True)) or ( (c3po.x1>1020) and (c3po.x1<1080) and (c3po.y1>190) and(c3po.y1<240) and (robowait==True)) or ( (c3po.x1>1020) and (c3po.x1<1080) and (c3po.y1>330) and(c3po.y1<390) and (robowait==True)):
        time.sleep(1)

    if (c3po.x1>41) and (c3po.x1<71) and (c3po.x1>51) and (c3po.x1<99):
        RoboFinished=True

def flipColour():
    global robowait
    if colourChanger==1:
        robowait=True
        Light1.changeColour("Red")
        Light2.changeColour("Red")
        Light3.changeColour("Red")
        Light4.changeColour("Red")
        Light5.changeColour("Red")
        Light6.changeColour("Red")
        Light7.changeColour("Red")
        Light8.changeColour("Red")
        Light9.changeColour("Red")
        Light10.changeColour("Red")
        Light11.changeColour("Red")
        Light12.changeColour("Red")
        Light13.changeColour("Red")
        Light14.changeColour("Red")
        Light15.changeColour("Red")
        Light16.changeColour("Red")
        Light17.changeColour("Red")
        Light18.changeColour("Red")
        Light19.changeColour("Red")
        Light20.changeColour("Red")
        Light21.changeColour("Red")
        Light22.changeColour("Red")
        Light23.changeColour("Red")
        Light24.changeColour("Red")
        Light25.changeColour("Red")
        Light26.changeColour("Red")
        Light27.changeColour("Red")
        Light28.changeColour("Red")
        canvas.update()
    if colourChanger==2:
        c3po.speed=1
        robowait=False
        Light1.changeColour("Green")
        Light2.changeColour("Green")
        Light3.changeColour("Green")
        Light4.changeColour("Green")
        Light5.changeColour("Green")
        Light6.changeColour("Green")
        Light7.changeColour("Green")
        Light8.changeColour("Green")
        Light9.changeColour("Green")
        Light10.changeColour("Green")
        Light11.changeColour("Green")
        Light12.changeColour("Green")
        Light13.changeColour("Green")
        Light14.changeColour("Green")
        Light15.changeColour("Green")
        Light16.changeColour("Green")
        Light17.changeColour("Green")
        Light18.changeColour("Green")
        Light19.changeColour("Green")
        Light20.changeColour("Green")
        Light21.changeColour("Green")
        Light22.changeColour("Green")
        Light23.changeColour("Green")
        Light24.changeColour("Green")
        Light25.changeColour("Green")
        Light26.changeColour("Green")
        Light27.changeColour("Green")
        Light28.changeColour("Green")


#Robot
c3po = robot(0, 0, speed = 1, size=20, colour='yellow')
c3po.randomPosition()
c3po.drawRobot()
c3po.pathfinder()
RobotList = [c3po]

main.mainloop()
