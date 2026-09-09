height = input("Enter your height (in inches) for permission to access the rides: ")
if (int(height) >= 48 and int(height) < 54):
    print("You are allowed to ride the Vortex, Lumber Jack, and the Flying Canoes. ")
if (int(height) > 54): 
    print("You are allowed on all of the rides")
elif (int(height) >= 40) and (int(height) < 48):
    print("You are allowed to ride the Tree Top Adventure, Taxi Jam, and the Sugar Shack.")
if (int(height) < 40):
    print("We're sorry, but you are not allowed on any of the rides")
if (int(height) >= 96):
    print("You are either trolling or way to tall for your own good.")
if (int(height) < 35 ): 
    print("Why are you appyling a toddler for this park?")