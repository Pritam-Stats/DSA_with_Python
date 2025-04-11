def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)

    only_in_nums1 = list(set1 - set2)
    only_in_nums2 = list(set2 - set1)
    return [only_in_nums1, only_in_nums2]


print(findDifference(nums1 = [1,2,3], nums2 = [2,4,6]))
print(findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))