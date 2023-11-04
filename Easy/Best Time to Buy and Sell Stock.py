'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.



Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104


'''
from typing import List


## Brute Force
class SolutionOne:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = None
        sell_price = None
        profit = 0
        for i in range(len(prices) - 1):
            if buy_price is None:
                buy_price = prices[i]
                sell_price = max(prices[i + 1:])
                profit = sell_price - buy_price if buy_price < sell_price else 0
            elif prices[i] < buy_price:
                buy_price = prices[i]
                sell_price = max(prices[i + 1:])
                if sell_price - buy_price > profit:
                    profit = sell_price - buy_price
        return profit


## Two Pointer Method
class SolutionTwo:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        if len(prices) < 2:
            return 0
        max_profit = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            elif prices[left] < prices[right]:
                if max_profit < prices[right] - prices[left]:
                    max_profit = prices[right] - prices[left]
            right += 1
        return max_profit


if __name__ == '__main__':
    sol = SolutionTwo()
    strs = [1, 2, 3, 1, 5]
    output = 4
    result = sol.maxProfit(prices=strs)
    print(result)
    assert output == result
