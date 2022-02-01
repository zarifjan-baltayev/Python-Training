

for n in range(0, 100, +1):
    print("NUMBER X = " + str(n))
    if n == 6:
        print("bu hatije")
    if n == 42:
        print("bu zarif ")
        break

print("-----------------------------This is END OF FORLOOP------------------------------")

x = 0
while True:
    print(x)
    x = x+1
    if x == 5:
        break
print(str(x) + "is found by computer")
