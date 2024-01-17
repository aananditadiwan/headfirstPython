temp = 'Marvin, the paraniod android'
letters = list(temp)
for ch in letters[:6]:
    print('\t',ch)
print()
for ch in letters[-7:]:
    print('\t'*2,ch)
print()
for ch in letters[12:20]:
    print('\t'*3,ch)
print()