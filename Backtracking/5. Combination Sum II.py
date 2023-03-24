class Solution:
    #Time complexity: O(N*2^N) (worst case), Space complexity: O(N) (worst case of the recursion tree)
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(i, sum, set):
            if sum == target: 
                ans.append(set.copy())
                return
            if i == len(candidates): return
            
            if (sum + candidates[i] <= target):
                set.append(candidates[i])
                backtrack(i + 1, sum + candidates[i], set)
                set.pop()
            
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i += 1
            backtrack(i, sum, set)

        candidates.sort()
        backtrack(0, 0, [])
        return ans