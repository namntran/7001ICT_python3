# calculate number of buses for rugby tournament
bigbus = float(input("How many big buses? "))
smallbus = float(input("How many small buses? "))
bigseats = float(38)
smallseats = float(10)
rugbyteam = float(15)

print("Number of teams, ", (bigbus*bigseats+smallbus*smallseats)//rugbyteam)