#File: homework1.py

# --- Variables and Data Types ---

a = 10
print(type(a)) #int: integers, no decimal points

b = 1.5
print(type(b)) #float: decimal (floating-point) numbers

c = 3j
print(type(c)) #complex: complex numbers -- numbers with a real and imaginary part

d = "hello"
print(type(d)) #str: strings -- sequences of characters used to store text

e = [1, 2, 3]
print(type(e)) #list: used to store multiple values in a single variable

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(type(f)) #dict: dictionary -- stores data as key-value pairs

g = (1, 2)
print(type(g)) #tuple: used to store multiple values in a single, ordered collection

h = ["apple", "banana", "strawberry"]
print(type(h)) #list: used to store multiple values in a single variable
 
i = True
print(type(i)) #boolean: represents True or False values

j = None
print(type(j)) #NoneType: type of the special value None -- "no value" or "nothing"

k = [True, "blue", 12]
print(type(k)) #list: used to store multiple values in a single variable

l = str(14)
print(type(l)) #str: strings -- sequences of characters used to store text

m = 1e4
print(type(m)) #float: decimal (floating-point) numbers


''' Questions: 
1. 9 data types
2. int, float, complex, str, list, bool, NoneType, dict, tuple
3. b and m are bouth float, d and l are both strings, e and h and k are all lists
4. Data type of l is str, and it is not an integer because str() typecasted 14 to a string 
5. Another data type: set -- unordered collection of unique items, written using {} or the set() function '''

# --- Booleans ---
print(10 > 9) #True
print(10 == 9) #False
print(10 <= 9) #False
print(bool("abc")) #True
print(bool(123)) #True
print(bool(["apple", "cherry", "banana"])) #True
print(bool(True)) #True
print(bool(False)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(" ")) #True
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print(bool(True and False)) #False
print(bool(True and True)) #True
print(bool(False and False))
print(bool(True or False)) #True
print(bool(True or True)) #True
print(bool(False or False)) #False
print(bool(not(False))) #True
print(bool(not(True))) #False

''' Questions
1. Expressions that return True includes numbers, strings, non-empty, sets, and if both are True for "and" statements and if one is True for "or" statements. Everything else returns False.
2. bool("") and bool(" ") surposed me about their results, because there's a space in the second one, but that changes the truth value.
3. bool(5 == 5) is true becuase 5 is indeed equal to 5.
5. bool(not(not(False))) is False, because not(False) is True, and not(True) will go back to False. '''

# --- Operators ---
print(10 + 5) #15, addition
print(10 - 5) #5, subtraction
print(2 * 4) #8, multiplication with integers
print(6 / 3) #2.0, Python always performs floating-point division even if result is whole number
print(5 % 2) #1, modular, so it returns remainder of 5/2
print(3 ** 2) #9, exponential equation, 3 * 3
print(15 // 2) #7, the floor division operator divides 15 and 2 and rounds down to nearest whole number
print(5 == 2) #False, because 5 is not equal to 2
print(10 != 10) #False, because 10 is equal to ten, and the not reverses it
print(2 < 5) #True, because 2 is less than 5
print(12 > 5) #True, because 12 is greater than 5
print(5 <= 6) #True, because 5 is less than or equal to 6
print(1 >= 10) #False, because 1 is not greater than or equal to 10

x = 5
x += 5
x -= 4
x *= 3

'''Questions:
1. "and" operator returns True if all booleans in the statement are True. bool(True and True) would return True, and bool(True and False) would return False.
2. "or" operator returns True is one boolean in the statement is True. bool(True or True) would return True, and bool(False or False) would return False.
3. "not" reverses the truth statement. bool(!False) would return True, and bool(!True) would return False.

More Questions:
1. / is a floating-point division, which returns a float with decimal points. // is floor division, which rounds the answer down to the nearest integer. 
2. % is mod, which returns the remainder when you divide two numbers. // returns the answer, but rounded down.
3. You would use 5 to calculate the remainder. For example, 5 % 2 = 1.
4. For assignment operators, you essentially store a value in a variable, and you can perform other operations on the variable. This is more flexible, where you can assign or store any values into  the variables. 
'''


# --- String ---
my_string = "hello"
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[-1])
print(my_string[1:3])
print(my_string[0:5:2])
print(len(my_string))
print(my_string + "goodbye")
print(my_string * 7)

name = "Oski"
print("Hello, my name is", name)

name = "Oski"
print(f"Hello, my name is {name}")

'''Questions:
1. Slicing is cutting out part of the sequence without changing the original. my_string[1:3] and my_string[0:5:2] are examples of slicing.
2. Hello, my name is Oski
3. Hello, my name is Oski
4. The first print statement is the comma method, where it takes multiple arguments separated by commas and automatically adds a space between each argument when printing.
The second print statement is an example of f-string, where inside the {}, Python replaces the variable with its value.
'''

# --- Terminal Commands ---

# cd
# change directories: use it to move from one folder to another
# ex. cd Downloads

# ls
# list: lists the files and directories in the current folder
# ex. ls

# ls -a
# lists all file sand directories in the current folder, including hidden files
# ex. ls -a

# mkdir
# Make directory: creates a new folder in the current directory
# ex. mkdir homework2

# cat
# concatenate: originally used to combine files, but now mostly used to view file contents
# ex. cat hw.py

# pwd
# Print working directory: displays full path of the folder you are currently in in the terminal
# ex. pwd homework1.py

# cd ..
# change directory to one directory above in the folder hierarchy
# ex. cd .. moves from homework1 to joyce

# cd .
# change directory to the current one, so you don't actually change directories
# ex. cd .

# cd ~
# change directory to home directory
# ex. cd ~

# cp
# copy: copy files or directories
# ex. cp homework1.py lab00.py

# mv
# move: move or rename files and directories
# ex. mv lab00.py /home/joycexu/Downloads

# rm
# remove: remove/delete files or directories
# ex. rm homework2

# clear
# clear the screen
# ex. clear

# grep
# global regular expression print: search for text patterns inside files or output
# ex. let file.txt contain {apple, banana, orange, peach}
#     grep "an" file.txt outputs banana orange


'''Questions:
1. 
touch: creates a new empty file or updates the timestamp of an existing file
ex. touch newFile.py
head: shows the first few lines of a file
ex. head -n 3 homework.py
tail: shows the last few lines of a file
ex. tail homework.py
2. ls prints the working directories but doesn't show the hidden ones while ls -a prints the hidden ones as well.
3. A hidden file is a file that is not normally visible whne you list the files in a direclty, and they are hidden to prevent accidental modification or deletion of important stuff.
4. 
-f: force -- forces an action without asking for confirmation
ex. rm -f homework2.py
-r: recursive -- applies a command to a directory and all its contents
ex. cp -r joyce
-i: make a command interactive -- ask for confirmation before performing an action
ex. rm -i homework2.py

'''