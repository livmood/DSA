'''
Problem Set Version 1
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted.
 Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. 
 You are given a string representing a post's content, and 
 your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
def is_valid_post_format(posts):
  pass
Example Usage:

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
Example Output:

True
True
False

Understand:
    Input: String of tags
    Output: Boolean, True or False

Plan:
    Initialize a dictionary where the keys are closing tags and the values are corresponding open tag.
    Initialize a stack
    We're gonna loop through the input string, and check:
        is the current character in the values?
            if yes, append it to our stack
        if no, check is there something in our stack
            if no, return false
            if yes, pop  it off and check, is dict[char] == popped item?
                if no, return false
            

We're gonna return the length of the set
'''
def is_valid_post_format(posts):
    tags = {']':'[', ')':'(', '}':'{'}
    stack = []
    for char in posts:
        if char in tags.values():
            stack.append(char)
        elif stack and tags[char] != stack.pop():
            return False
    return len(stack) == 0

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))