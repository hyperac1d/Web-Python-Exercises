x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))

print("Operator Choice: \n1: Add\n2: Sub\n3: Mul\n4: Div with float\n5: Mod\n6: Div_floor\n7: exponen")
choice = int(input("\nYour choice: "))
if choice == 1:
    sum = x + y
    print('\nSum is ',sum)
elif choice == 2:
    sub = x-y
    print('\nDifference is ',sub)
elif choice == 3:
    mul = x*y
    print('\nProduct is ',mul)
elif choice == 4:
    div = x/y
    print('\nQuotient is ',div)
elif choice == 5:
    mod = x%y
    print('\Remainder is ',mod)
elif choice == 6:
    quot = x//y
    print('\nQuotient is ', quot)
elif choice == 7:
    expo = x ** y
    print('\nResult of', x,'to the power of', y, 'is ',expo)
else:
    print("\nINVALID INPUT!")



    
