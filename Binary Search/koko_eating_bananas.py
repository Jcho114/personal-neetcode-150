"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

from typing import List
import math

def minEatingSpeed(piles: List[int], h: int) -> int:
  low, high = 1, max(piles)

  while low < high:
    mid = (low + high) // 2
    time = 0
    for pile in piles:
      time += math.ceil(pile / mid)
      if time <= h:
        high = mid
      else:
        low = mid + 1
        
  return low

"""
We basically perform a binary search where the low, high, and middle
values represent rates at with Koko will eat bananas. If Koko can eat
all of here bananas within the time frame, we know that we can try
to have her eat less. If she can't finish them, we know that we should
have her eat more. Eventually, we end up with the minimum number of
bananas Koko should eat per hour to finish eating the food in time.
TC: O(n*lg(h))
SC: O(1)
"""