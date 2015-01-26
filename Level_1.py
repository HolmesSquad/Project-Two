from Tkinter import *
import webbrowser
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

    def __init__(self,x,y,length,width,colour,canvas):
        global ObjectList
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.colour = colour
        self.canvas=canvas
        self.object = canvas.create_rectangle(self.x,self.y,self.x+self.length,self.y+self.width,fill = self.colour)

class landmarks(objects):
   
    def TreasurePicker(self):
        num=random.choice(LandMarkList)
        Treasure = canvas.create_rectangle(num.x,num.y,num.x+num.length,num.y+num.width,fill = "Yellow")      

class interface:

    def __init__(self, name):
        self.start_button = Button(name, text="Start", width = 20, command=self.start, bg = "Green")
        self.start_button.place(x = 1110, y = 150)

        self.pause_button = Button(name, text = "Pause/Unpause", width = 20, command = self.pause, bg = "Light Blue")
        self.pause_button.place(x = 1110, y = 200)

        self.reset_button = Button(name, text="Reset", width = 20, command=self.reset, bg = "Orange")
        self.reset_button.place(x = 1110, y = 250)

        self.level2_button = Button(name, text="Level 2", width = 20, command=self.level2, bg = "Yellow")
        self.level2_button.place(x = 1110, y = 300)

        self.level3_button = Button(name, text="Level 3", width = 20, command=self.level3, bg = "Yellow")
        self.level3_button.place(x = 1110, y = 350)

        self.timerShow_label = Label(name, text = "", width = 7, font = ("Arial", 16))
        self.timerShow_label.place(x = 1170, y = 30)

        self.timer_label= Label(name,text ="Timer", width = 5, font = ("Arial", 16))
        self.timer_label.place(x = 1110, y = 30)

        self.treasures_label = Label(name, text = "Treasure Remaining: ", width = 16, height = 2, font = ("Arial", 12), anchor = N)
        self.treasures_label.place(x = 1110, y = 70)

        self.treasureShow_label = Label(name, text = "1", width = 16, font = ("Arial", 12))
        self.treasureShow_label.place(x = 1110, y = 100)

        self.robot1Score_label = Label(name, text = "Robot Score: ", width = 16, height = 1, font = ("Arial", 12), anchor = N)
        self.robot1Score_label.place(x = 1110, y = 400)

        self.robot1Score_label = Label(name, text = "0", width = 16, font = ("Arial", 12))
        self.robot1Score_label.place(x = 1110, y = 420)

        self.info_label1=Label(name, text="", width=16, font = ("Arial", 12))
        
    def start(self):
        global resetpressed, RoboFinished
        
        interface.start_button.place_forget()
        interface.counter_label(interface)

    def pause(main):
        global paused, programispaused, pausebuffer
        if paused:
            programispaused = False
        else:
            pausebuffer = 1
            main.pause_button.place_forget()
            programispaused = True
            main.negcounter()
            
        paused = not paused            

    def reset(main):
        global counter, resetpressed, RoboFinished
        counter = 0
        main.timerShow_label.config(text = str(counter))
        resetpressed = True
        interface.start_button.place(x = 1110, y = 150)
        RoboFinished = True

    def level2(self):
        main.destroy()
        import Level_2
        
    def level3(self):
        main.destroy()
        import Level_3
             
        
    def count(main):
        global counter, resetpressed, pausepressed, colourChanger
        counter==counter
        global RoboFinished
        RoboFinished==RoboFinished
        if (RoboFinished != True):
            counter=counter+1
            if colourChanger!=4:
                colourChanger=colourChanger+1
                print ("colourChanger",colourChanger)
            else:
                colourChanger=0
            main.timerShow_label.config(text = str(counter))
            flipColour()
            main.timerShow_label.after(1000, main.count) 
        else:
            main.counter_stop()

    def counter_label(main,self):
        
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

    def counter_stop(main,self):
        main.info_label.config(text="The Robot has found the last treasure")
        self.info_label1.place(x = 1110, y = 670)


