import math

# Absolute value

print("Absolute Value", abs(-100))

# python3 Ceiling, floor, round

print("math ceiling", math.ceil(1.5))
print("math.floor: ", math.floor(1.5))
print("round:", round(1.5))

# Max/min

print('Max 100,50', max(100,50))
print('Min 100,50', min(100,50))

# If else

some_number = 3

if some_number == 1:
    print("number is 1")
elif some_number == 2:
    print("number is 2")
elif some_number == 3:
    print("number is 3")
else:
    print("?")

# Ternary

x = 2
y = 3

print("'even' if x % 2 == 0 else 'odd'", 'even' if x % 2 == 0 else 'odd')
print("'odd' if y % 2 == 0 else 'odd'", 'even' if y % 2 == 0 else 'odd')

# Exceptions
try: 
    foo()
except NameError:
    print('foo is not defined')

# Continue break

for number in range(1,10):
    if number == 3:
        print("Fizz")
        continue
    if number == 5:
        print("Buzz")
        break
    print(number)

# Length 
len_string = "abcd"

print(len(len_string))

# Interpolation
hello = "hello"
print(f"{hello} World")

# Multiline

multi = """
Line 1
Line 2
Line 3
"""

print("multiline", multi)

# String to integer
string_1 = "1"
number_1 = int(string_1)

print('String to integer', number_1)

# Contains
if "2" in "123":
    print("2 is in the string")

if "2" not in "456":
    print("2 is not in the string")

# Substring
some_str = "012345"
print('print 234 from 012345', some_str[2:5])

# Join

some_list = ['a','b','c']
print(",".join(some_list))

# Strip

strip_string = "   abc   "
print(strip_string.strip())

# Split
abc_string = "a,b,c"
abc_strip_list = abc_string.split(',')

print("abc_strip_list[0]", abc_strip_list[0])
print("abc_strip_list[1]", abc_strip_list[1])
print("abc_strip_list[2]", abc_strip_list[2])

# Replace 

replace_str = "a b c d e"
print("replace", replace_str.replace(" ",","))

# regex match

import re

if re.search(r"\d", "iphone 8"):
    print('theres is a number')
if not re.search(r"\d", "iphone x"):
    print("there is no number")

# iteration
iteration_list = [1,2,3]

for item in iteration_list:
    print(item)

# Enumerate
enumerate_list = [4,5,6,7,8]

for i, item in enumerate(enumerate_list):
    print(f"{i} {item}")

print(list(enumerate(enumerate_list)))
# [(0, 4), (1, 5), (2, 6), (3, 7), (4, 8)]

# Contains

if 2 in [1,2,3]:
    print('2 is in the list')

if 2 not in [4,5,6]:
    print('2 is not in the list')

# reverse
rev_list = [1,2,3,4,5,6]

reverse_list = list(reversed(rev_list))

for item in reverse_list:
    print(f"{item}")

for item in reversed(rev_list):
    print(f"{item}")

# Range iteration

for i in range(4):
    print(i)

for i in range(4,8):
    print(i)

for i in range(6,3,-1):
    print(i)

# Append with modification

append_list = [1,2]

append_list.append(3)

for i in append_list:
    print(i)

# Append without modification
original_list = [1,2]
new_list = [*original_list, 3]
original_list[0] = 5

for i in new_list:
    print(i)

# Extend with Modification

extend_list = [1]
extend_list.extend([2,3])
for i in extend_list:
    print(extend_list)

