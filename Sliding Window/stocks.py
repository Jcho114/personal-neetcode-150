"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List
import math

def maxProfit(prices: List[int]) -> int:
  res, sell = 0, math.inf
  for buy in prices:
    sell = min(sell, buy)
    res = max(res, buy - sell)
  return res

"""
When we are at a certain point in time, we make the most profit if
we sold at the point at which it was cheapest before the aforementioned
time. We can do this by maintaining a relative minimum variable as we
iterate through the prices. We also maintain a variable keeping track
of our largest profit.

TC: O(n)
SC: O(1)
"""