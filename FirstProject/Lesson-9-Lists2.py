cars = ['Bmw', 'volksWagen', 'Seat', 'Skoda', 'Mercedes', 'Ferrari']
for x in cars:
    print(x.upper())

for x in range(0, 6):
    print(x)
myNumberList = list(range(0, 10+1))
print(myNumberList)
print("=====================================================")
for x in myNumberList:
    x = x*2
    print(x)

myNumberList.sort(reverse=True)
print(myNumberList)
print("The maximum number of list: \n\t"+str(max(myNumberList)))
print(min(myNumberList))
print(sum(myNumberList))
print("The avarage of the list: \n\t" + str(sum(myNumberList)/len(myNumberList)))

mycars = cars[1:4]
mycars = cars[:4]
mycars = cars[4:]
mycars = cars[:-1]
mycars = cars[-4:-1]
mycars = cars[:]

print(mycars)