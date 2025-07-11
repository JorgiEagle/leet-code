from collections import deque


def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        # size of gap, index of gap (events to left and right can't be used, this gap is equal to event index or equal to event index -1)
        gaps = [(0, None)] * (len(startTime) + 1)
        current_window = deque(maxlen=3)
        # first gap
        current_window.append(startTime[0])
        gaps[0] = (startTime[0], -1)
        # tuples, total window cost, event cost, event_index
        max_with_move = []
        max_with_push = startTime[0]
        for i in range(len(startTime)):
            # calculate the gap ahead of the current event index
            if i >= len(startTime)-1:
                next_gap = eventTime - endTime[-1] 
            else:
                next_gap = startTime[i+1] - endTime[i]
            gaps[i+1] = (next_gap, i)
            # add current event and next gap to current window
            current_event_time = endTime[i] - startTime[i]    
            current_window.append(current_event_time)
            current_window.append(next_gap)
            
            # handle largest gap obtained by pushing one event to the edge
            current_window_push_gap = current_window[0] + current_window[-1]
            max_with_push = max(max_with_push, current_window_push_gap)
            # add max_with_move to list if greater than current max push
            if sum(current_window) > max_with_push:
                max_with_move.append((sum(current_window), current_event_time, i))

        # sort gaps
        gaps.sort(key=lambda x: x[0], reverse=True)

        # sort max_with_move
        max_with_move.sort(key=lambda x: x[0], reverse=True)
        
        for total_gap, event_size, event_index in max_with_move:
            if total_gap <= max_with_push:
                return max_with_push
            gap_index = 0
            while event_size <= gaps[gap_index][0]:
                if gaps[gap_index][1] not in (event_index, event_index-1):
                    return total_gap
                gap_index += 1
        return max_with_push
        