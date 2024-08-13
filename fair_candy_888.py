def fairCandySwap(aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
    alice_sum = sum(aliceSizes)
    bob_sum = sum(bobSizes)
    swap = bob_sum - alice_sum
    for x in aliceSizes:
        if (swap+x) in bobSizes:
            return [x, swap+x]
        

print(fairCandySwap([1, 1], [2,2]))