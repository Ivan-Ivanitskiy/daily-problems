import math

def find_num(nums, target):
    left_edge = findEdge(nums, target, 0, math.ceil(len(nums)/2) - 1, 1, 0)
    print("----")
    right_edge = findEdge(nums, target, 0, math.ceil(len(nums)/2) - 1, -1, 0)
    return (left_edge, right_edge)

# lr is +1 if we are looking for the left edge of the interval and -1 otherwise
def findEdge(nums, target, i, step, lr, depth):
    print(i, step)
    depth += 1
    if depth > 5:
        return -1
    i += step
    step = abs(step)
    if (i < 0) or (i >= len(nums)):
        return -1
    if lr * nums[i] < lr * target:
        step = lr * max(1, math.ceil(step/2) - 1)
    elif lr * nums[i] > lr * target:
        step = (-1) * lr * max(1, math.ceil(step/2) - 1)
    elif (nums[i] == target) and (nums[i - lr] != target):
        return i
    else:
        step = (-1) * lr * max(1, math.ceil(step/2) - 1)
    return findEdge(nums, target, i, step, lr, depth)

print(find_num([1, 1, 3, 5, 7], 1))
# (0, 1)

print(find_num([1, 1, 2, 2, 2, 2, 3, 3, 3, 5, 5, 6, 7], 5))
# (9, 10)

print(find_num([1, 2, 3, 4, 4, 4, 4], 5))
# (-1, -1)