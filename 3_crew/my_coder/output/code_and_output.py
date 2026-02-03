
def first_missing_positive(nums):
    n = len(nums)

    # Base case: if the array is empty
    if n == 0:
        return 1

    # Step 1: Replace negative numbers and zeros with a number greater than n
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    # Step 2: Mark numbers present in the array
    for i in range(n):
        num = abs(nums[i])
        if 1 <= num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    # Step 3: Find the first index with a positive value
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    # If all numbers are present, the missing positive is n + 1
    return n + 1

# Test cases
print(first_missing_positive([1, 2, 0]))  # Output: 3
print(first_missing_positive([3, 4, -1, 1]))  # Output: 2
print(first_missing_positive([7, 8, 9, 11, 12]))  # Output: 1


# Output:
# ```
# 3
# 2
# 1
# ```