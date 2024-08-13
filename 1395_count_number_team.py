from itertools import combinations
def numTeams(rating: list[int]) -> int:
        return len([x for x in combinations(rating, 3) if x[0] > x[1] > x[2]])

print(numTeams([2,5,3,4,1]))