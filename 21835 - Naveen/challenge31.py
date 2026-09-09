input = input("Type something for all vowels to be removed: ")
vowels = "aeiouAEIOU"
result = ""
i = 0

while i < len(input):
    if input[i] not in vowels: 
        result += input[i]
    i += 1

print(result)