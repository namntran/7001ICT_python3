# list = [1,2,3,4,5]

# list_sum = 0
# for x in list:
#    list_sum += x
#    print(list_sum)

hours = int(input("How many hours were worked? "))
sales = float(input("Total sales for the week? "))
rate = float(30.25)
commission = (sales-3000)*.03
# total = 0
wages = rate*hours
totalWages = (rate*hours) + commission
extraHours = hours-37
overTime = extraHours*rate*1.5

if hours < 37:
    # total += hours
    print("Pay =", totalWages)
elif hours > 37:
    print("Pay =", 37*rate+overTime)
    # print(overTime)
elif sales > 3000:
    print("Pay =", totalWages)



# if hours > 37 and > 40:

# total += __

# else:
#     total += hours * rate

# if earned > 
# total += bana
# print(total)

# def calcWeeklyWages(totalHours, hourlyWage):
#     if totalHours <= 37:
#         totalWages = hourlyWage*totalHours
#     else:
#         overtime = totalHours - 37
#         totalWages = hourlyWage*37 + (1.5*hourlyWage)*overtime
#     return totalWages

# def calcSalesCommission(sales, bonus):
#     if sales > 3000:
#         bonus = (sales - 3000)*0.3
#     return bonus

# print(calcWeeklyWages(totalHours, hourlyWage))
# # print(calcSalesCommission())

