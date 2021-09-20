import tkinter as tk
import csv
import module1 as m1
import module2 as m2
import module3 as m3

def executeCommands():
    if mod1a.get() == 1 or mod1b.get() == 1 or mod1c.get() == 1 or mod1d.get() == 1:
        runModule1()
    if mod2a.get() == 1 or mod2b.get() == 1 or mod2c.get() == 1 or mod2d.get() == 1 or mod2e.get() == 1:
        runModule2()
    if mod3a.get() == 1:
        runModule3()

def runModule1():
    data = list(csv.reader(open("players.csv")))

    if mod1a.get() == 1:
        m1.playerProgression(data)
    if mod1b.get() == 1:
        m1.freshmanNums(data)
    if mod1c.get() == 1:
        m1.qbAwareness(data)
    if mod1d.get() == 1:
        m1.realisticInjuries(data)

    with open("newPlayers.csv","w") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',',lineterminator='\n')
        csvWriter.writerows(data)

def runModule2():
    data = list(csv.reader(open("recruits.csv")))

    if mod2a.get() == 1:
        m2.fixDuplicates(data)
    if mod2b.get() == 1:
        m2.generateHyphens(data)
    if mod2c.get() == 1:
        m2.generateSuffixes(data)
    if mod2d.get() == 1:
        m2.awarenessBoost(data)
    if mod2e.get() == 1:
        m2.freshmanInj(data)

    with open("newRecruits.csv","w") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',',lineterminator='\n')
        csvWriter.writerows(data)

def runModule3():
    data = list(csv.reader(open("newPlayers.csv")))

    if mod3a.get() == 1:
        m3.betterPlayersLeaving(data)

    with open("newPlayersLeaving.csv","w") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',',lineterminator='\n')
        csvWriter.writerows(data)








#################################################################################################

HEIGHT = 800
WIDTH = 1200
COL0 = 40
COL1 = 450
COL2 = 860



root = tk.Tk() #creates the root window

root.resizable(False,False)
root.title("NCAA 14 Dynamic Dynasty Tool")

#variables used by checkboxes
#mod1a= tk.IntVar()
mod1b= tk.IntVar()
mod1c= tk.IntVar()
mod1d= tk.IntVar()
mod2a= tk.IntVar()
mod2b= tk.IntVar()
mod2c= tk.IntVar()
mod2d= tk.IntVar()
mod2e= tk.IntVar()
mod3a= tk.IntVar()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='gray')
frame.place(relwidth=1, relheight=1)

#main title
titleLb = tk.Label(frame, text="Hammer's Dynamic Dynasty Tool", bg='gray')
titleLb.config(font=("Arial", 30))
titleLb.place(x=COL0, y=40)

#MODULE 1 - PROGRESSION/REGRESSION
moduleTitle1 = tk.Label(frame, text="Progression Module", bg='gray')
moduleTitle1.config(font=("Arial", 22))
moduleTitle1.place(x=COL0, y=100)

moduleExp1 = tk.Label(frame, text="(Run during preseason phase)", bg='gray')
moduleExp1.config(font=("Arial", 18))
moduleExp1.place(x=370, y=100)

#CHECKBUTTONS FOR WHICH SCRIPTS TO RUN

#attribute progression/regression
prog = tk.Checkbutton(frame, text="Attribute Progression/Regression", bg='gray', variable=mod1a)
prog.config(font=("Arial", 15))
prog.place(x=COL0, y=150)

#better jersey nums
jerNum = tk.Checkbutton(frame, text="Choose better jersey numbers for freshmen", bg='gray', variable=mod1b)
jerNum.config(font=("Arial", 15))
jerNum.place(x=COL1, y=150)

#big team awareness boost
awrBoost = tk.Checkbutton(frame, text="QB awareness boost for big schools", bg='gray', variable=mod1c)
awrBoost.config(font=("Arial", 15))
awrBoost.place(x=COL0, y=200)


##################################################################################################################


#MODULE 2 - RECRUITS
moduleTitle2 = tk.Label(frame, text="Recruits Module", bg='gray')
moduleTitle2.config(font=("Arial", 22))
moduleTitle2.place(x=COL0, y=300)

moduleExp2 = tk.Label(frame, text="(Run during preseason phase)", bg='gray')
moduleExp2.config(font=("Arial", 18))
moduleExp2.place(x=370, y=300)

#CHECKBUTTONS FOR WHICH SCRIPTS TO RUN

#duplicate names
dup = tk.Checkbutton(frame, text="Fix duplicate names", bg='gray', variable=mod2a)
dup.config(font=("Arial", 15))
dup.place(x=COL1, y=350)

#hyphenated names
hyph = tk.Checkbutton(frame, text="Generate hyphenated last names", bg='gray', variable=mod2b)
hyph.config(font=("Arial", 15))
hyph.place(x=COL0, y=350)

#suffixed names
suff = tk.Checkbutton(frame, text="Generate names with suffixes", bg='gray', variable=mod2c)
suff.config(font=("Arial", 15))
suff.place(x=COL0, y=400)

#increase awareness for top recruits
recAwr = tk.Checkbutton(frame, text="Increase awareness for top recruits", bg='gray', variable=mod2d)
recAwr.config(font=("Arial", 15))
recAwr.place(x=COL1, y=400)

'''
#recruit injury rating adjustment
recInj = tk.Checkbutton(frame, text="Normalize recruit injury ratings", bg='gray', var=mod2e)
recInj.config(font=("Arial", 15))
recInj.place(x=COL2, y=350)
'''


##################################################################################################################


#MODULE 3 - PLAYERS LEAVING
moduleTitle3 = tk.Label(frame, text="Players Leaving Module", bg='gray')
moduleTitle3.config(font=("Arial", 22))
moduleTitle3.place(x=COL0, y=500)

moduleExp3 = tk.Label(frame, text="(Run during players leaving phase)", bg='gray')
moduleExp3.config(font=("Arial", 18))
moduleExp3.place(x=370, y=500)

#CHECKBUTTONS FOR WHICH SCRIPTS TO RUN

#underclassmen leaving
ucLeav = tk.Checkbutton(frame, text="More underclassmen declare for the draft", bg='gray', variable=mod3a)
ucLeav.config(font=("Arial", 15))
ucLeav.place(x=COL0, y=550)




gen = tk.Button(frame, text="Run Modules", command=executeCommands)
gen.config(font=("Arial", 30))
gen.place(x=COL0, y=650)

root.mainloop() #place all code above this line, this opens the actual GUI
