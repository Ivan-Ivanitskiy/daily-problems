import timeit

def fourSum(nums, target):
    nums.sort()
    return nSum(nums, [], 4, target)
        
def nSum(nums_sorted, addends, n, target):
    addends_combinations = []
    for i, num in enumerate(nums_sorted):
        addends_ = addends[0:]
        addends_.append(num)
        current_sum = sum(addends_)
        if current_sum > target:
            continue
        if (current_sum == target) and (n > 1):
            continue
        elif (n == 1) and (current_sum != target):
            continue
        nums_sorted_ = nums_sorted[i+1:]
        if (current_sum == target) and (n == 1):
            addends_combinations.append(addends_)
            continue
        addends_combinations_ = nSum(nums_sorted_, addends_, n-1, target)
        addends_combinations += addends_combinations_
    return remove_duplicates(addends_combinations)

def remove_duplicates(data):
    result = []
    for raw in data:
        if raw not in result:
            result.append(raw)
    return result

from collections import defaultdict

def fourSumAlt(nums, target):
  pairs = defaultdict(list)

  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      pairs[nums[i] + nums[j]].append((i, j))

  result = set()

  for p_sum, pairs_list in pairs.items():
    if target - p_sum not in pairs:
      continue

    for pair1 in pairs_list:
      for pair2 in pairs[target - p_sum]:
        if (
            pair1[0] != pair2[0] and pair1[0] != pair2[1] and
            pair1[1] != pair2[0] and pair1[1] != pair2[1]
        ):
          result.add(
              tuple(sorted([nums[pair1[0]], nums[pair1[1]], nums[pair2[0]], nums[pair2[1]]])))

  return [list(n) for n in result]

print(nSum([3], [], 1, 3))
start = timeit.timeit()
print(fourSum([1, 1, -1, 0, -2, 1, -1], 0))
end = timeit.timeit()
print (end - start)
start = timeit.timeit()
print(fourSumAlt([1, 1, -1, 0, -2, 1, -1], 0))
end = timeit.timeit()
print (end - start)
# print [[-1, -1, 1, 1], [-2, 0, 1, 1]]

print(fourSum([3, 0, 1, -5, 4, 0, -1], 1))
# print [[-5, -1, 3, 4]]

print(fourSum([0, 0, 0, 0, 0], 0))
# print ([0, 0, 0, 0])