from Tkinter import *
import random
main = Tk(className = "Level 2")
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
class objects: #class that defines the objects that populate the map

    def __init__(self,x,y,length,width,colour,canvas):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.colour = colour
        self.canvas=canvas
        self.object = canvas.create_rectangle(self.x,self.y,self.x+self.length,self.y+self.width,fill = self.colour)
        
class Landmarks(objects): #class that defines the Landmarks that may contain treasures - inherits from objects
    def __init__(self,x,y,length,width,colour,canvas,Id,treasure,visited):
        objects.__init__(self,x,y,length,width,colour,canvas)
        self.Id=Id
        self.treasure=treasure
        self.visited=visited

class Treasure(objects): #class that defines the Treasures that are hidden in selected landmarks - inherits from objects
    
    def __init__(self,x,y,length,width,colour,canvas,Found,points):
        objects.__init__(self,x,y,length,width,colour,canvas)
        
        self.Found = Found
        self.points = points

class interface:

    def __init__(self, name):
        self.start_button = Button(name, text="Start", width = 20, command=self.start, bg = "Green")
        self.start_button.place(x = 1110, y = 150)

        self.pause_button = Button(name, text = "Pause", width = 20, command = self.pause, bg = "Light Blue")
        self.pause_button.place(x = 1110, y = 200)

        self.reset_button = Button(name, text="Reset", width = 20, command=self.reset, bg = "Orange")
        self.reset_button.place(x = 1110, y = 250)

        self.level1_button = Button(name, text="Level 1", width = 20, command=self.level1, bg = "Yellow")
        self.level1_button.place(x = 1110, y = 300)

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

    def start(self):
        global resetpressed, RoboFinished
        print "Start"
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

    def level1(self):
        main.destroy()
        import Level_1

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
            if colourChanger!=12:
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


interface = interface(main)

Map = objects(10.0, 10.0, 1070.0, 700.0,"Dark Grey",canvas)
Robot1 = objects(20.0,55.0,20.0,20.0,"Cyan",canvas)

#Top Row
pave1 = objects(10.0,10.0,1070.0,35.0, "Light Grey",canvas)
object1 = objects(10.0,15.0,200.0, 25.0, "Red",canvas)
object2 = objects(290.0,15.0,200.0,25.0, "Red",canvas)
object3 = objects(580.0,15.0,200.0,25.0, "Red",canvas)
object4 = objects(870.0,15.0,210.0,25.0, "red",canvas)

#second row
pave2 = objects(50.0,85.0,354.0,35.0, "Light Grey",canvas)
object5 = objects(55.0,90.0,344.0,25.0,"Red",canvas)
pave3 = objects(444.0,85.0,35.0,110.0,"Light Grey",canvas)
object6 = objects(449.0,90.0,25.0,100.0, "Red",canvas)
pave4 = objects(519.0,85.0,351.0,35.0,"Light Grey",canvas)
object7 = objects(524.0,90.0,341.0,25.0,"Red",canvas)
pave5 = objects(910.0,85.0,35.0,150.0,"Light Grey",canvas)
object8 = objects(915.0,90.0,25.0,140.0,"Red",canvas)
pave6 = objects(985.0,85.0,35.0,110.0,"Light Grey",canvas)
object9 = objects(990.0,90.0,25.0,100.0, "Red",canvas)

#Third Row
pave7 = objects(50.0,160.0,394.25,35.0,"Light Grey",canvas)
object10 = objects(55.0,165.0,384.0,25.0,"Red",canvas)
pave9 = objects(519.0,160.0,351.0,35.0,"Light Grey",canvas)
object12 = objects(524.0,165.0,341.0,25.0,"Red",canvas)

#Fourth Row
pave10 = objects(50.0,235.0,180.25,105.0,"Light Grey", canvas)
object13 = objects(55.0,240.0,170.25,95.0, "Red", canvas)
pave12 = objects(270.25,235.0,765.75,105.0, "Light Grey", canvas)
object15 = objects(275.0,240.0,755.75,95.0, "Red", canvas)

#Fifth Row
pave21 = objects(50.0,380.0,180.25,105.0, "Light Grey",canvas)
object27 = objects(55.0,385.0,170.25,95.0, "Red",canvas)
pave22 = objects(270.25, 380.0, 180.25,105.0, "Light Grey",canvas)
object28 = objects(275.0, 385.0,170.0,95.0, "Red",canvas)
pave23 = objects(490.25,380.0,549.75,105.0, "Light Grey",canvas)
object29 = objects(495.25,385.0,539.75,95.0, "Red",canvas)

#Sixth Row
pave13 = objects(50.0,525.0,276.5,35.0, "Light Grey",canvas)
object16 = objects(55.0,530.0,266.5,25.0, "Red",canvas)
pave14 = objects(366.0,525.0,544.0,35.0, "Light Grey",canvas)
object17 = objects(371.0,530.0,534.0,25.0,"Red",canvas)
pave16 = objects(910.0,525.0,170.0,150.0, "Light Grey",canvas)
object19 = objects(915.0,530.0,160.0,140.0, "red",canvas)

