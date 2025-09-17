# File: homework1.py
# --- Variables and Data Types ---
a = 10
print(a)
print(type(a)) # a is an integer, a whole number with no decimals
b = 1.5
c = 3j
d = "hello"
e = [1, 2, 3]
f = {"name": "Ellen", "favorite fruit": "strawberry"}
g = (1, 2)
h = ["apple", "banana", "strawberry"]
i = True
j = None
k = [True, "blue", 12]
l = str(14)
m = 1e4
print(b,c,d,e,f,g,h,i,j,k,l,m)
print(type(b),type(c),type(d),type(e),type(f),type(g),type(h),type(i),type(j),type(k),type(l),type(m))
# b is a float, representing numbers with decimals.
# c is a complex, which is used for complex numbers with real and imaginary parts.
# d is a string, which is textual data.
# e is a list, which is an ordered collection of items that can be changed.
# f is a dictionary, which maps keys to values.
# g is a tuple, which is a fixed-size, ordered collection of items.
# h is a list.
# i is a boolean, which are logical values (true/false), often in conditions.
# j is a NoneType, which is representing the absence of a value or a null value.
# k is a list.
# l is a string.
# m is a float.

# HW Questions:
# I found 9 different data types.
# They are: int float complex str list dict tuple bool NoneType
# e, h, k are all lists. d and l are both strings. b and m are both floats.
# l is a string, because the command str() converts a value into a string.
# Another type is set.
n = {1,2,3}
print(n)
print(type(n)) # n is a set, an unordered collection of unique elements.

# --- Booleans ---
print(10 > 9)                 # True, 10 is greater than 9
print(10 == 9)                # False, 10 is not equal to 9
print(10 <= 9)                # False, 10 is not less than or equal to 9

print(bool("abc"))            # True, non-empty string will be true
print(bool(123))              # True, non-zero number will be true
print(bool(["apple", "cherry", "banana"])) # True, non-empty list will be true
print(bool(True))             # True, as expected 
print(bool(False))            # False, as expected
print(bool(0))                # False, zero will be false
print(bool(""))               # False, empty string will be false
print(bool(" "))              # True, a space is still a non-empty string which will be true
print(bool(()))               # False, empty tuple will be false
print(bool([]))               # False, empty list will be false
print(bool({}))               # False, empty dictionary will be false
print(bool(True and False))   # False, this is an 'and' expression where one of the options is False
print(bool(True and True))    # True, both are True
print(bool(False and False))  # False, both are False
print(bool(True or False))    # True, at least one is True
print(bool(True or True))     # True, both are True
print(bool(False or False))   # False, both are False
print(bool(not(False)))       # True, not False is True
print(bool(not(True)))        # False, not True is False

# HW Questions:
# Expressions returning True have logically correct or nonzero/non-empty values.
# Expressions returning False have logically incorrect, empty, or 0 values, or involve the False value.
# print(bool(" ")) was surprising because it looks like an empty string. But there is actually a space inside which makes it not empty.
# print(bool(1.2)) will return True because any nonzero float will also return True.
# print(bool(None)) will return False because there is no value.

