try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter Value: "))
    
    percentage = value/total_value * 100
    print(f"That is {percentage}%")

except ValueError:
    print("You need to enter a number. Run the program again.")

except ZeroDivisionError:
    print("your total value cannot be zero.")