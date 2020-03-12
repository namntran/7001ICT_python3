#votes received
a = int(input("How many votes for Angus? "))
b = int(input("How many votes for Betty? "))
c = int(input("How many votes for Cathy? "))
total = a+b+c
# list of numbers 
list1 = [a, b, c]
list2 = ["Angus", "Betty", "Cathy"]
# sorting the list 
list1.sort() 
mostVotes = list2[-1]
secondVotes = list2[-2]
thirdVotes = list2[-3]
# 1. if a candidate has more than half the votes: print they win  
if a > total/2:
    print("Angus wins")
elif b > total/2:
    print("Betty wins")
elif c > total/2:
    print("Cathy wins")

# 2. find the biggest two candidates
# if mostVotes > thirdVotes AND secondVotes > thirdVotes:
elif thirdVotes < secondVotes:
    print("Next round: ", mostVotes,"and", secondVotes)

# 3. if there is a tie: print everyone
elif a == b == c:
    print("Next round: Angus, Betty, and Cath")

