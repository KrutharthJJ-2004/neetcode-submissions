class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i,x in enumerate(numbers):
            need = target - x
            if need in seen:
                return [seen[need]+1,i+1]
            seen[x]=i