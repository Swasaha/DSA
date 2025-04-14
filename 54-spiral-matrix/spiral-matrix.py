from typing import List
class Solution:
    def spiralOrder(self,matrix:List[list[int]])->List[int]:
        if not matrix:
            return []
        top_row=matrix.pop(0)
        rotated=list(zip(*matrix))[::-1]
        rotated=[list(row)for row in rotated]
        return top_row + self.spiralOrder(rotated)