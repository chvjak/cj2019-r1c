f = open("bacterial.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------


def is_free(row):
    for x in row:
      if x == "#":
          return False
    else:
        return True

def transpose(rows):
    if not len(rows):
        return []

    columns = [[] for x in range(len(rows[0]))]
    for r, row in enumerate(rows):
        for c, char in enumerate(row):
            columns[c].append(char)

    return columns


def get_win_pos_count(rows):
    result = 0
    for r, row in enumerate(rows):
        if is_free(row):
            above_wpc = get_win_pos_count(rows[:r])
            below_wpc = get_win_pos_count(rows[r + 1:])

            # if it is only 0 or 1+ cases matter could break the loop on first result and only on highest level loop through all
            if above_wpc == 0 and below_wpc == 0:
                result += len(row)
            elif above_wpc > 0 and below_wpc > 0:
                result += len(row)

    columns = transpose(rows)
    for c, column in enumerate(columns):
        if is_free(column):
            left_wpc = get_win_pos_count(columns[:c])
            right_wpc = get_win_pos_count(columns[c + 1:])

            if left_wpc == 0 and right_wpc == 0:
                result += len(column)
            elif left_wpc > 0 and right_wpc > 0:
                result += len(column)

    return result


import sys

T = int(input())
for i in range(T):
    R, C =  [int(x) for x in input().strip().split(" ")]
    
    rows = []
    for r in range(R):
        row = input().strip()
        rows.append(row)

    # Number of distinct winning openning moves for P1: i.e {(r1, c1, H), (r1, c1, V) ...}
    result = get_win_pos_count(rows)

    print("Case #{0}: {1}".format(i + 1, result))
