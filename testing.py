def productExceptSelf(nums):
    res = [1] * (len(nums))

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res

nums = [1, 2, 3, 4]
productExceptSelf(nums)

import collections
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()

strs = ["eat","tea","tan","ate","nat","bat"]
groupAnagrams(strs)



def isValidSudoku(board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set)  # key = (r /3, c /3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True


board = [[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."],
         [".", ".", "2", ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."],
         [".", ".", "4", ".", ".", ".", ".", ".", "."]]
isValidSudoku((board))

