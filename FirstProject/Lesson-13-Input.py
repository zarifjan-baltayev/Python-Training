
# name = input('Hello please enter your name')
# print('Wellcome ' + name)

# print("This is rectangle area calculato!")
#
# high = input('Pleace enter HIGH : \n\t\t')
# widh = input('Please enter widh : \n\t\t')
#
# print('The area of the rectangle is : \n\t\t' +
#       str(int(high) * int(widh)) + ' squares of ...')



# msg = ""
# while True:
#     msg = input("Please enter password : ")
#     if msg == "zarif":
#         print("Password is Correct!")
#         break
#     print("Wrong password! \n")


names = []
rule = ''


def input(param):
    pass


while rule != 'stop':
    rule = input("Enter NEW NAME or STOP the program! \n\t --:")
    names.append(rule)

print("Entered name are! \n")
for i in names:
    print(i)