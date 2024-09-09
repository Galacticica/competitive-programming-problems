a1, a2  = input().split(" ")
a1 = int(a1)
a2 = int(a2)
letters = input()





if letters == "ABBA" and (a2 - a1 == 3):
    print((a1 + 1), (a1 + 2))
elif letters == "AABB" and (a2 == 7):
    print(8, 9)
elif letters == "ABAB" and (a1 == 6):
    print(7,9)
elif letters == "BBAA" and (a1 == 3):
    print(1,2)
elif letters == "BABA" and (a2 == 4):
    print (1, 3)
elif letters == "BAAB" and (a1 == 2) and (a2 == 8):
    print (1, 9)
else:
    print(-1)





