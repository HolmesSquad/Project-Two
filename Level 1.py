from Tkinter import *
main = Tk(className = "Level 1")
canvas = Canvas(main, width = 1280, height = 720, bg = "Black")
canvas.pack()
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
        print "Start"

    def pause(main):
        programispaused=True
        main.negcounter()

    def reset(main):
        global counter, resetpressed, RoboFinished
        counter=-1
        resetpressed=True

    def nextLevel(self):
        print "Next Level"

    def count(main):
        global counter, resetpressed, pausepressed
        counter==counter
        global RoboFinished
        RoboFinished==RoboFinished
       
        if (RoboFinished !=True):
            counter=counter+1
            main.timerShow_label.config(text = str(counter))
            main.timerShow_label.after(1000, main.count) 
        elif resetpressed==True:
            print resetpressed
            counter=0
            resetpressed=False
        elif pausepressed==True:
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
        global programispaused
        programispaused=True
        if programispaused==True:
            global counter
            counter=counter-1
            main.timerShow_label.after(1000, main.negcounter) 

interface = interface(main)
interface=interface.counter_label(interface)
    

Map = objects(10.0, 10.0, 1070.0, 700.0,"Dark Grey", False, canvas)
Robot1 = objects(20.0,55.0,20.0,20.0,"Cyan",False,canvas)
#Top Row
pave1 = objects(10.0,10.0,1070.0,35.0, "Light Grey",False,canvas)
object1 = objects(10.0,15.0,200.0, 25.0, "Red",False,canvas)
object2 = objects(290.0,15.0,200.0,25.0, "Red",False,canvas)
object3 = objects(580.0,15.0,200.0,25.0, "Red",False,canvas)
object4 = objects(870.0,15.0,210.0,25.0, "Red",True,canvas)

#second row
pave2 = objects(50.0,85.0,354.0,35.0, "Light Grey", False,canvas)
object5 = objects(55.0,90.0,344.0,25.0,"Red", False, canvas)
pave3 = objects(444.0,85.0,35.0,110.0,"Light Grey", False,canvas)
object6 = objects(449.0,90.0,25.0,100.0, "Red",False,canvas)
pave4 = objects(519.0,85.0,351.0,35.0,"Light Grey",False,canvas)
object7 = objects(524.0,90.0,341.0,25.0,"Red",False,canvas)
pave5 = objects(910.0,85.0,35.0,150.0,"Light Grey",False,canvas)
object8 = objects(915.0,90.0,25.0,140.0,"Red",False,canvas)
pave6 = objects(985.0,85.0,35.0,110.0,"Light Grey",False,canvas)
object9 = objects(990.0,90.0,25.0,100.0, "Red",False,canvas)

#Third Row
pave7 = objects(50.0,160.0,180.25,35.0,"Light Grey", False,canvas)
object10 = objects(55.0,165.0,170.0,25.0,"Red", False,canvas)
pave8 = objects(271.25,160,172.75,35.0, "Light Grey", False,canvas)
object11 = objects(276.25,165.0,162.75,25.0, "Red", False, canvas)
pave9 = objects(519.0,160.0,351.0,35.0,"Light Grey",False,canvas)
object11 = objects(524.0,165.0,341.0,25.0,"Red",False,canvas)

#Fourth Row
pave10 = objects(50.0,235.0,180.25,250.0, "Light Grey", False,canvas)
object12 = objects(55.0,240.0,170.25,240.0, "Red", False,canvas)



#Fifth Row
pave13 = objects(50.0,525.0,276.5,35.0, "Light Grey", False,canvas)
object16 = objects(55.0,530.0,266.5,25.0, "Red", False,canvas)
pave14 = objects(366.0,525.0,351.0,35.0, "Light Grey", False,canvas)
object17 = objects(371.0,530.0,341.0,25.0,"Red", False,canvas)
pave15 = objects(757.0,525.0,153.0,35.0, "Light Grey", False,canvas)
object18 = objects(762.0,530.0,143.0,25.0,"Red",False,canvas)
pave16 = objects(910.0,525.0,170.0,150.0, "Light Grey", False,canvas)
object19 = objects(915.0,530.0,160.0,140.0, "Red", True, canvas)

#Sixth Row
pave17 = objects(50.0,600.0,180.25,35.0,"Light Grey", False,canvas)
object20 = objects(55.0,605.0,170.0,25.0, "Red", True, canvas)
pave18 = objects(271.25,600.0,207.75,35.0, "Light Grey", False,canvas)
object21 = objects(276.25,605.0,197.75,25.0, "Red", False, canvas)
pave19 = objects(519.0,600.0,351.0,35.0,"Light Grey", False,canvas)
object22 = objects(524,605,341.0,25.0, "Red", False,canvas)

#Seventh Row
pave20 = objects(10.0,675.0,1070.0,35.0, "Light Grey",False,canvas)
object23 = objects(10.0,680.0,200.0, 25.0, "Red",False,canvas)
object24 = objects(290.0,680.0,200.0,25.0, "Red",False,canvas)
object25 = objects(580.0,680.0,200.0,25.0, "Red",False,canvas)
object26 = objects(870.0,680.0,210.0,25.0, "Red",True,canvas)





main.mainloop()

