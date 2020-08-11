from typing import List

"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""


class LetterCombinations:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        phoneLetter = {
            "2": "abc",
            "3": "edf",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        product = ['']
        for x in digits:
            product = [i + j for i in product for j in phoneLetter[x]]
        return product

if __name__ == '__main__':
    let = LetterCombinations()
    print(let.letterCombinations("23"))