# --- Operators ---
# 3.3.1 Arithmetic Operators
print(10 + 5)  # 15, + performs addition
print(10 - 5)  # 5, - performs subtraction
print(2 * 4)   # 8, * performs multiplication
print(6 / 3)   # 2.0, / performs division
print(5 % 2)   # 1, % performs modulus (gives remainder of division)
print(3 ** 2)  # 9, ** performs exponentiation (3^2)
print(15 // 2) # 7, // performs floor division (division rounded down)

# 3.3.2 Comparison Operators
print(5 == 2)   # False, == checks if values are equal
print(10 != 10) # False, != checks if values are not equal
print(2 < 5)    # True, < checks if left is less than right
print(12 > 5)   # True, > checks if left is greater than right
print(5 <= 6)   # True, <= checks if left is less than or equal to right
print(1 >= 10)  # False, >= checks if left is greater than or equal to right

# 3.3.3 Assignment Operators
x = 5          
x += 5         # x = x + 5, so x becomes 10
print(x)       # 10
x -= 4         # x = x - 4, so x becomes 6
print(x)       # 6
x *= 3         # x = x * 3, so x becomes 18
print(x)       # 18

# 3.3.4 Logical Operators
# 1. 'and' returns True only if both expressions are True
# print((1 == 1) and (2 == 2))  returns True
# print((1 == 1) and (2 != 2))  returns False

# 2. 'or' returns True if at least one expression is True
# print((1 == 1) or (1 == 2))   returns True
# print((1 == 2) or (1 == 3))   returns False

# 3. 'not' reverses the true/false value
# print(not (1 == 2))  returns True
# print(not (1 == 1))  returns False

# More Questions:
# 1. / performs division and returns a float
#    // performs floor division and returns the quotient rounded down to nearest integer

# 2. % returns the remainder of division
#    // returns the quotient (rounded down)

# 3. I would use % operator.
# For example: print(10 % 3) returns 1

# 4. Assignment operators perform an operation on a variable and then assign the result back to that variable.

# --- Strings ---
my_string = "hello"
print(my_string)          # Prints: hello
print(my_string[0])       # Prints: h (first character)
print(my_string[1])       # Prints: e (second character)
print(my_string[2])       # Prints: l (third character)
print(my_string[3])       # Prints: l (fourth character)
print(my_string[4])       # Prints: o (fifth character)
print(my_string[-1])      # Prints: o (last character)
print(my_string[1:3])     # Prints: el (characters from index 1 up to but not including 3)
print(my_string[0:5:2])   # Prints: hlo (characters from index 0 to 4, stepping by 2)
print(len(my_string))     # Prints: 5 (length of the string)
print(my_string + "goodbye")  # Prints: hellogoodbye (string concatenation)
print(7 * my_string)          # Prints: hellohellohellohellohellohellohello (string repeated 7 times)

# Questions:
# 1. Slicing extracts a portion of the string. I performed this in mutations 8 and 9, my_string[1:3] and my_string[0:5:2]

# 2. It prints "Hello, my name is Oski"
#    The comma separates strings, so "Hello, my name is" and name are printed with a space in between
name = "Oski"
print("Hello, my name is", name)

# 3. It also prints "Hello, my name is Oski"
name = "Oski"
print(f"Hello, my name is {name}")

# 4. The second expression uses an f-string. The expression inside {} is evaluated and inserted into the string directly.

# --- Terminal Commands ---
# 1. cd
# Changes directories. Use to move from current folder to another.
# Example: cd Desktop

# 2. ls
# Lists files and directories in the current directory.
# Example: ls

# 3. ls -a
# Lists all files including hidden files (those starting with a dot).
# Example: ls -a

# 4. mkdir
# Creates a new directory (folder).
# Example: mkdir new_folder

# 5. cat
# Displays the contents of a file.
# Example: cat datatypes.py

# 6. pwd
# Prints the current working directory path.
# Example: pwd

# 7. cd ..
# Moves up one directory level (to the parent directory).
# Example: cd ..

# 8. cd .
# Stays in the current directory (represents current directory).
# Example: cd .

# 9. cd ~
# Moves to the home directory.
# Example: cd ~

# 10. cp
# Copies files or directories.
# Example: cp hw1_folder.png new_folder

# 11. mv
# Moves or renames files or directories.
# Example: mv oldname.py newname.py

# 12. rm
# Removes/deletes files.
# Example: rm file.py

# 13. clear
# Clears the terminal screen.
# Example: clear

# 14. grep
# Searches for a specific pattern or text inside files.
# Example: grep "hello" homework1.py

# Questions:
# 1.
# a) touch: Creates an empty file or updates existing file.
# Example: touch newfile.py

# b) head: Displays the first few lines of a file.
# Example: head datatypes.py

# c) tail: Displays the last few lines of a file.
# Example: tail datatypes.py

# 2. ls -a shows hidden files as well, while ls only shows visible files.

# 3. A hidden file is a file which has a name starting with a dot, making it invisible in normal directory listings.

# 4.
# a) -l (long listing): Shows detailed information about files.
# Example: ls -l

# b) -r (reverse): Reverses the order of the output.
# Example: ls -r

# c) -i (show inode): Shows the inode number of files.
# Example: ls -i
print(type([]))