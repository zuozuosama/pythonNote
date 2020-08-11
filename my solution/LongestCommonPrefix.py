from typing import List


class LongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        a = min(strs)
        b = max(strs)
        for i, x in enumerate(a):
            if b[i] != x:
                return a[:i]
        return a
