def map_number(number, mapping):
    digits = str(number)
    mapping = {str(index): str(num) for index, num in enumerate(mapping)}
    return int(''.join(mapping[x] for x in digits))


mapping = [1,2,8,6,3,7,4,5,9,0]
nums = [8248059]

for num in nums:
    print(map_number(num, mapping))