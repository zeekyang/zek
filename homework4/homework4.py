# File name: homework4.py

#3.1
foods = ["sushi", "chicken rice", "carbonara", "steak", "mochi"]
print(foods[1])
print(foods[-1])
foods.append("ramen")
foods.insert(0, "apple")
del foods[2]
print(len(foods))
for food in foods:
    print(food.upper())
first_and_last = [foods[0], foods[-1]]
print(first_and_last)
if "potato" in foods:
    print("A potato!")
else:
    print("No potato!")

#3.2
numbers = list(range(21))
def get_first_15(numbers):
    return numbers[:15]
"""
I encountered this error:
TypeError: 'int' object is not subscriptable
I originally wrote: return numbers[15]
I forgot to include the colon for slicing a list and I fixed it by adding the colon: return numbers[:15]
"""

def get_every_5th(lst):
    return lst[::5]

def reverse_and_stride(lst):
    reversed_lst = lst[::-1]
    return reversed_lst[::3]

step1 = get_first_15(numbers)
step2 = get_every_5th(step1)
step3 = reverse_and_stride(step2)
print(step3)

#3.3
numbers = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print(numbers[2])

"""
I encountered this error:
IndexError: list index out of range
I originally wrote: print(numbers[3])
I forgot that the index starts at 0, and I fixed it by rewriting the index: print(numbers[2])
"""

print(numbers[1][1])
numbers.append([10, 11, 12])
def sum_nested(nested_list):
    total = 0
    for row in nested_list:
        for num in row:
            total += num
    return total
print(sum_nested(numbers))

#3.4
def create_5x5():
    result = []
    num = 1
    for i in range(5):
        row = []
        for j in range(5): 
            row.append(num)
            num += 1
        result.append(row)
    return result
grid = create_5x5()
print(grid)

def replace_m3(lst):
    new_result = []
    for row in lst:
        new_row = []
        for num in row:
            if num % 3 == 0:
                new_row.append("?")
            else:
                new_row.append(num)
            """
I encountered this error:
SyntaxError: invalid syntax
I originally wrote: if num % 3 = 0
I did not use the correct equals sign. I fixed it by adding the right equal notation: if num % 3 == 0
"""
        new_result.append(new_row)
    return new_result
new_grid = replace_m3(grid)
print(new_grid)

def sum_non_question(grd):
    total = 0
    for row in grd:
        for newsum in row:
            if newsum != "?":
                total += newsum
    return total

total_sum = sum_non_question(new_grid)
print(total_sum)

#4.1
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25,
    "Mira": 48
}
print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]
for name, age in ages.items():
    print(f"{name}, {age}")

#5.2
numbers2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

result2 = sum_nested(numbers)
print("The total sum of all numbers in the nested list is:", result2)










