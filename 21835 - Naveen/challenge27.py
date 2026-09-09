destinations = ["Thailand", "Brazil", "Japan", "Singapore", "England"]      
print("\n=== Travel Destination Wish List ===")
print("1. Add a travel destination")
print("2. Find a travel destination")
print("3. Remove a travel destination")
print("4. Sort destinations by alphabet")
print("5. Count destinations")
print(destinations)

choice = int(input("Choose an option: "))

if (choice == 1):
    newDestination = input("What destination would you like to add? ")
    destinations.append(newDestination)
    print(destinations)
    print("\n=== Travel Destination Wish List ===")
    print("1. Add a travel destination")
    print("2. Find a travel destination")
    print("3. Remove a travel destination")
    print("4. Sort destinations by alphabet")
    print("5. Count destinations")
    choice = int(input("Choose an option: "))

if (choice == 2):
    findDestination = input("What destination are you looking for? ")
    if findDestination in destinations: 
        print("This destination is included.")
        print("\n=== Travel Destination Wish List ===")
        print("1. Add a travel destination")
        print("2. Find a travel destination")
        print("3. Remove a travel destination")
        print("4. Sort destinations by alphabet")
        print("5. Count destinations")  
        choice = int(input("Choose an option: "))
    else:
     print("This destination is not included. Press 1 to add it.")
     print("\n=== Travel Destination Wish List ===")
     print("1. Add a travel destination")
     print("2. Find a travel destination")
     print("3. Remove a travel destination")
     print("4. Sort destinations by alphabet")
     print("5. Count destinations")  
     choice = int(input("Choose an option: "))


if (choice == 3 ): 
   removed = input("Which destination would you like to remove?")
   if (removed in destinations): 
      destinations.remove(removed)
      print(destinations)
      print("\n=== Travel Destination Wish List ===")
      print("1. Add a travel destination")
      print("2. Find a travel destination")
      print("3. Remove a travel destination")
      print("4. Sort destinations by alphabet")
      print("5. Count destinations")  
      choice = int(input("Choose an option: "))

   else:  
      print("This item is not included in the list.")
      print(destinations)
      print("\n=== Travel Destination Wish List ===")
      print("1. Add a travel destination")
      print("2. Find a travel destination")
      print("3. Remove a travel destination")
      print("4. Sort destinations by alphabet")
      print("5. Count destinations")  
      choice = int(input("Choose an option: "))


if (choice == 4):
   destinations.sort()
   print(destinations)
   print("\n=== Travel Destination Wish List ===")
   print("1. Add a travel destination")
   print("2. Find a travel destination")
   print("3. Remove a travel destination")
   print("4. Sort destinations by alphabet")
   print("5. Count destinations")  
   choice = int(input("Choose an option: "))

if (choice == 5): 
   destinationCount = len(destinations)
   print("There are " + str(destinationCount) + " destinations included.")
   print(destinations)
   print("\n=== Travel Destination Wish List ===")
   print("1. Add a travel destination")
   print("2. Find a travel destination")
   print("3. Remove a travel destination")
   print("4. Sort destinations by alphabet")
   print("5. Count destinations")  
   choice = int(input("Choose an option: "))