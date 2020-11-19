import tkinter as tk
from winsound import Beep

# This will is the window with instructions and the possebility to change 
# the training time
class SetTime():
    def __init__(self):
        
       # Lets you insert the Time 
        def retrieve():
            global Set
            Set = float(E1.get())*60                       
            top.destroy()

        top = tk.Tk() #opens the window (parend widget ) named "top"
        
        # first Label with a 100pixels spred from the Top
        L1 = tk.Label(top, text="Training Time in Min: ", font="Times 30")
        L1.pack(pady = 50)
        
        #Input Field with predefined value of 7.5 (min)
        E1 = tk.Entry(top, bd=10, font="Times 30")
        E1.insert(0, "7.5")
        E1.pack()

        # Button with Pads left and Right to get it centered
        Button = tk.Button(top, text = "Let's Go", command = retrieve, font="Times 40", bg="#66a3ff")
        Button.pack(padx = 5, pady = 5)
        
        # Label That explains the Trainingsmethod
        Explain = tk.Label(top, text="Welcome to the Step-Intervall-Timer!\n\nHow to use:\n\nDo one repetition (rep) of an exercise - Rest.\nDo two reps - Rest.\nAdd always one more rep.\nOnce you reach muscle failure do one less.\nIf you don't reach one rep don't worry.\nThe rest-periode is as long as reps.\n\nHave Fun!", font = "Times 10")
        Explain.pack(pady = 50)
        
        # loops the windowe untill its closed
        top.mainloop()

# This is the main Timer
class App():
      
    def __init__(self):
        
        # The function for the Pause-Button
        # sets 3 variables one depending on the timer direction
        def Pause():
            global stop
            global work
            global seconds
            
            if Prepare == -1: # # Renders the Button Functionless while in Preparetime
                if stop == False and seconds > 0: # Renders it functionless while in Resttime
                    seconds -=2 # sets it to the right time
                    stop = True
                    work = "Rest"
        
        self.root = tk.Tk() #opens the window   
        
        # Closes the timer
        QuitButton = tk.Button(self.root, text ="Quit", command=self.root.destroy)
        QuitButton.pack()
        
        # Shows the Training Periode
        self.Task = tk.Label(text=work, font = "Times=80", bg = "dark orange", fg ="white")
        self.Task.pack(fill = "x", pady=10)
        
        self.label = tk.Label(text="", font ="Times 200", fg ="dark orange")
        self.label.pack(pady=5)
        
        self.Settime = tk.Label(text="{}:{}".format(int(Set/60), int(Set%60)), font = "Times 30", fg = "red")
        self.Settime.pack()
        
        PauseButton = tk.Button(self.root, text="Pause", command = Pause, font = "Times 100", bg= "#66a3ff" )
        PauseButton.pack(side= "bottom", fill = "both")
      
        self.update_clock()
        self.root.mainloop()
        

    def CountUP (self):
        global seconds
        global stop
        global work
        global Set
        global Prepare
    
        # run down a little Time to get ready
        if Prepare > -1:
            Prepare -= 1
            seconds = Prepare
            work = "Prepare"
            if Prepare == -1:
                work = "Work"
                seconds = 1
                Set -=1
                Beep(250,200)
                
        # This is the actual timer. It starts when the Preparetime is expired        
        elif Set > 0 and Prepare < 0:
            if stop == False:
                work = "Work"
                seconds += 1
                Set -= 1
                self.label.configure(fg ="dark blue")
                self.Task.configure(bg ="dark blue")

            elif stop == True:
                work = "Rest"
                seconds  -= 1
                Set -= 1
                self.label.configure(fg ="green")
                self.Task.configure(bg ="green")
            
            # Repeated Buttonpresses ofter Restpiriod will be catched by these 2 if-statements
            if seconds == -1:
                stop = False
                Beep(250,200)
                seconds = 1
                work = "Work"
                
            elif seconds == -2:
                seconds = 1
                stop = False
        
        # will give a fiinal message after the Time run out
        else:
            self.Task.configure(text="You are", font = "Times 60", bg ="dark orange")
            self.label.configure(text="Awesome", font = "Times 60")
            self.Settime.configure(text="Good Job!", font = "Times 60")
    
    # Updates the 3 Labels and calls itself after 1000 ms as well as the Timerfunction
    def update_clock(self):
        self.label.configure(text=seconds, font = "Times 200")
        self.Task.configure(text=work, font = "Times 40")
        self.Settime.configure(text="{}:{}".format(str(int(Set/60)).zfill(2), str(int(Set%60)).zfill(2)))#zfill gives the numbers the 00:00 format
        self.root.after(1000, self.update_clock)
        self.root.after(1000, self.CountUP)


# This window will ask the User if he wants to go again and if not closes the Whole App for good
class End():
    def __init__(self):
        
        # this closes the window and let begin another round
        def Yes():
            global Round
            Round = True
            Again.destroy()
        
        # closes the window and well as the App
        def callback():
            global Round
            Round = False
            Again.destroy()
        
        def ImperialMarch():
            Beep(440, 500) 
            Beep(440, 500) 
            Beep(440, 500) 
            Beep(349, 350) 
            Beep(523, 150) 
            Beep(440, 500) 
            Beep(349, 350) 
            Beep(523, 150) 
            Beep(440, 1000) 
            Beep(659, 500) 
            Beep(659, 500) 
            Beep(659, 500) 
            Beep(698, 350) 
            Beep(523, 150) 
            Beep(415, 500) 
            Beep(349, 350) 
            Beep(523, 150) 
            Beep(440, 1000)


        Again = tk.Tk()
        tk.Button(Again, text="Imperial", command = ImperialMarch,font = "Times 12", bg="black", fg= "white").pack(fill=tk.X)
        tk.Label(Again,text="Again?", font = "Times 100").pack(pady=100)
        tk.Button(Again, text='Yes!', command=Yes, font = "Times 60", bg= "light blue").pack(fill=tk.X)
        tk.Button(Again, text='Quit', command=callback,font = "Times 60", bg="orange").pack(fill=tk.X)
        
        
        Again.mainloop()


    
        
# This is the sequence in wich the 3 Windows are called        
        
Round = True        
        
while Round == True:
    
    stop = False
    seconds = 5
    work = "Prepare"
    Prepare = 5

    Duration = SetTime()
    # Counter 
    app=App()

    app = End()# will set Round to False if Presssd the Quid butting, ending the Loop