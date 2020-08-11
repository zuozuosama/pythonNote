def duplicate(nums):
    if not nums:
        return False
    nums_len = len(nums)
    for nu in nums:
        if nu < 0 or nu > nums_len - 1:
            return False
    for ni in range(nums_len):
        while nums[ni] != ni:
            cur = nums[ni]
            if nums[ni] == nums[cur]:
                return True
            nums[ni], nums[cur] = nums[cur], nums[ni]

    return False


if __name__ == '__main__':
    seq = [2, 3, 1, 0, 2, 5, 3]
    print(duplicate(seq))
