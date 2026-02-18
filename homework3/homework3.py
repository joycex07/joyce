def say_goodbye (name):
    print("Goodbye ", name)

def area (r):
    print (3.14 * (r ** 2))

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    assert b != 0
    return a/b

def min_max (temp):
    return (min(temp), max(temp))

def is_weekend (num):
    if num == 6 or num == 7:
        return True
    return False

def fuel_efficiency (distance, fuel):
    return distance/fuel

def encrypt_num (num):
    temp = num
    length = 0
    while temp > 0:
        length += 1
        temp = temp // 10

    last_digit = num % 10
    num = num // 10
    num = num + last_digit * (10 ** (length - 1))
    return num

def exp (x, y):
    total = 1
    for i in range(y):
        total = total * x
    return total

def for_min(nums):
    min = nums[0]
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
    return min

def for_max(nums):
    max = nums[0]
    for i in range(len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max

def while_min(nums):
    i = 0
    min = nums[0]
    while (i < len(nums)):
        if nums[i] < min:
            min = nums[i]
        i += 1
    return min

def while_max(nums):
    i = 0
    max = nums[0]
    while (i < len(nums)):
        if nums[i] > max:
            max = nums[i]
        i += 1
    return max

def sum_digits(num):
    total = 0
    while num > 10:
        total += num % 10
        num = num // 10
    total += num
    return total

num = 12345
result = sum_digits(num)
print("The sum of the digits of", num, "is", result)