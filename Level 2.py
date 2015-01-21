from Tkinter import *
import random
main = Tk(className = "Level 2")
canvas = Canvas(main, width = 1280, height = 720, bg = "Black")
canvas.pack()
class objects:

    def __init__(self,x,y,length,width,colour,canvas):
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.colour = colour
        self.canvas=canvas
        self.object = canvas.create_rectangle(self.x,self.y,self.x+self.length,self.y+self.width,fill = self.colour)
        
class Landmarks(objects):
    def __init__(self,x,y,length,width,colour,canvas,Id,treasure):
        objects.__init__(self,x,y,length,width,colour,canvas)
        self.Id=Id
        self.treasure=treasure

class Treasure(objects):
    
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

        self.nextLevel_button = Button(name, text="Next Level", width = 20, command=self.nextLevel, bg = "Yellow")
        self.nextLevel_button.place(x = 1110, y = 300)

        self.timerShow_label = Label(name, text = "", width = 7, font = ("Arial", 16))
        self.timerShow_label.place(x = 1170, y = 30)

        self.timer_label= Label(name,text ="Timer", width = 5, font = ("Arial", 16))
        self.timer_label.place(x = 1110, y = 30)

        self.treasures_label = Label(name, text = "Treasure Remaining: ", width = 16, height = 2, font = ("Arial", 12), anchor = N)
        self.treasures_label.place(x = 1110, y = 70)

        self.treasureShow_label = Label(name, text = "1", width = 16, font = ("Arial", 12))
        self.treasureShow_label.place(x = 1110, y = 100)

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

    def nextLevel(self):
        print "Next Level"

    def count(main):
        global counter, resetpressed, pausepressed
        counter==counter
        global RoboFinished
        RoboFinished==RoboFinished
        if (RoboFinished != True):
            counter=counter+1
            main.timerShow_label.config(text = str(counter))
            main.timerShow_label.after(1000, main.count) 
        elif resetpressed == True:
            print resetpressed
            counter=0
            resetpressed= False
        elif pausepressed== True:
            print "Wololol 2"
        else:
            print "help"
            main.cstop()

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
Landmark1 = Landmarks(55.0,67.0,10.0,20.0,"blue",canvas,"Dave",False)
Landmark2 = Landmarks(200.0,583.0,10.0,20.0,"blue",canvas,"Jason",True)
Landmark3 = Landmarks(383.0,508.0,10.0,20.0,"blue",canvas,"Kim",False)
Landmark4 = Landmarks(860.25,363.0,10.0,20.0,"blue",canvas,"Matt",True)
Landmark5 = Landmarks(990.0,67.0,10.0,20.0,"blue",canvas,"Pete",False)
Landmark6 = Landmarks(519.0,143.0,10.0,20.0,"blue",canvas,"Rose",True)
Landmark7 = Landmarks(590.25,363.0,10.0,20.0,"blue",canvas,"Mark",False)
Landmark8 = Landmarks(90.0,143.0,10.0,20.0,"blue",canvas,"Roshel",True)
Landmark9 = Landmarks(366.0,583.0,10.0,20.0,"blue",canvas,"Lucy",False)
Landmark10 = Landmarks(800,583.0,10.0,20.0,"blue",canvas,"Ben",True)

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
main.mainloop()
