'''
Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars as a parameter and multiplies each element in the list by two. Return the doubled list.

def doubled(hunny_jars):
	pass
Example Usage

hunny_jars = [1, 2, 3]
doubled(hunny_jars)
Example Output:

[2, 4, 6]
'''

def doubled(hunny_jars):
    for indx in range(len(hunny_jars)):
        hunny_jars[indx] = hunny_jars[indx] * 2
    return hunny_jars

hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))