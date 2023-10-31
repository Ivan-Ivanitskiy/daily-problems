def majority_element(nums):
    element_count = {}
    half_len = len(nums) / 2
    for num in nums:
        if num in element_count:
            element_count[num] += 1
            if element_count[num] > half_len:
                return num
        else:
            element_count[num] = 1
    return None

def majority_element_alt(nums):
    count = 0
    result = 0

    for num in nums:
        if count == 0:
            result = num

        if result == num:
            count += 1
        else:
            count -= 1

    return result

print(majority_element([3, 5, 3, 3, 2, 4, 3]))
print(majority_element_alt([3, 5, 3, 3, 2, 4, 3]))
# 3