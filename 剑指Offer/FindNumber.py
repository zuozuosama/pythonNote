def find_number(target, nums):
    if not nums:
        return False
    row, col = len(nums), len(nums[0])
    r, c = row - 1, 0
    while r >= 0 and c <= col - 1:
        cur = nums[r][c]
        if cur > target:
            r -= 1
        elif cur < target:
            c += 1
        else:
            return True
    return False

if __name__ == '__main__':
    seq=[
        [1,2,8,9],
        [2,4,9,12],
        [4,7,10,13],
        [6,8,11,15]
    ]
    print(find_number(7,seq))
