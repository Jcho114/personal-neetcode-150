"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

def top_k_frequent_elements(nums, k):
  freqs = {}
  for n in nums:
    if n not in freqs:
      freqs[n] = 0
    freqs[n] += 1
  return sorted(freqs.keys(), key=lambda el: freqs[el], reverse=True)[:k]

"""
Use a dictionary to track frequencies of each number
Sort the numbers by their frequency then return the top k elements

Time Complexity: O(n)
Space Complexity: O(n)
"""