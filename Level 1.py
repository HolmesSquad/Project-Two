from Tkinter import *
import random
main = Tk(className = "Level 1")
canvas = Canvas(main, width = 1280, height = 720, bg = "Black")
canvas.pack()

def DFS(route, start, end): #Graph and start node as arguments
    path=[] #List of nodes in the path 
    queue=[start] #Queue list 
    while queue: #While list is not empty
        v=queue.pop(0) #Remove node from list
        if v == end:
            return path
        if v not in path: #If node v has not been checked yet
            path=path+[v] #Add node to path list
            queue=route[v]+queue #Add node's neighbors at the beginning of the list 
    return path



class objects:

    def __init__(self,x,y,length,width,colour,TreasurePresent,canvas):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.colour = colour
        self.TreasurePresent = TreasurePresent
        self.canvas=canvas
        self.object = canvas.create_rectangle(self.x,self.y,self.x+self.length,self.y+self.width,fill = self.colour)

class light:

    def __init__(self,x0,y0,x1,y1,colour):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.colour = colour
        self.object = canvas.create_oval(self.x0,self.y0,self.x1,self.y1,fill = self.colour)




class Road:
    def __init__(self,name,x,y,width,height):
        self.name=name
        self.x1=x
        self.y1=y
        self.x2=x+width
        self.y2=y+height
        self.width=width
        self.height=height
        self.object=canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill="darkgrey", width=0)

class Robot:
    def __init__(self,x,y,speed=1.0,size=20,colour='blue'):
        self.x1=x
        self.y1=y
        self.x2=x+size
        self.y2=y+size
        self.colour=colour
        self.speed=speed
        self.size=size
        self._vx=0
        self._vy=0
    def drawRobot(self):
        self.canvas=canvas
        self.shape=canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill=self.colour)
    #Give the robot a random position (Use this before drawing the robot)
    def RandomPosition(self):
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
    def CheckPosition(self):
        for road in Roads:
            if self.x1>=road.x1 and self.x2<=road.x2 and self.y1>=road.y1 and self.y2<=road.y2:
                return road.name



    def Move(self):
        
        route = {'Road1':['B', 'C'], 'B':['E'], 'C':['E', 'D'], 'D':['E'], 'E':['F'], 'F':[]} #Connectivity 
        print 'DFS path: ', DFS(route, self.CheckPosition())

'''class button:

    def __init__(self, name, text, width, command, bg, x, y):
        self.name = name
        self.text = text
        self.width = width
        self.command = command
        self.bg = bg
        self.x = x
        self.y = y
        self.canvas = canvas
        self.button = Button(self.name, self.text, self.width, self.command, self.bg)
        self.button.place = (self.x, self.y)
        
        
    def test1(self):
        print "test1"

button1 = button(main,"Test", 10, button.test1, "Green", 10, 10)'''
Road1=Road('Road1',10,45,1070,40)
Road2=Road('Road2',10,45,40,630)
Road3=Road('Road3',1040,45,40,480)
Road4=Road('Road4',945,45,40,190)
Road5=Road('Road5',945,195,135,40)
Road6=Road('Road6',10,195,900,40)
Road7=Road('Road7',870,45,40,190)
Road8=Road('Road8',479,45,40,190)
Road9=Road('Road9',404,45,40,115)
Road10=Road('Road10',10,120,434,40)
Road11=Road('Road11',231.25,120,40,405)
Road12=Road('Road12',479,120,431,40)
Road13=Road('Road13',10,340,1070,40)
Road14=Road('Road14',10,485,1070,40)
Road15=Road('Road15',450.25,195,40,330)
Road16=Road('Road16',10,560,900,40)
Road17=Road('Road17',326,485,40,115)
Road18=Road('Road18',717,485,40,115)
Road19=Road('Road19',10,635,900,40)
Road20=Road('Road20',230.25,560,40,115)
Road21=Road('Road21',479,560,40,115)
Road22=Road('Road22',870,560,40,115)

Roads=[Road1,Road2,Road3,Road4,Road5,Road6,Road7,Road8,Road9,Road10,Road11,Road12,Road13,Road14,Road15,Road16,Road17,Road18,Road19,Road20,Road21,Road22]

#Top Row
pave1 = objects(10.0,10.0,1070.0,35.0, "Light Grey",False,canvas)
object1 = objects(10.0,15.0,200.0, 25.0, "Red",False,canvas)
object2 = objects(290.0,15.0,200.0,25.0, "Red",False,canvas)
object3 = objects(580.0,15.0,200.0,25.0, "Red",False,canvas)
object4 = objects(870.0,15.0,210.0,25.0, "Red",False,canvas)

#second row
pave2 = objects(50.0,85.0,354.0,35.0, "Light Grey", False,canvas)
object5 = objects(55.0,90.0,344.0,25.0,"Red", False, canvas)
pave3 = objects(444.0,85.0,35.0,110.0,"Light Grey", False,canvas)
object6 = objects(449.0,90.0,25.0,100.0, "Red",False,canvas)
pave4 = objects(519.0,85.0,351.0,35.0,"Light Grey",False,canvas)
object7 = objects(524.0,90.0,341.0,25.0,"Red",False,canvas)
pave5 = objects(910.0,85.0,35.0,150.0,"Light Grey",False,canvas)
object8 = objects(915.0,90.0,25.0,140.0,"Red",False,canvas)
pave6 = objects(985.0,85.0,55.0,110.0,"Light Grey",False,canvas)
object9 = objects(990.0,90.0,45.0,100.0, "Red",False,canvas)

