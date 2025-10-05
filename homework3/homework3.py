# File: homework3.py

#3.1
def say_goodbye(name):
    print("Goodbye,",name)
# say_goodbye("Nebuchadnezzar")

#3.2
def area_of_circle(radius):
    print((radius ** 2) * 3.14) #area of circle is r^2 * pi
# area_of_circle(5)

#4.1
def subtract(a, b):
    return a - b
print(subtract(2,1))
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b  # There will be an error if b = 0

#5.1
readings = [15, 14, 17, 20, 23, 28, 20]
def what_to_wear(readings):
    return min(readings), max(readings)

#5.2
def is_weekend(day_number):
    if day_number == 6 or day_number == 7:
        return True
    else:
        return False
    
#5.3
def fuel_efficiency(distance, fuel):
   return distance / fuel

#5.4
def encrypt(n):   
    last_digit = n % 10
    other_digits = n // 10
    num_digits = len(str(other_digits))
    
    encrypted = last_digit * (10 ** num_digits) + other_digits
    return encrypted

#6.1
def power(x, y):
    result = 1

    for n in range(abs(y)):
        result *= x

    if y < 0:
        return 1 / result
    else:
        return result
# print(power(2,3))

#6.2.1
def find_min_for(nums):
    min_num = nums[0]
    for num in nums:
        if num < min_num:
            min_num = num
    return min_num

def find_max_for(nums):
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

#6.2.2
def find_min_while(nums):
    min_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] < min_num:
            min_num = nums[i]
        i += 1
    return min_num

def find_max_while(nums):
    max_num = nums[0]
    i = 1
    while i < len(nums):
        if nums[i] > max_num:
            max_num = nums[i]
        i += 1
    return max_num

numbers_list = [1,2,3,4,5]

# print(find_min_for(numbers_list))
# print(find_max_for(numbers_list))
# print(find_min_while(numbers_list))
# print(find_max_while(numbers_list))

#6.3
def sum_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total
# print(sum_digits(1234))

#7.1
x = 2
y = 3
result = power(x, y)
print(f"The result of Oski Stole Your Power (5.1) with x = {x} and y = {y} is {result}.")
