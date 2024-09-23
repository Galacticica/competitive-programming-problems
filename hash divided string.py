from itertools import islice

def split_into(iterable, sizes):
    it = iter(iterable)
    for size in sizes:
        if size is None:
            yield list(it)
            return
        else:
            yield list(islice(it, size))

s = input()
k = int(input())
n = len(s)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
index = []
substringNum = n // k
finalLetter = ""
for i in range (substringNum):
    index.append(k)
listOfChars = list(split_into([str(x) for x in str(s)], index))
for hash in listOfChars:
    sum = 0
    for letter in hash:
        i = alphabet.index(letter)
        sum = sum+i
    finalLetter = finalLetter + alphabet[(sum % 26)]
print (finalLetter)