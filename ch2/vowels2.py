word = input("Please provide a word : ")
vowels = ['a','e','i','o','u']
found = []
for ch in word :
    if ch in vowels :
        if ch not in found:
            found.append(ch)
for vowl in found:
    print(vowl)