# program to calculate wages plus bonus for a salesperson in a week

hours = int(input("How many hours were worked? "))
sales = float(input("Total sales for the week? "))
rate = float(30.25)
commission = (sales-3000)*.03
wages = rate*hours
totalWages = (rate*hours) + commission
extraHours = hours-37
overTime = extraHours*rate*1.5

if hours < 37:
    print("Pay =", totalWages)
elif hours > 37:
    print("Pay =", 37*rate+overTime)
elif sales > 3000:
    print("Pay =", totalWages)