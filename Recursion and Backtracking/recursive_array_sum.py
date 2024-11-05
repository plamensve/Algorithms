# ------------------Variant 1-------------------------------- #

def calculate_recursive(nums, idx):
    if idx == len(nums):
        return 0

    return nums[idx] + calculate_recursive(nums, idx + 1)


nums = [int(x) for x in input().split()]

print(calculate_recursive(nums, 0))


# ------------------Variant 2-------------------------------- #

def calculate_recursive(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calculate_recursive(nums, idx + 1)


nums = [int(x) for x in input().split()]

print(calculate_recursive(nums, 0))