#Third Row
pave7 = objects(50.0,160.0,180.25,35.0,"Light Grey", False,canvas)
object10 = objects(55.0,165.0,170.0,25.0,"Red", False,canvas)
pave8 = objects(271.25,160,172.75,35.0, "Light Grey", False,canvas)
object11 = objects(276.25,165.0,162.75,25.0, "Red", False, canvas)
pave9 = objects(519.0,160.0,351.0,35.0,"Light Grey",False,canvas)
object12 = objects(524.0,165.0,341.0,25.0,"Red",False,canvas)

#Fourth Row
pave10 = objects(50.0,235.0,180.25,105.0, "Light Grey", False,canvas)
object13 = objects(55.0,240.0,170.25,95.0, "Red", False,canvas)
pave11 = objects(270.25, 235.0, 180.25,105.0, "Light Grey", False, canvas)
object14 = objects(275.0, 240.0,170.0,95.0, "Red", False, canvas)
pave12 = objects(490.25,235.0,549.75,105.0, "Light Grey", False, canvas)
object15 = objects(495.25,240.0,539.75,95.0, "Red", False, canvas)

#Fifth Row
pave21 = objects(50.0,380.0,180.25,105.0, "Light Grey", False,canvas)
object27 = objects(55.0,385.0,170.25,95.0, "Red", False,canvas)
pave22 = objects(270.25, 380.0, 180.25,105.0, "Light Grey", False, canvas)
object28 = objects(275.0, 385.0,170.0,95.0, "Red", False, canvas)
pave23 = objects(490.25,380.0,549.75,105.0, "Light Grey", False, canvas)
object29 = objects(495.25,385.0,539.75,95.0, "Red", False, canvas)

#Sixth Row
pave13 = objects(50.0,525.0,276.5,35.0, "Light Grey", False,canvas)
object16 = objects(55.0,530.0,266.5,25.0, "Red", False,canvas)
pave14 = objects(366.0,525.0,351.0,35.0, "Light Grey", False,canvas)
object17 = objects(371.0,530.0,341.0,25.0,"Red", False,canvas)
pave15 = objects(757.0,525.0,153.0,35.0, "Light Grey", False,canvas)
object18 = objects(762.0,530.0,143.0,25.0,"Red",False,canvas)
pave16 = objects(910.0,525.0,170.0,150.0, "Light Grey", False,canvas)
object19 = objects(915.0,530.0,160.0,140.0, "Red", True, canvas)

#Seventh Row
pave17 = objects(50.0,600.0,180.25,35.0,"Light Grey", False,canvas)
object20 = objects(55.0,605.0,170.0,25.0, "Red", False, canvas)
pave18 = objects(271.25,600.0,207.75,35.0, "Light Grey", False,canvas)
object21 = objects(276.25,605.0,197.75,25.0, "Red", False, canvas)
pave19 = objects(519.0,600.0,351.0,35.0,"Light Grey", False,canvas)
object22 = objects(524,605,341.0,25.0, "Red", False,canvas)

#Eighth Row
pave20 = objects(10.0,675.0,1070.0,35.0, "Light Grey",False,canvas)
object23 = objects(10.0,680.0,200.0, 25.0, "Red",False,canvas)
object24 = objects(290.0,680.0,200.0,25.0, "Red",False,canvas)
object25 = objects(580.0,680.0,200.0,25.0, "Red",False,canvas)
object26 = objects(870.0,680.0,210.0,25.0, "Red",False,canvas)

ListOfLandmarks = (object4, object13,object19,object20)
'''r2d2 = Robot(0, 0, speed = 1, colour='yellow')
c3po = Robot(0, 0, speed = 1, size=20, colour='cyan')
r2d2.RandomPosition()
c3po.RandomPosition()
r2d2.drawRobot() 
c3po.drawRobot()
c3po.Move()'''
'''Light1 = lights(20.0,130.0,40,150,"Green")
Light2 = lights(20.0,205.0,40,225,"Green")'''

route1 = {Road1:[Road2, Road9, Road7, Road4, Road3], Road2:[Road1,Road10,Road5,Road13,Road14,Road16, Road19], Road3: [Road1,Road5,Road13,Road14], Road4:[Road1,Road5], Road5:[Road3, Road4], Road6:[Road2,Road11,Road8,Road15,Road7], Road7:[Road6,Road12,Road1], Road8:[Road1,Road12,Road6], Road9:[Road1,Road10], Road10:[Road9,Road2,Road11], Road11:[Road10,Road6,Road13, Road14], Road12:[Road8,Road7], Road13:[Road2,Road11,Road15,Road3], Road14:[Road2,Road17,Road15,Road18, Road3], Road15:[Road6,Road13,Road14], Road16:[Road2,Road20,Road17,Road21,Road8,Road22], Road17:[Road14,Road16], Road18:[Road14,Road16], Road19:[Road19,Road20,Road21,Road22], Road20:[Road16,Road19], Road21: [Road16,Road19], Road22: [Road16,Road19]}
print DFS(route1, Road21, Road1)



main.mainloop()
