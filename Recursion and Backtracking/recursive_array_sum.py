# ------------------Variant 1-------------------------------- #

def calculate_recursive(nums, idx):
    """
    Recursively calculates the sum of elements in a list starting from a given index.

    Parameters:
    nums (list of int): The list of integers to sum.
    idx (int): The current index in the list from which to start summing.

    Returns:
    int: The sum of the elements in the list from the current index to the end.
    """
    if idx == len(nums):
        return 0

    return nums[idx] + calculate_recursive(nums, idx + 1)


nums = [int(x) for x in input().split()]

print(calculate_recursive(nums, 0))


# ------------------Variant 2-------------------------------- #

def calculate_recursive(nums, idx):
    """

    The calculate_recursive function calculates the sum of elements in a list of numbers (nums) using recursion.
    It starts at a specified index (idx) and proceeds to sum all elements until the end of the list.

    """
    if idx == len(nums) - 1:
        return nums[idx]

    return nums[idx] + calculate_recursive(nums, idx + 1)


nums = [int(x) for x in input().split()]

print(calculate_recursive(nums, 0))
