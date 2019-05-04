f = open("task3.txt")
def input():
    return f.readline()
# LOCAL
#------------------------------------------------------------------------------------------------


import sys

# simulate
def query0(input_data, bad_bits = {990, 991, 992, 993, 994, 995, 996, 997, 998, 999, 1000}): 
    return "".join([x for i,x in enumerate(input_data) if i not in bad_bits])

# real
def query(input_data): 
    print(input_data)
    output_data = input()
    return output_data 


T = int(input())
for i in range(T):
    GuessCount, N =  [int(x) for x in input().strip().split(" ")]

    input_data = initial_guess
    for i in range(GuessCount):
        response = query(input_data)
        input_data = generate_next_query(response)

    # guess
    print(input_data)
    verdict = input()

