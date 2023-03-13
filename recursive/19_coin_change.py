def rec_coin(target, coins):
    min_coins = target

    if target in coins:
        return 1
    else:
        # for every coins value there is <= my target
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin(target - i, coins)
            if num_coins < min_coins:
                min_coins = num_coins
    return min_coins


# def rec_coin_dynam(target, coins, known_results):
#     # default output to target
#     min_coins = target

#     # Base case
#     if target in coins:
#         known_results[target] = 1
#         return 1
#     # Return a known result if it happens to be greater than 1
#     elif known_results[target] > 0:
#         return known_results[target]
#     else:
#         # for every coins value there is <= my target
#         for i in [c for c in coins if c <= target]:
#             num_coins = 1 + rec_coin(target - i, coins, known_results)
#             if num_coins < min_coins:
#                 min_coins = num_coins

#                 # reset the known result
#                 known_results[target] = min_coins

#     return min_coins

print(rec_coin(10,[1,5,4]))

    
    

