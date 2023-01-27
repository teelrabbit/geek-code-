class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        data = salary[1:-1]
        return sum(data) / len(data)

    

