from heapq import heappush, heappushpop
from typing import List


def mostBooked(n: int, meetings: List[List[int]]) -> int:
        # min heap of rooms. room meeting endtime, room number, number of meeting held in room
        rooms = [(0, index, 0) for index in range(1, n)]
        current_room = (0, 0, 0)
        meetings.sort(key=lambda x: x[0])
        for meeting_start, meeting_end in meetings:
            duration = meeting_end - meeting_start
            room_endtime, room_number, number_of_meetings = current_room
            room_endtime = max(room_endtime, meeting_start)
            new_room = (room_endtime + duration, room_number, number_of_meetings + 1)
            current_room = heappushpop(rooms, new_room)
        heappush(rooms, current_room)
        return max(rooms, key=lambda x: (x[2], -x[1]))[1]


def main():
    n = 4
    meetings = [[18,19],[3,12],[17,19],[2,13],[7,10]]
    print(mostBooked(n, meetings))


if __name__ == "__main__":
    main()