def trap(height):
    if len(height) < 3:
            return 0
    total = 0
    l_end, r_end = 0, len(height) - 1
    # find edge high points
    while height[l_end + 1] > height[l_end]:
        l_end += 1
    while height[r_end - 1] > height[r_end]:
        r_end -= 1
    # divide and conquer
    # heap to split:
    to_split = [(l_end, r_end)]
    # heap to calculate
    to_calculate = []
    while to_split:
        l, r = to_split.pop()
        if abs(l-r) <= 1:
            continue
        # find max
        max_index = height[l:r].index(max(height[l + 1:r])) + l
        if height[max_index] < height[l] and height[max_index] < height[r]:
            to_calculate.append((l, r))
        else:
            to_split.extend([(l, max_index), (max_index, r)])
    for section in to_calculate:
        bound = min(height[section[0]], height[section[1]])
        total += sum([-x for x in height[section[0] + 1: section[1]]]) + (bound*(section[1]-section[0]-1))
    return total

print(trap([0,2,0,3,1,0,1,3,2,1]))