coins = [500, 100, 50, 10]

chagne = 100000
total = 0
for i in range(len(coins)):
    coin = coins[i]
    if chagne // coin >= 1:
        total = total + chagne // coin
        chagne = chagne - coin * (chagne//coin)

print(total)