class lights(interface):

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

class Road:
    def __init__(self,name,x,y,width,height,colour="darkgrey"):
        self.name=name
        self.x1=x
        self.y1=y
        self.x2=x+width
        self.y2=y+height
        self.width=width
        self.height=height
        self.object=canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill=colour, width=0)

class Robot:
    def __init__(self,x,y,speed=1.0,size=20,colour='blue'):
        self.x1=x
        self.y1=y
        self.x2=x+size
        
        self.y2=y+size
        self.colour=colour
        self.speed=speed
        self.size=size
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
                return road
    def Move(self):
        city = {Road1:[Road2, Road9, Road7, Road4, Road3], Road2:[Road1,Road10,Road5,Road13,Road14,Road16, Road19], Road3: [Road1,Road5,Road13,Road14], Road4:[Road1,Road5], Road5:[Road3, Road4], Road6:[Road2,Road11,Road8,Road15,Road7], Road7:[Road6,Road12,Road1], Road8:[Road1,Road12,Road6], Road9:[Road1,Road10], Road10:[Road9,Road2,Road11], Road11:[Road10,Road6,Road13, Road14], Road12:[Road8,Road7], Road13:[Road2,Road11,Road15,Road3], Road14:[Road2,Road17,Road15,Road18, Road3,Road11], Road15:[Road6,Road13,Road14], Road16:[Road2,Road20,Road17,Road21,Road8,Road22], Road17:[Road14,Road16], Road18:[Road14,Road16], Road19:[Road19,Road20,Road21,Road22], Road20:[Road16,Road19], Road21: [Road16,Road19], Road22: [Road16,Road19]}
        Route=list(DFS(city, self.CheckPosition(), Road12))
        Route.append(Road12)
        IteminRoute=0
        print len(Route)
        while IteminRoute<len(Route):
            NextRoad=Route[IteminRoute]
            print Route[IteminRoute]
            if NextRoad.height>NextRoad.width:
                #print "Test 4"
                x_destination=NextRoad.x1+NextRoad.width/2
                print "X Destination:"+str(x_destination)
                if x_destination>(self.x1+(self.size/2)):
                    
                    #print "Test 3"
                    for t in range(0,int((x_destination-(self.x1+(self.size/2))/self.speed))):
                        self.x1+=self.speed
                        self.x2+=self.speed
                        self.canvas.coords(self.shape,self.x1,self.y1,self.x2,self.y2)
                        self.canvas.update()
                        
                        time.sleep(0.01)
                else: # x_destination<(self.x1+(self.size/2))
                    for t in range(0,int(((self.x1+(self.size/2)-x_destination)/self.speed))):
                        # print "Test 2"
                        self.x1-=self.speed
                        self.x2-=self.speed
                        self.canvas.coords(self.shape,self.x1,self.y1,self.x2,self.y2)
                        self.canvas.update()
                        
                        time.sleep(0.01)
            else:
                #print "Test 5"
                y_destination=NextRoad.y1+(NextRoad.height/2)
                print "Y Destination:"+str(y_destination)
                if y_destination>(self.y1+(self.size/2)):
                   # print "Test 7"
                    for t in range(0,int((y_destination-(self.y1+(self.size/2))/self.speed))):
                        self.y1+=self.speed
                        self.y2+=self.speed
                        self.canvas.coords(self.shape,self.x1,self.y1,self.x2,self.y2)
                        self.canvas.update()
                        
                        time.sleep(0.01)
                else: #if y_destination<(self.x1+(self.size/2))
                    for t in range(0,int(((self.y1+(self.size/2)-y_destination)/self.speed))):
                        #print "Test 8"
                        self.y1-=self.speed
                        self.y2-=self.speed
                        self.canvas.coords(self.shape,self.x1,self.y1,self.x2,self.y2)
                        self.canvas.update()
                        
                        time.sleep(0.01)
            IteminRoute+=1

