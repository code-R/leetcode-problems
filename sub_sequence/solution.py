class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0

        for i, _ in enumerate(t):
            try:
                if t[i] == s[ptr]:
                    ptr += 1
            except IndexError:
                return True

        return ptr == len(s)
