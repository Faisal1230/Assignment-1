num_1 = int(input("Frist Number: "))
num_2 = int(input("Second Number: "))
print("Here are the conditions start")
ch = input("enter the value (+,-,/,*:)")


if ch == '+':
    print(num_1 + num_2)
elif ch == '-':
    print(num_1 - num_2)
elif ch =='*':
    print(num_1*num_2)    
elif ch =='/':
    print(num_1/num_2)
else:
    print("All clear between us")   

print("Ending")     


