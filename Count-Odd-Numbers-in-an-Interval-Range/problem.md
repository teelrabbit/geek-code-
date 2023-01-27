Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

 

Example 1:

Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].
Example 2:

Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].
 

Constraints:

0 <= low <= high <= 10^9


### Explanation 
This solution takes advantage of the fact that odd numbers are separated by even numbers. If the low number is even, it is incremented to the next odd number. If the high number is even, it is decremented to the previous odd number. Then, we can simply calculate the number of odd numbers within the range by dividing the difference between the modified low and high by 2 and adding 1.
