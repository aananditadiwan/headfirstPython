word = 'bottles'
for beer_num in range(5,0,-1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer...")
    print("take one down")
    print("pass it around")
    if beer_num == 1:
        print("No more ", word , " left")
    else :
        new_num = beer_num - 1
        if new_num == 1 :
            word = "bottle"
        print()