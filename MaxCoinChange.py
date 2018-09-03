# Same as CoinChangeAll except that we have an index to keep track of

def coin_change(coins, amount, coin_path, result, index):
    if amount == 0:
        result.append(coin_path)
    for i in range(index, len(coins)):
        coin=coins[i]
        if amount - coin >= 0:
            coin=coins[i]
            coin_change(coins, amount - coin, coin_path+[coin], result, i)

result=[]
coin_path=[]
coin_change([1,2,4], 4, coin_path, result, 0)
print result

'''
Result:
[[1, 1, 1, 1], [1, 1, 2], [2, 2], [4]]
'''
