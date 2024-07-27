import time

def validate_binary_list(nums: list) -> bool:
    return not bool(nums.difference({0, 1}))


def validate_binary_list_fast(nums: list) -> bool:
    return not bool({0, 1}.difference(nums))



long_list = set(range(100000000))
start_time = time.time()
validate_binary_list(long_list)
end_time = time.time()

print(end_time-start_time)

start_time = time.time()
validate_binary_list_fast(long_list)
end_time = time.time()

print(end_time-start_time)
