
print("Menu:\n1: Binary to Decimal\n2: Decimal to Binary\n3: End")
choice = eval(input("Enter your choice: "))

if choice==1:
    print("\nYou've chosen bin to dec")
    val = str   (input("Binary value: "))
    bin = int(val,2)
    print('bin: ',val, ' to dec: ',bin)
elif choice==2:
    val = int(input("Decimal value: "))
    dec = int(bin(val)[2:])
    print ('dec: ',val, ' to bin: ',dec)               
elif choice==3:
        print("\n---E-N-D---")


    
    


            
        
            
        
