# 1: Two Sum
def two_sum(nums, target):
    seen = {}
    num = 0
    needed = 0

    for i in range(len(nums)):
        num = nums[i]
        needed = target - num

        if needed in seen:
            return [seen[needed], i]
        
        seen[num] = i


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))



# 2: Best Time to Buy and Sell Stock
def maxProfit(prices):
    minimum_price = prices[0]
    maximum_profit = 0

    for price in prices[1:]:
        if price < minimum_price:
            minimum_price = price
        else:
            profit = price - minimum_price
            if profit > maximum_profit:
                maximum_profit = profit

    return maximum_profit

prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))