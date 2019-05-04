#------------------------------------------------------------------------------------------------------------
# Priority Max Q
import heapq
class Item:
    def __init__(self, value):
        self.value = value
        self.deleted = False

    def __lt__(self, value):
        return True

    def __repr__(self):
        return "({0}, {1})".format(self.value, self.deleted)

class MaxPQ:
    def __init__(self):
        self.data = []

    def push(self, value):
        item = Item(value)
        heapq.heappush(self.data, (-value, item))

        return item 

    def max(self):
        while self.data[0][1].deleted:
            heapq.heappop(self.data)

        return -self.data[0][0]
#------------------------------------------------------------------------------------------------------------
# Scanline
def count_intersections(all_segments):
    segments_l = defaultdict(list)
    segments_r = defaultdict(list)

    keys = set()
    for rect in all_segments:
       l_key, r_key = rect[0][1], rect[1][1]
       segments_l[l_key].append(rect)
       segments_r[r_key].append(rect)
       keys |= set([l_key, r_key])

    keys_list = list(keys)
    keys_list.sort()

    active_segments = []
    max_intersections = 0
    max_intersection_key = -1
    for key in keys_list:
        if len(segments_l[key]):
            active_segments += segments_l[key]

            if max_intersections < len(active_segments):
                max_intersections = len(active_segments)
                max_intersection_key = key

        for segment in segments_r[key]:
            active_segments.remove(segment)

    return  max_intersections, max_intersection_key 

#------------------------------------------------------------------------------------------------------------
# Greatest Common Divisor

def gcd(a, b):
    a, b = (a, b) if a > b else (b, a)
    while a != b:
        a = a - b
        a, b = (a, b) if a > b else (b, a)

    return a

#------------------------------------------------------------------------------------------------------------
# 
