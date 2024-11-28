def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    mid = len(nums) // 2
    if len(nums) % 2 == 0:
        return (nums[mid - 1] + nums[mid]) / 2
    else:
        return nums[mid]

nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0
