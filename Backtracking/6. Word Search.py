class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        def backtrack(i, row, col):
            if board[row][col] != word[i]: return False
            c = board[row][col]
            board[row][col] = "*"
            if i == len(word) - 1: return True
            for j in range(4):
                if (0 <= row + dx[j] < m and 0 <= col + dy[j] < n
                and board[row + dx[j]][col + dy[j]] != "*"):
                    if backtrack(i+1, row + dx[j], col + dy[j]): return True
            board[row][col] = c
            return False
        
        for row in range(m):
            for col in range(n):
                if backtrack(0, row, col): return True
        return False
       