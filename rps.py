f = open("rps.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------

# return best of 2 selected
def best_char(used_chars):
    char_list = list(used_chars)
    char_list.sort()
    chars = "".join(char_list)

    if chars == "PR":
        return "P"

    if chars == "PS":
        return "S"

    if chars == "RS":
        return "R"

# return bette then 1 selected
def better_char(used_chars):
    char_list = list(used_chars)
    char = char_list[0]

    if char == "P":
        return "S"

    if char == "R":
        return "P"

    if char == "S":
        return "R"

from functools import reduce
def get_best_program(programs):
    max_len = reduce(lambda x,y: x * y, set(len(p) for p in programs))

    # pad to same len
    for p in programs:
        lp = len(p)
        for i in range(lp, max_len):
            p.append(p[i % lp])

    best_program = ""
    for i in range(max_len):

        # if there are 3 chars => impossible
        # if there are 2 chars => draw possible
        # if there are 1 chars => win possible
        used_chars = set()
        for program in programs:
            used_chars.add(program[i])

            if len(used_chars) == 3:
                return "IMPOSSIBLE"
        else:
            if len(used_chars) == 2:
                best_program = best_program + best_char(used_chars)
            else: # 1 char
                best_program = best_program + better_char(used_chars)
                return best_program

    return "IMPOSSIBLE"

import sys

T = int(input())
for i in range(T):
    number_of_robots =  int(input().strip()) 

    programs = []
    for n in range(number_of_robots):
        programs.append(list(input().strip()))

    result = get_best_program(programs)

    print("Case #{0}: {1} ".format(i + 1, "".join(result)))
