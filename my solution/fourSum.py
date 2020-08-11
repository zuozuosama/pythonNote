from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = set()
        ret.add("()")
        if n == 1:
            return [i for i in ret]
        else:
            for x in range(n-1):
                newset = set()
                for j in ret:
                    newset.add("()"+j)
                    newset.add("("+j+")")
                    newset.add(j+"()")
                ret = newset
            ls = [i for i in ret]
            ls.sort()
            return ls

if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(4))