interface = interface(main)

Map = objects(10.0, 10.0, 1070.0, 700.0,"Dark Grey", canvas)

#Roads
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

#Objects & Landmarks
#Top Row
pave1 = objects(10.0,10.0,1070.0,35.0, "Light Grey",canvas)
object1 = objects(10.0,15.0,200.0, 25.0, "Red",canvas)
object2 = objects(290.0,15.0,200.0,25.0, "Red",canvas)
object3 = objects(580.0,15.0,200.0,25.0, "Red",canvas)
object4 = landmarks(870.0,15.0,210.0,25.0, "Blue",canvas)

#second row
pave2 = objects(50.0,85.0,354.0,35.0, "Light Grey",canvas)
object5 = objects(55.0,90.0,344.0,25.0,"Red", canvas)
pave3 = objects(444.0,85.0,35.0,110.0,"Light Grey",canvas)
object6 = objects(449.0,90.0,25.0,100.0, "Red",canvas)
pave4 = objects(519.0,85.0,351.0,35.0,"Light Grey",canvas)
object7 = objects(524.0,90.0,341.0,25.0,"Red",canvas)
pave5 = objects(910.0,85.0,35.0,150.0,"Light Grey",canvas)
object8 = objects(915.0,90.0,25.0,140.0,"Red",canvas)
pave6 = objects(985.0,85.0,35.0,110.0,"Light Grey",canvas)
object9 = objects(990.0,90.0,25.0,100.0, "Red",canvas)

#Third Row
pave7 = objects(50.0,160.0,180.25,35.0,"Light Grey", canvas)
object10 = objects(55.0,165.0,170.0,25.0,"Red", canvas)
pave8 = objects(271.25,160,172.75,35.0, "Light Grey", canvas)
object11 = objects(276.25,165.0,162.75,25.0, "Red",  canvas)
pave9 = objects(519.0,160.0,351.0,35.0,"Light Grey",canvas)
object12 = objects(524.0,165.0,341.0,25.0,"Red",canvas)

#Fourth Row
pave10 = objects(50.0,235.0,180.25,105.0, "Light Grey", canvas)
object13 = landmarks(55.0,240.0,170.25,95.0, "Blue", canvas)
pave11 = objects(270.25, 235.0, 199.25,105.0, "Light Grey",canvas)
object14 = objects(275.0, 240.0,189.0,95.0, "Red",canvas)
pave12 = objects(524.25,235.0,510.75,105.0, "Light Grey",canvas)
object15 = objects(529.25,240.0,500.75,95.0, "Red",canvas)

#Fifth Row
pave21 = objects(50.0,380.0,180.25,105.0, "Light Grey",canvas)
object27 = objects(55.0,385.0,170.25,95.0, "Red", canvas)
pave22 = objects(270.25, 380.0, 199.25,105.0, "Light Grey",canvas)
object28 = objects(275.0, 385.0,189.0,95.0, "Red",canvas)
pave23 = objects(524.25,380.0,510.75,105.0, "Light Grey",canvas)
object29 = landmarks(529.0,385.0,500.75,95.0, "Blue",canvas)

#Sixth Row
pave13 = objects(50.0,525.0,276.5,35.0, "Light Grey",canvas)
object16 = objects(55.0,530.0,266.5,25.0, "Red",canvas)
pave14 = objects(366.0,525.0,351.0,35.0, "Light Grey",canvas)
object17 = objects(371.0,530.0,341.0,25.0,"Red",canvas)
pave15 = objects(757.0,525.0,153.0,35.0, "Light Grey", canvas)
object18 = objects(762.0,530.0,143.0,25.0,"Red",canvas)
pave16 = objects(910.0,525.0,170.0,150.0, "Light Grey",canvas)
object19 = landmarks(915.0,530.0,160.0,140.0, "Blue",canvas)

