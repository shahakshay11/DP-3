"""
// Time Complexity : O(N)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No

// Your code here along with comments explaining your approach
Algorithm Explanation
The main idea is to consider the elements in the row into 3 parts, 0th column, n-1th column and middle
Start at row 1, push down the minimum from the above by considering the adjacent columns in the previous row 
Algo
- For row = 1 to n
    For col = 0 to m:
        if col == 0 then
            A[row][col] += min(A[row-1][col],A[row-1][col+1])
        else if col == m-1  then
            A[row][col] += min(A[row-1][col],A[row-1][col-1])
        else
            A[row][col] += min(A[row-1][col],A[row-1][col-1],A[row-1][col+1])

- return min(A[-1]) # last row, fetch the minimum
"""
class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        for i in range(1,len(A)):
            for j in range(len(A[0])):
                if j == 0:
                    A[i][j] += min(A[i-1][j],A[i-1][j+1])
                elif j == len(A) - 1:
                    A[i][j] += min(A[i-1][j-1],A[i-1][j])
                else:
                    A[i][j] += min(A[i-1][j],A[i-1][j+1],A[i-1][j-1])
        return min(A[-1])