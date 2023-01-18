heightList = []

noOfCustomers = int(input("Enter number of customers : "))

for i in range(0, noOfCustomers):
    h = float(input())
    heightList.append(h*2.54)
    
print(heightList)