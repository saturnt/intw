def coin_change(coins, amount, coin_path, result):
    if amount == 0:
        result.append(coin_path)
    for coin in coins:
        if amount - coin >= 0:
            coin_change(coins, amount - coin, coin_path+[coin], result)

result=[]
coin_path=[]
coin_change([1,2,4], 4, coin_path, result)
print result

'''
Result:
[[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2], [4]]
'''
