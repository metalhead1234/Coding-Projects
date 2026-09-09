allegedFairyTale = input("Is your story a fairy tale?: ")
trueFairyTale = allegedFairyTale.startswith("Once upon a time") and allegedFairyTale.endswith("THE END")
print(trueFairyTale) 