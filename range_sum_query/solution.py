from typing import List


class NumArray:
    """asdfsf."""

    def __init__(self, nums: List[int]):
        self.runningTotal = [0]

        for num in nums:
            self.runningTotal.append(self.runningTotal[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.runningTotal[j + 1] - self.runningTotal[i]
