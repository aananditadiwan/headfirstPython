vowels = ['a','e','i','o','u']
word= input("Enter a word : ")
found={}
for i in 
for letter in word :
    if letter in vowels:
        if letter not in found :
            found.append(letter)
print(found)