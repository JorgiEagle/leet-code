def minMovesToSeat(seats: list[int], students: list[int]) -> int:
        seats.sort()
        students.sort()
        x = list(zip(seats, students))
        return sum(map(lambda x: abs(x-y), zip(seats, students)))


minMovesToSeat([3,1,5],[2,7,4])