"""
825. Friends Of Appropriate Ages
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person. 

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:
Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

Notes:
1 <= ages.length <= 20000.
1 <= ages[i] <= 120.
"""
# Time complexity: O(N) but ~O(1), ages should be very small
# Space complexity: O(N), ~O(1)
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        def friend_request(a, b):
            return not (b <= 0.5 * a+7 or b > a or b > 100 and a < 100)
        
        counter = collections.Counter(ages)
        total = 0
        for a in counter:
            for b in counter:
                if a == b:
                    total += friend_request(a, b) * counter[a] * (counter[b] - 1)
                else:
                    total += friend_request(a, b) * counter[a] * counter[b]
        return total
        
"""
Write a sub function request(a, b) to check if age a will friend requests age b.
return !(condition1 || condition2 || condition3)

Count number of all ages to a map.
Because we have at most 20000 ages but only in range [1, 120].

For each age a and each age b != a, if request(a, b), we will make count[a] * count[b] requests.

For each age a, if request(a, a), we will make count[a] * (count[a] - 1) requests.
"""
