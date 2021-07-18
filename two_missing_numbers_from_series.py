import random

master_list = list(range(0, 101))
random.shuffle(master_list)
print(master_list)
q = master_list.pop()
w = master_list.pop()


def find_missing_brute_force(master_list):
    out = []
    for x in range(len(master_list) + 2):
        if x not in master_list:
            out.append(x)
    print(out)


def find_missing_math(master_list):
    s = sum(master_list)
    s2 = ((len(master_list) + 2) * (len(master_list) + 1)) / 2
    sum_of_two = s2 - s
    # q,w are the two numbers, then
    # q + w = sum_of_two
    # q,w are distinct so q<w or w<q assuming q<w
    avg = int(sum_of_two // 2)
    # q < avg < w
    # sum of elements including avg -> expected
    # sum of elements in array including less than or equal to avg -> calculated
    # expected - calculated is the
    q = int((avg * (avg + 1)) / 2 - sum(x for x in master_list if x <= avg))
    w = int(sum_of_two) - q
    print([q, w])


print("Actual missing elements in the list:\t", [q, w])
print("Calculated from brute force approach", end=":\t")
find_missing_brute_force(master_list)
print("Calculated from sum and average approach", end=":\t")
find_missing_math(master_list)
