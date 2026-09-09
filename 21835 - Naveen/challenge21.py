message = input("What is your message?: ")
stripMessage = message.strip()
print(len(stripMessage))
emergency = stripMessage.find("911") 