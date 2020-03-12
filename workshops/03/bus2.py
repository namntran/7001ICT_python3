# calculate number of buses for rugby tournament
teams = float(input("How many teams? "))
rugbyTeam = float(15)
bigBus = float(38)

buscapacity = teams*rugbyTeam/bigBus
#if bus capacity not equal to whole number
# ceil function and no if statement
if buscapacity != int:
    print(int(buscapacity+1))
else:
    print(int(buscapacity))
