def sum_combinations(nums, target):
    nums.sort()
    return findSum(nums, [], target)

def findSum(nums_sorted, addends, target):
    addends_combinations = []
    for i, num in enumerate(nums_sorted):
        addends_ = addends[0:]
        addends_.append(num)
        current_sum = sum(addends_)
        if current_sum > target:
            break
        nums_sorted_ = nums_sorted[i+1:]
        if current_sum == target:
            addends_combinations.append(addends_)
            break
        addends_combinations += findSum(nums_sorted_, addends_, target)
    return remove_duplicates(addends_combinations)

def remove_duplicates(data):
    result = []
    for raw in data:
        if raw not in result:
            result.append(raw)
    return result

print(sum_combinations([10, 1, 2, 7, 6, 1, 5], 8))
# [(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)]