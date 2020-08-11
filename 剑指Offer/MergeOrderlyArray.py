def merge_orderly_array(nums1, nums2):
    if not nums2:
        return nums1
    if not nums1:
        nums1 = nums2
        return nums1
    for nu in nums2:
        idx = len(nums1) - 1
        while idx >= 0 and nu < nums1[idx]:
            idx -= 1
        nums1.insert(idx + 1, nu)

    return nums1


if __name__ == '__main__':
    nums1 = [2, 7, 13, 19, 23, 45]
    nums2 = [1, 3, 8, 10, 31]
    print(merge_orderly_array(nums1, nums2))
