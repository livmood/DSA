print("This is the print function!")

string_example = "this is an example string"

print(string_example) # this also works

len(string_example) # should be 25

range(start, stop, step) # start is inclusive, stop is exclusive, step is the increment

sum([1, 2, 3, 4]) # accepts a list of numbers, returns the sum of all values in the list

min([1, 2, 3, 4]) # accepts a list of numbers or strings. returns min number. for characters, returns the one with the lowest ASCII value. (characters closer to 'a' are smaller than those closer to 'z')
    min(["banana", "apple", "watermelon"], key=len) # would return apple bc it has only 5 characters. 
    as long as key is set equal to a function, it evaluates the function on each item in the list and then compares them with the less than operator (<)
max([1, 2, 3, 4]) # does opposite of min, compares with greater than operator (>)

### List Methods
lst.append(item) # addsan item to the end of a list
fruit = ["pear", "plum", 'peach']
fruit.append("cherry")

lst.sort() # sorts the list in ascending order
lst = [4, 2, 1, 3]
lst.sort()
print(lst) # prints [1, 2, 3, 4]

s.lower() # returns s as a lower case string
s = "Hello World!" # now running line 28 would give "hello world"

string_example.split(" ") # returns a list of the substrings, so ["this", "is", "an", "example", "string"]

seperator = "."
lst = ["example", "email", "domain", "com"]
joined = seperator.join(lst) # example.email.domain.com

str = "bananna"
newStr = str.strip("n") # if no value is specified, whitespace is removed from beginning and end of str
print(newStr) # prints baaa

* in python, variables don't needa be declared using a keyword. simply write a name and assign a value to it
* variable names use snake case and should have underscores between words
* variable types can change upon reassignment.
* use if, elif and else for conditionals
* functions are defined using the def keyword
* use the return keyword. by default functions return None
* use f-strings to insert variable expressions into python strings:

name = "Michael"
print(f"Welcome to Codepath, {name}!")


