pizzaSlicesTotal = int(input("How many (total) slices of Pizza?: "))
people = int(input("How many people?: "))
fraction = pizzaSlicesTotal // people
remainder = pizzaSlicesTotal - (fraction * people)
print("Each person gets " + str(fraction) + " Pizza slices. There will be " + str(remainder)  + " Slices left." )        
