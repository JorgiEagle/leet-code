num = 5

print(bin(num))

mask_len = 0
while num > 0:
    mask_len += 1
    num >>= 1

num = 5

print(bin(num ^ ((1 << mask_len)-1)))