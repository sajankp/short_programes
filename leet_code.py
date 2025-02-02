from typing import List


def remove_element(the_list: List[int], val: int) -> int:
    k = 0
    i = len(the_list) - 1
    while i > -1:
        if the_list[i] == val:
            del (the_list[i])
            k += 1
            i -= 1
        else:
            i -= 1
    return k


print("---" * 10)
print("removeElement")
nums1 = [0, 1, 2, 2, 3, 0, 4, 2]
print(nums1)
print(f"val 2")
out = remove_element(nums1, 2)

print(out)
print(nums1)


def is_palindrome(s: str) -> bool:
    # q = [x.lower() for x in s if x.isalnum()]
    # return q == q[::-1]
    a = 0
    b = len(s) - 1
    while a > b:
        if s[a].isalnum() and s[b].isalnum():
            if s[a] == s[b]:
                a += 1
                b -= 1
            else:
                return False
        elif s[a].isalnum():
            b -= 1
        else:
            a += 1
    return True


x = is_palindrome("race a car")
print(x)


def min_sub_array_len_cognitive(target: int, nums: List[int]) -> int:
    left = 0
    curr_sum = 0
    min_length = float("infinity")
    # for x in range(len(nums)):
    #     for y in range(x + 1, len(nums)+1):
    #         if sum(nums[x:y]) >= target:
    #             if y - x < least_num:
    #                 least_num = y - x
    # return least_num
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            if right - left < min_length:
                min_length = right - left + 1
            curr_sum -= nums[left]
            left += 1
    if min_length == float("infinity"):
        return 0
    else:
        return min_length


print("----------" * 10)
nums1 = [2, 3, 1, 2, 4, 3]
the_target = 7
print(min_sub_array_len_cognitive(the_target, nums1))

print("----------" * 10)
