from tkinter import *
from random import *


root = Tk()
root.title("Jeu de la vie")



canvas = Canvas(root, width=800, height=500, bg="light yellow", highlightthickness=2, highlightbackground="black", bd=0)
canvas.grid(padx=25, pady=25)

class Cellule :
    global NbColumn, NbRow

    listeCellules = []

    
    def __init__(self, coA, coB, row, column):
        Cellule.listeCellules.append(self)

        self.id = Cellule.listeCellules.index(self)

        self.row = row
        self.column = column

        self.coA = coA
        self.coB = coB

        self.etat = 0
        self.futur = 0

        self.compteur_longevite = 0

        self.rec = canvas.create_rectangle(coA, coB, coA+10, coB+10, fill='black', outline="") # outline=""

        canvas.tag_bind(self.rec, "<Button-1>", self.clic)

        # canvas.tag_bind(self.rec, "<B1_Motion>", self.clic)
        # <B1-Motion>

    def get_id (self):
        return self.id 
    
    def get_etat (self):
        return self.etat

    def get_row (self):
        return self.row
    
    def get_column (self):
        return self.column
    
    def get_future (self):
        return self.futur
    
    def get_compteur_L (self):
        return self.compteur_longevite

    def set_compteur_L (self, nb):
        if nb == 1:
            self.compteur_longevite += 1
        elif nb == 0 :
            self.compteur_longevite = 0

    def set_future (self, future):
        self.futur = future

    def set_etat (self, etat):  
        self.etat = etat

    def vivre (self):
        self.set_etat(1)

        canvas.itemconfig(self.rec, fill=self.maCouleur(self.get_compteur_L())) 


    def mourir (self):
        self.set_etat(0)
        self.set_compteur_L(0)


        canvas.itemconfig(self.rec, fill='black') 

    def voisines (self):

        myId = self.get_id()
        myRow = self.get_row()
        myColumn = self.get_column()
        

        idVoisines = [NbColumn-1, NbColumn, NbColumn+1, -1, 1, (-NbColumn)-1, (-NbColumn), (-NbColumn)+1]

        if myColumn == NbColumn-1 : 
            del idVoisines[7]
            del idVoisines[4]
            del idVoisines[2]
        
        if myColumn == 0 :
            del idVoisines[5]
            del idVoisines[3]
            del idVoisines[0]

        listeVoisinesID = []

        for i in (idVoisines):
            if 0 <= myId + i < len(Cellule.listeCellules):

                listeVoisinesID.append(myId+i)


        NbVoisineV = 0

        for j in (listeVoisinesID):
                cel = Cellule.listeCellules[j]
                if cel.get_etat() == 1:
                   NbVoisineV += 1
        
        return NbVoisineV


    def clic (self, event):
        
        if self.etat == 0:
            self.vivre()
        else:
            self.mourir()
        
    def evolution (self):

        myEtat = self.get_etat()
        myVoisinesV = self.voisines()
        
        if myEtat == 0:
            if myVoisinesV == 3:
                self.set_future(1)
                self.compteur_longevite = 0
                
            else:
                self.set_future(0)
                           
        else:
            if myVoisinesV < 2 or self.voisines() > 3:
                self.set_future(0)
                
            else:
                self.set_future(1)
                self.compteur_longevite += 1
                
        
    def maCouleur (self, nb):
        listeCouleur = ["green", "yellow", "orange", "red"]
        if nb <= 2:
            couleur = listeCouleur[nb]
        else:
            couleur = listeCouleur[3]
        
        return couleur

    def go (self):
        myEtat = self.get_etat()
        myFutur = self. get_future()

        if myEtat == 1:
            canvas.itemconfig(self.rec, fill=self.maCouleur(self.get_compteur_L())) 

        if myEtat != myFutur :
            if myFutur == 1:
                self.vivre()
                
            else:
                self.mourir()
                
NbRow = 50
NbColumn = 80

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

frame = Frame(root) # bg='light green'
frame.grid(sticky=EW, padx=10, pady=10)

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)      
frame.columnconfigure(3, weight=1)
frame.columnconfigure(4, weight=1)

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