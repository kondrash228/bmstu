import sys

a = int(input())

nums = []
nums.append(a)


def convert_base(num, to_base=10, from_base=10):
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


for _ in range(3):
    a += 1
    nums.append(int(convert_base(a, 10, 7)))

# new_str = ''
# for i in range(len(nums)):
#     new_str += str(nums[i])


print(nums)


def add_x(x):
    j = 0

    for elem in nums:
        if elem == nums[0]:
            continue

        if elem == nums[-1]:
            continue

        nums.insert(nums.index(elem) + 1, x)

        print(nms)

    new_str = ''

    for i in range(len(nums)):
        new_str += str(nums[i])

    return int(new_str)


flag = True
x = 1
print(add_x(3))
# while flag:
#     print( f"x = {x}")
#     if int(convert_base(add_x(x), 10, 3 * x)) / (3 * x) - 1 == 0:
#         print(f'x = {x}')
#         flag = False
#     else:
#         x += 1

"""
    while flag:
        print(int(convert_base(int(new_str), 7, 10)))
        if int(convert_base(int(new_str), 7, 10)) / (3 * x) - 1 == 0:
            flag = False
            print(f'Успех x = {x}')
        else:
            x += 1
"""

"""
    while j < len(nums):
        if j == 0:
            j += 1
            continue

        if j == len(nums) - 1:
            break
        print(f'nums = {nums}')
        nums.insert(j, x)
        j += 1

"""
u
