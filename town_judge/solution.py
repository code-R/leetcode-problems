from typing import List


class Solution:
    """Leet code."""

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1

        trustArr = [0] * (N + 1)

        for (person1, person2) in trust:
            trustArr[person1] -= 1
            trustArr[person2] += 1

        for (i, x) in enumerate(trustArr):
            if (x == N - 1):
                return i

        return -1
