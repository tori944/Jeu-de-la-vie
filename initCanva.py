from tkinter import *

NbRow = 50
NbColumn = 80

root = Tk()
root.title("Jeu de la vie")

canvas = Canvas(root, width=800, height=500, bg="light yellow", highlightthickness=2, highlightbackground="black", bd=0)
canvas.grid(padx=25, pady=25)
