from initCanva import *
from random import *

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
        # myRow = self.get_row()
        myColumn = self.get_column()
        

        idVoisines = [NbColumn-1, NbColumn, NbColumn+1, -1, 1, (-NbColumn)-1, (-NbColumn), (-NbColumn)+1]

        if myColumn == NbColumn-1 :  # bord droit
            del idVoisines[7]
            del idVoisines[4]
            del idVoisines[2]
        
        if myColumn == 0 :    # bord gauche
            del idVoisines[5]
            del idVoisines[3]
            del idVoisines[0]

        # for i in (idVoisines):
        #     if i < 0 or i >= len(Cellule.listeCellules):
        #         idVoisines.remove(i)


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