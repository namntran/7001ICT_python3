# Concert theatre has seating for 100 guests
# Box office to sell only 100 tickets

#intitialise
seats = 100 
while seats > 0:
    tickets = int(input("Seats remaining: " + str(seats) + ". How many in your group? ")) # number of tickets sold (input wants a string)
    if tickets <= seats:
        print("Booked, thank you")
    while tickets > seats:
        print("Sorry, not enough seats left")
        tickets = int(input("Seats remaining: " + str(seats) + ". How many in your group? ")) # number of tickets sold (input wants a string)
    seats -= tickets # shorthand for seats = seats - tickets
print("SOLD OUT!")