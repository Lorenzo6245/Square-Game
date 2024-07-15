ATTENTION!!!
This program run only on visual studio code and not on Github codespace because it use a library called keyboard (you can install it by digiting on your prompt: pip install keyboard)

if the save system don't work as well insert the file eplorer location of the SaveMiniGame.py file

example:

def save():
    
    f = open("INSERT HERE THE LOCATION OF SAVEMINIGAME.PY", "w")

    f.write("Moves = " + str(moves) + "\n")
    f.write("DestinationR =" + str(DestinationR) + "\n")
    f.write("DestinationC =" + str(DestinationC) + "\n")
    f.write("Level = " + str(Level) + "\n")
    f.write("PlayerR = " + str(rowplayer) + "\n")
    f.write("PlayerC = " + str(columnplayer) + "\n")
    f.write("TargetC1 = " + str(TargetC1) + "\n")
    f.write("TargetR1 = " + str(TargetR1) + "\n")

    f.close()
