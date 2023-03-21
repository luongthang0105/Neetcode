class Solution:
# Time complexity: O(N * 2^N) since it takes O(N) to append any subset with average length of N
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtracking(i, set):
            if i >= len(nums): 
                ans.append(set.copy())
                return

            #choose to add index i
            set.append(nums[i])
            backtracking(i + 1, set)
            set.pop()

            backtracking(i + 1, set)
        backtracking(0, [])
        return ans
            

