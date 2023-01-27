### Problem
1491. Average Salary Excluding the Minimum and Maximum Salary
Easy
1.1K
128
company
Amazon
Netsuite
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000
 

Constraints:

3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.

### Solution
This code defines a class Solution that has a method average(self, salary: List[int]) -> float. This method takes in a single parameter, salary, which is a list of integers.

The first line salary.sort() sorts the elements of the salary list in ascending order.

The second line data = salary[1:-1] assigns to the variable data all the elements in the list salary from the second element (index 1) to the second-to-last element (index -1). This will exclude the first and last elements of the original list.

The last line return sum(data) / len(data) returns the average of the elements in the data list. It calculates the sum of all elements in the data list using the sum() function and divide it by the length of the data list using the len() function.
