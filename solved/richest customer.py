accounts = [[1,5],[7,3],[3,5]]
richestCusty = 0

for account in accounts:
    currentCusty = sum(account)
    if currentCusty > richestCusty:
        richestCusty = currentCusty

print(richestCusty)