#Seventh Row
pave17 = objects(50.0,600.0,180.25,35.0,"Light Grey",canvas)
object20 = objects(55.0,605.0,170.0,25.0, "red",canvas)
pave18 = objects(271.25,600.0,207.75,35.0, "Light Grey",canvas)
object21 = objects(276.25,605.0,197.75,25.0, "Red",canvas)
pave19 = objects(519.0,600.0,351.0,35.0,"Light Grey",canvas)
object22 = objects(524,605,341.0,25.0, "Red",canvas)

#Eighth Row
pave20 = objects(10.0,675.0,1070.0,35.0, "Light Grey",canvas)
object23 = objects(10.0,680.0,200.0, 25.0, "Red",canvas)
object24 = objects(290.0,680.0,200.0,25.0, "Red",canvas)
object25 = objects(580.0,680.0,500.0,25.0, "Red",canvas)

#Landmarks
Landmark1 = Landmarks(55.0,67.0,10.0,20.0,"blue",canvas,"Dave",False,False)
Landmark2 = Landmarks(200.0,583.0,10.0,20.0,"blue",canvas,"Jason",True,False)
Landmark3 = Landmarks(383.0,508.0,10.0,20.0,"blue",canvas,"Kim",False,False)
Landmark4 = Landmarks(860.25,363.0,10.0,20.0,"blue",canvas,"Matt",True,False)
Landmark5 = Landmarks(990.0,67.0,10.0,20.0,"blue",canvas,"Pete",False,False)
Landmark6 = Landmarks(519.0,143.0,10.0,20.0,"blue",canvas,"Rose",True,False)
Landmark7 = Landmarks(590.25,363.0,10.0,20.0,"blue",canvas,"Mark",False,False)
Landmark8 = Landmarks(90.0,143.0,10.0,20.0,"blue",canvas,"Roshel",True,False)
Landmark9 = Landmarks(366.0,583.0,10.0,20.0,"blue",canvas,"Lucy",False,False)
Landmark10 = Landmarks(800,583.0,10.0,20.0,"blue",canvas,"Ben",True,False)

#Treasures
Treasure1 = Treasure(200.0,578.0,10.0,5.0,"dark green",canvas,False,100)
Treasure2 = Treasure(860.25,358.0,10.0,5.0,"dark green",canvas,False,100)
Treasure3 = Treasure(519.0,138.0,10.0,5.0,"dark green",canvas,False,100)
Treasure4 = Treasure(90.0,138.0,10.0,5.0,"dark green", canvas, False,100)
Treasure5 = Treasure(800.0,578.0,10.0,5.0,"dark green",canvas,False,100)

#Lights
#Column 1
Light1 = lights(20, 130, 40, 150, "Green")
Light2 = lights(20, 205, 40, 225, "Green")
Light3 = lights(20, 350, 40, 370, "Green")
Light4 = lights(20, 495, 40, 515, "Green")
Light5 = lights(20.0, 570, 40, 590, "Green")

#Column 2
Light6 = lights(240, 130, 260, 150, "Green")
Light7 = lights(240, 205, 260, 225, "Green")
Light8 = lights(240, 350, 260, 370, "Green")
Light9 = lights(240, 495, 260, 515, "Green")
Light10 = lights(240, 570, 260, 590, "Green")
Light11 = lights(240, 645, 260, 665, "Green")

#Column 3
Light12 = lights(415, 55, 435, 75, "Green")
Light13 = lights(335, 495, 355, 515, "Green")
Light14 = lights(335, 570, 355, 590, "Green")

#Column 4
Light15 = lights(490, 55, 510, 75, "Green")
Light16 = lights(490, 130, 510, 150, "Green")
Light17 = lights(490, 210, 510, 230, "Green")
Light18 = lights(490, 350, 510, 370, "Green")
Light19 = lights(490, 495, 510, 515, "Green")
Light20 = lights(490, 570, 510, 590, "Green")
Light21 = lights(490, 645, 510, 665, "Green")

#Column 5
Light24 = lights(880, 55, 900, 75, "Green")
Light25 = lights(880, 130, 900, 150, "Green")

#Column 6
Light26 = lights(955, 55, 975, 75, "Green")

#Column 7
Light27 = lights(1040, 205, 1060, 225, "Green")
Light28 = lights(1040, 350, 1060, 370, "Green")