#Seventh Row
pave17 = objects(50.0,600.0,180.25,35.0,"Light Grey",canvas)
object20 = objects(55.0,605.0,170.0,25.0, "Red",canvas)
pave18 = objects(271.25,600.0,207.75,35.0, "Light Grey",canvas)
object21 = objects(276.25,605.0,197.75,25.0, "Red",canvas)
pave19 = objects(519.0,600.0,351.0,35.0,"Light Grey",canvas)
object22 = objects(524,605,341.0,25.0, "Red",canvas)

#Eighth Row
pave20 = objects(10.0,675.0,1070.0,35.0, "Light Grey",canvas)
object23 = objects(10.0,680.0,200.0, 25.0, "Red",canvas)
object24 = objects(290.0,680.0,200.0,25.0, "Red",canvas)
object25 = objects(580.0,680.0,200.0,25.0, "Red",canvas)
object26 = objects(870.0,680.0,210.0,25.0, "Red",canvas)

#Lights
#Column 1
Light1 = lights(20.0,130.0,40,150,"Green") #Used in group 1
Light2 = lights(20.0,205.0,40,225,"Green") #Used in group 2
Light3 = lights(20.0, 350.0, 40, 370.0, "Green")#Used in group 3
Light4 = lights(20.0, 495, 40, 515, "Green")
Light5 = lights(20.0, 570, 40, 590, "Green")

#Column 2
Light6 = lights(240, 130, 260, 150, "Green")
Light7 = lights(240, 205, 260, 225, "Green")
Light8 = lights(240, 350, 260, 370, "Green")#Used in group 1
Light9 = lights(240, 495, 260, 515, "Green")#Used in group 2
Light10 = lights(240, 570, 260, 590, "Green")#Used in group 3
Light11 = lights(240, 645, 260, 665, "Green")

#Column 3
Light12 = lights(415, 55, 435, 75, "Green")
Light13 = lights(335, 495, 355, 515, "Green")#Used in group 1
Light14 = lights(335, 570, 355, 590, "Green")#Used in group 2

#Column 4
Light15 = lights(490, 55, 510, 75, "Green")#Used in group 3
Light16 = lights(490, 130, 510, 150, "Green")
Light17 = lights(490, 210, 510, 230, "Green")
Light18 = lights(490, 350, 510, 370, "Green")
Light19 = lights(490, 495, 510, 515, "Green")
Light20 = lights(490, 570, 510, 590, "Green")
Light21 = lights(490, 645, 510, 665, "Green")

#Column 5
Light22 = lights(725, 495, 745, 515, "Green")
Light23 = lights(725, 570, 745, 590, "Green")

#Column 6
Light24 = lights(880, 55, 900, 75, "Green")
Light25 = lights(880, 130, 900, 150, "Green")

#Column 7
Light26 = lights(955, 55, 975, 75, "Green")#Used in group 1

#Column 8
Light27 = lights(1040, 205, 1060, 225, "Green")#Used in group 2
Light28 = lights(1040, 350, 1060, 370, "Green")#Used in group 3

#changing colour

def flipColour():
    
    

    #group 1
    if colourChanger==1 or colourChanger==2:
        c3po.speed=0.1
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
        Light22.change_colour("Red")
        Light23.change_colour("Red")
        Light24.change_colour("Red")
        Light25.change_colour("Red")
        Light26.change_colour("Red")
        Light27.change_colour("Red")
        Light28.change_colour("Red")
        canvas.update()
    if colourChanger==3 or colourChanger==4:
        c3po.speed=1
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
        Light22.change_colour("Green")
        Light23.change_colour("Green")
        Light24.change_colour("Green")
        Light25.change_colour("Green")
        Light26.change_colour("Green")
        Light27.change_colour("Green")
        Light28.change_colour("Green")

#Robot
c3po = Robot(0, 0, speed = 1, size=20, colour='yellow')
c3po.RandomPosition()
c3po.drawRobot()
c3po.Move()



main.mainloop()
