class Solution:
# Worst Time complexity is O(2^Target)
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sets = []
        def backtrack(i, cur, set):
            if cur > target or i == len(candidates): return
            if cur == target:
                sets.append(set.copy())
                return
            
            # choose to add this index
            set.append(candidates[i])
            backtrack(i, cur + candidates[i], set)
            set.pop()

            # not choose to add this index
            backtrack(i + 1, cur, set)
        backtrack(0, 0, [])
        return sets