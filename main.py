from Cellule import *

for i in range (NbRow):
    for j in range (NbColumn):
        Cellule(j*10, i*10, i, j)


def GO ():
    global running

    if running == False:
        return

    for c in Cellule.listeCellules:
        c.evolution()
    
    for c in Cellule.listeCellules:
        c.go()

    vitesse = scaleVitesse.get()
    
    root.after(vitesse, GO)

def unTiers ():
    r = 0
    for cel in Cellule.listeCellules:
        r = choice([0, 1, 0])
        if r == 1:
            cel.vivre()
        else :
            cel.mourir()

def Start ():
    global running
    running = True
    GO()

def Stop ():
    global running
    running = False

def Clear ():
    for cel in Cellule.listeCellules:
        if cel.etat == 1:
            cel.mourir()

frame = Frame(root)
frame.grid(sticky=EW, padx=10, pady=10)

frame.columnconfigure([0,1,2,3,4], weight=1)

btnR = Button(frame, text="1/3",font=("",15), command=unTiers)
btnR.grid(column=0, row=0, pady=10)

btnStart = Button(frame, text="Start", font=("",15), cursor='star', command=Start)
btnStart.grid(column=1, row=0, pady=10)

btnStop = Button(frame, text="Stop", font=("",15), cursor='spider', command=Stop)
btnStop.grid(column=2, row=0, pady=10)

btnClear = Button(frame, text="clear", font=("",15), cursor="gumby", command=Clear)
btnClear.grid(column=3, row=0, pady=10)

frame2 = Frame(frame)
frame2.grid(column=4, row=0, pady=10)

scaleVitesse = Scale(frame2, from_=50, to=1000, orient=HORIZONTAL, resolution=50)
scaleVitesse.grid()
scaleVitesse.set(500)
labelV = Label(frame2, text="Vitesse", font=("",15))
labelV.grid()


root.mainloop()