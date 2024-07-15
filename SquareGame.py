#spike caccatus

from tkinter import *
import keyboard
import SaveMiniGame
import random
import time


GRID_SIZE = 11
CELL_SIZE = 50 

SaveMiniGame.Moves = random.randrange(15, 25)

rowplayer = SaveMiniGame.PlayerR
columnplayer = SaveMiniGame.PlayerC
Level = SaveMiniGame.Level
moves = SaveMiniGame.Moves
playerColor = "blue"

TargetR1 = SaveMiniGame.TargetR1
TargetC1 = SaveMiniGame.TargetC1

DestinationC = SaveMiniGame.DestinationC
DestinationR = SaveMiniGame.DestinationR

pickup = False
canpickup = False

def save():
    f = open("Square-Game/SaveMiniGame", "w")

    f.write("Moves = " + str(moves) + "\n")
    f.write("DestinationR =" + str(DestinationR) + "\n")
    f.write("DestinationC =" + str(DestinationC) + "\n")
    f.write("Level = " + str(Level) + "\n")
    f.write("PlayerR = " + str(rowplayer) + "\n")
    f.write("PlayerC = " + str(columnplayer) + "\n")
    f.write("TargetC1 = " + str(TargetC1) + "\n")
    f.write("TargetR1 = " + str(TargetR1) + "\n")

    f.close()
    

def loop():
    global rowplayer
    global columnplayer
    global moves
    global DestinationC
    global DestinationR
    global TargetC1
    global TargetR1
    global Level

    if keyboard.is_pressed('s') or keyboard.is_pressed('down'):
        if rowplayer < 10:
            rowplayer += 1
        else:
            rowplayer = 0
        moves -= 1
    if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
        if rowplayer > 0:
            rowplayer -= 1
        else:
            rowplayer = 10
        moves -= 1
    if keyboard.is_pressed('a') or keyboard.is_pressed('left'):
        if columnplayer > 0:
            columnplayer -= 1
        else:
            columnplayer = 10
        moves -= 1
    if keyboard.is_pressed('d') or keyboard.is_pressed('right'):
        if columnplayer < 10:
            columnplayer += 1
        else:
            columnplayer = 0
        moves -= 1
    if moves <= 0:
        Level = 1
        moves = random.randrange(15, 25)
        DestinationR = random.randrange(10)
        DestinationC = random.randrange(10)
        TargetC1 = random.randrange(10)
        TargetR1 = random.randrange(10)
        save()

    LevelLab.config(text = "Level: " + str(Level) + " " + str(moves))

    update_grid()

    x = True

    if x:
        x = False
    else:
        x = True
    save()

    root.after(100, loop)

def update_grid():
    global playerColor
    global TargetC1
    global TargetR1
    global pickup
    global canpickup
    global DestinationC
    global DestinationR
    global Level
    global moves

    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if rowplayer != TargetR1 or columnplayer != TargetC1:
                canpickup = False
                if r == TargetR1 and c == TargetC1 and not playerColor == "white":
                    cells[r][c].configure(bg = "red", font = ("Roboto", 10), text = "")
                elif r == rowplayer and c == columnplayer:
                        cells[r][c].configure(bg=playerColor)
                elif r == DestinationR and c == DestinationC:
                    cells[r][c].configure(bg = "green")
                else:
                    cells[r][c].configure(bg="black", text = "")
            elif r == DestinationR and c == DestinationC:
                cells[r][c].configure(bg = "green")
            else:
                cells[r][c].configure(bg="black", text = "")
            if r == rowplayer == TargetR1 and c == columnplayer == TargetC1:
                cells[r][c].configure(bg = "white", font = ("Roboto", 10))
                save()
                canpickup = True
            if r == DestinationR == rowplayer and c == DestinationC == columnplayer:
                cells[r][c].configure(bg = playerColor)
            if DestinationC == TargetC1 and DestinationR == TargetR1:
                DestinationR = random.randrange(10)
                DestinationC = random.randrange(10)
                TargetC1 = random.randrange(10)
                TargetR1 = random.randrange(10)
                Level += 1
                moves = random.randrange(15, 25)
                LevelLab.config(text = "Level: " + str(Level) + " " + str(moves))
                save()
            if keyboard.is_pressed('e'):
                if pickup == False:
                    if canpickup == True:    
                        playerColor = "white"
                        pickup = True
                        save()
                        PickUpLab.config(text = "Item picked up: YES", fg = "green")
                        time.sleep(0.5)
                else:
                    TargetC1 = columnplayer
                    TargetR1 = rowplayer
                    playerColor = "blue"
                    pickup = False
                    PickUpLab.config(text = "Item picked up: NO", fg = "red")
                    save()
                    time.sleep(0.5)

root = Tk(className = " Square Game")
root.geometry = (f'{GRID_SIZE * CELL_SIZE}x{GRID_SIZE * CELL_SIZE}')
root.configure(background = 'black')

cells = []

for r in range(GRID_SIZE):
    row = []
    for c in range(GRID_SIZE):
        cell = Label(root, width = 4, height = 2, relief = "solid", bg = "black")
        cell.grid(row=r, column=c)
        row.append(cell)
    cells.append(row)

LevelLab = Label(root, text = "Level: " + str(Level) + " " + str(moves), font = ("Roboto", 25), fg = "white", bg = "black")
LevelLab.grid(row = 12, column = 0 ,columnspan = 200)

PickUpLab = Label(root, text = "Item picked up: NO", fg = "red", font = ("Roboto", 15), bg = "black")
PickUpLab.grid(row = 13, column = 0, columnspan = 200)

InfoLab = Label(root, text = "INFO:" + "\n" + "wasd or arrows for movement" + "\n" + "e to pick up" + "\n" + "pick up the red square and put it into" + "\n" + "the green square (you are the blue square)", fg = "white", font = ("Roboto", 15), bg = "black")
InfoLab.grid(row = 14, column = 0, columnspan = 200)
        
root.after(100, loop)

root.mainloop()
