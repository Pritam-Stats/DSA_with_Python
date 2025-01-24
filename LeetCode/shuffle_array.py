def shuffle(nums: list[int], n: int) -> list[int]:
    x_pointer = 0
    y_pointer = n
    shuffled = []
    while y_pointer < 2*n:
        shuffled.append(nums[x_pointer])
        shuffled.append(nums[y_pointer])
        x_pointer += 1
        y_pointer += 1
    return shuffled

print(shuffle(nums = [2,5,1,3,4,7], n = 3)) # [2,3,5,4,1,7]