def flipColour(): #This function calls the lights to change colour at the correct interval. The lights have been grouped to easier make alterations.
    
    
    
        #group 1
    if colourChanger==1 or colourChanger==2 or colourChanger==3:
        robot_wait=False
        Light1.change_colour("Red")
        Light8.change_colour("Red")
        Light13.change_colour("Red")
        Light26.change_colour("Red")
        canvas.update()
    if colourChanger==4 or colourChanger==10 or colourChanger==11:
        Light1.change_colour("Yellow")
        Light8.change_colour("Yellow")
        Light13.change_colour("Yellow")
        Light26.change_colour("Yellow")
        canvas.update()
    if colourChanger==7 or colourChanger==8 or colourChanger==9  or colourChanger==6 or colourChanger==5:
        Light1.change_colour("Green")
        Light8.change_colour("Green")
        Light13.change_colour("Green")
        Light26.change_colour("Green")
        canvas.update()
            

      #group 2
    if colourChanger==1 or colourChanger==2 or colourChanger==3:
        robot_wait=True
        Light2.change_colour("Red")
        Light9.change_colour("Red")
        Light14.change_colour("Red")
        Light27.change_colour("Red")
        canvas.update()
    if colourChanger==4 or colourChanger==10 or colourChanger==11:
        robot_wait=False
        Light2.change_colour("Yellow")
        Light9.change_colour("Yellow")
        Light14.change_colour("Yellow")
        Light27.change_colour("Yellow")
        canvas.update()
    if colourChanger==7 or colourChanger==8 or colourChanger==9  or colourChanger==6 or colourChanger==5:
        Light2.change_colour("Green")
        Light9.change_colour("Green")
        Light14.change_colour("Green")
        Light27.change_colour("Green")
        canvas.update()

    
        #group 3
    if colourChanger==1 or colourChanger==2 or colourChanger==3:
        robot_wait=True
        Light3.change_colour("Red")
        Light10.change_colour("Red")
        Light15.change_colour("Red")
        Light28.change_colour("Red")
        canvas.update()
    if colourChanger==4 or colourChanger==10 or colourChanger==11:
        robot_wait=False
        Light3.change_colour("Yellow")
        Light10.change_colour("Yellow")
        Light15.change_colour("Yellow")
        Light28.change_colour("Yellow")
        canvas.update()
    if colourChanger==7 or colourChanger==8 or colourChanger==9  or colourChanger==6 or colourChanger==5:
        Light3.change_colour("Green")
        Light10.change_colour("Green")
        Light15.change_colour("Green")
        Light28.change_colour("Green")
        canvas.update()

    
        #group 4
    if colourChanger==1 or colourChanger==2 or colourChanger==3:
        robot_wait=True
        Light4.change_colour("Red")
        Light11.change_colour("Red")
        Light16.change_colour("Red")
        Light25.change_colour("Red")
        canvas.update()
    if colourChanger==4 or colourChanger==10 or colourChanger==11:
        robot_wait=False
        Light4.change_colour("Yellow")
        Light11.change_colour("Yellow")
        Light16.change_colour("Yellow")
        Light25.change_colour("Yellow")
        canvas.update()
    if colourChanger==7 or colourChanger==8 or colourChanger==9  or colourChanger==6 or colourChanger==5:
        robot_wait=False
        Light4.change_colour("Green")
        Light11.change_colour("Green")
        Light16.change_colour("Green")
        Light25.change_colour("Green")
        canvas.update()

        #group 5
    if colourChanger==1 or colourChanger==2 or colourChanger==3:
        robot_wait=True
        Light5.change_colour("Red")
        Light12.change_colour("Red")
        Light17.change_colour("Red")
        Light24.change_colour("Red")
        canvas.update()
    if colourChanger==4 or colourChanger==10 or colourChanger==11:
        robot_wait=False
        Light5.change_colour("Yellow")
        Light12.change_colour("Yellow")
        Light17.change_colour("Yellow")
        Light24.change_colour("Yellow")
        canvas.update()
    if colourChanger==7 or colourChanger==8 or colourChanger==9  or colourChanger==6 or colourChanger==5:
        robot_wait=False
        Light5.change_colour("Green")
        Light12.change_colour("Green")
        Light17.change_colour("Green")
        Light24.change_colour("Green")
        canvas.update()

        #group 6
    if colourChanger==1 or colourChanger==2 or colourChanger==3:
        robot_wait=True
        Light6.change_colour("Red")
        Light18.change_colour("Red")
        Light20.change_colour("Red")
        canvas.update()
    if colourChanger==4 or colourChanger==10 or colourChanger==11:
        robot_wait=False
        Light6.change_colour("Yellow")
        Light18.change_colour("Yellow")
        Light20.change_colour("Yellow")
        canvas.update()
    if colourChanger==7 or colourChanger==8 or colourChanger==9  or colourChanger==6 or colourChanger==5:
        robot_wait=False
        Light6.change_colour("Green")
        Light18.change_colour("Green")
        Light20.change_colour("Green")
        canvas.update()
            
        #group 7
    if colourChanger==1 or colourChanger==2 or colourChanger==3:
        robot_wait=True
        Light7.change_colour("Red")
        Light19.change_colour("Red")
        Light21.change_colour("Red")
        canvas.update()
    if colourChanger==4 or colourChanger==10 or colourChanger==11:
        robot_wait=False
        Light7.change_colour("Yellow")
        Light19.change_colour("Yellow")
        Light21.change_colour("Yellow")
        canvas.update()
    if colourChanger==7 or colourChanger==8 or colourChanger==9  or colourChanger==6 or colourChanger==5:
        robot_wait=False
        Light7.change_colour("Green")
        Light19.change_colour("Green")
        Light21.change_colour("Green")
        canvas.update()

main.mainloop()
