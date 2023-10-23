import timeit

def remove_dups(nums):
    m = 1
    i = 1
    saved_number = nums[0]
    while i < len(nums):
        current_number = nums[i]
        if (current_number == saved_number):
            nums.pop(i)
        else:
            m += 1
            i += 1
            saved_number = current_number
    return m

def remove_dups_alt(nums):
    i = 0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]

    for j in range(0, len(nums) - i - 1):
        nums.pop()
    return i + 1
        
nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
start = timeit.timeit()
print(remove_dups(nums))
end = timeit.timeit()
print (end - start)
# 8
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 9]

nums = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]
start = timeit.timeit()
print(remove_dups_alt(nums))
end = timeit.timeit()
print (end - start)
# 8
print(nums)
# [1, 2, 3, 4, 5, 6, 7, 9]

nums = [1, 1, 1, 1, 1, 1]
print(remove_dups(nums))
print(nums)
# 1
# [1]