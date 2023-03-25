class Solution:
    #Time complexity: N*2^N, Space complexity: O(N)
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        result = []

        def palindrome(k):
            t = len(k)
            for i in range(t):
                if k[i] != k[t-i-1]: return False
            return True

        def backtrack(start, subindex, k):
            if start == n:
                if palindrome(k[subindex]): 
                    result.append(k.copy())
                return

            k[subindex] += s[start]
            backtrack(start + 1, subindex, k)
            k[subindex] = k[subindex][:-1]

            if not palindrome(k[subindex]): return

            k.append(s[start])
            backtrack(start + 1, subindex + 1, k)
            k.pop()
        backtrack(1, 0, [s[0]])
        return result