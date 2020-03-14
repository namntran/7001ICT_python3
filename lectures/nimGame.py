# Two person Nim game

# Rules: start with 20 matches
# Person who takes the last match loses
# Each takes 1-3 matches per turn

#intitialise
matches = 20 
player = 1

while matches > 0:
    print("There are", matches, "left")
    pickup = int(input("Player " + str(player) + " how many matches to pick up: ")) #number of matches taken in one turn
    while pickup > matches or pickup > 3 or pickup < 1:
        print("Time wasting dufus ... 1 ....3 please")
        pickup = int(input("Player " + str(player) + " how many matches to pick up: ")) #input wants a string
    matches -= pickup # shorthand for matches = matches - pickup
# switch player
    if player == 1:
        player = 2
    else:
        player = 1
print("Player", player, "wins!")