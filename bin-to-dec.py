def main():
    print("Menu:\n1: Binary to Decimal\n2: Decimal to Binary\n3: END")
    choice = eval(input("My Choice: "))

    if choice == 1:
        print("\nYou have chosen Binary to Decimal!")
        x = str(input('Binary value: '))
        count = len(x)
        if(count > 5):
            print("binary value should not exceed 5 digits!")
            return None
        else:
            result = int(x,2)
            print('Binary {} is equal to {} in decimal'.format(x,result))
    elif choice == 2:
        print("\nYou have chosen Decimal to Binary!")
        y = int(input('Enter value: '))
        if y<= 500:
            dec = bin(y)[2:]
            print('Decimal {} is equal to {} in binary'.format(y,dec))
        else:
            print('Should not exceed 500!')
            return None
    elif choice == 3:
        print("\nEND!")
        return None
    else:
        print("Invalid Input!")
        return None
        
    
