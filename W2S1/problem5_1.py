'''
As part of the festival, attendees cast votes for their favorite set. Given a dictionary votes that maps attendees id 
numbers to the artist they voted for, return the artist that had the highest number of votes. 
If there is a tie, return any artist with the top number of votes.

Understand:
    Input: dictionary (key: attendee_id (number), value: artist (string))
    Output: artist (string)
    Edge Cases: there is a tie, dictionary is empty

Plan: 
    create a dictionary voteRecord => (key: artistName (string), value: number of votes (number))
    loop through the input dictionary and for every value, check if the value exists as a key in the dict. if it is, 
        increment current value at that key
    else, 
        insert that value as a key and set the value of that key to 1
    then, initialize a counter called current_max to 0
    loop through the voteRecord dictionary, comparing each value to current_max. if greater than current_max,  


def best_set(votes):
    pass
Example Usage:

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))
Example Output:

SZA
Ethel Cain
Note: SZA and Ethel Cain would both be acceptable answers for the second example

'''


'''
Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. However, 
for a special feature, you need to reverse the order of comments before displaying them. 
Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']
'''
# 
# input: queue
# output: stack
# edge case: empty string
# if empty return empty stack
# create stack
# loop through queue
# pop from right
# add popped element to stack
# return stack
'''
def reverse_comments_queue(comments):
    if not comments:
        return []
    
    stack = []
    
    while comments:
        popped = comments.pop()
        stack.append(popped)
    return stack
    
    
print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
'''

'''
TASK 3: 

As part of a new feature on your social media platform, you want to highlight post titles 
that are symmetrical, meaning they read the same forwards and backwards 
when ignoring spaces, punctuation, and case. Given a post title as a string, 
use a new algorithmic technique the two-pointer method to determine if the 
title is symmetrical.

def is_symmetrical_title(title):
  pass
Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
Example Output:

True
False

Understand: 
Input: str 
Output: boolean 
checking if it is symmetrical 
"ASantaatNASA"

Plan: 
 make str lowercase and remove spaces and punctuation, so it is easier to check 
 edge cases: 
    - empty str --> return None 
    - not equal --> return False
    
# Two pointers
# left at the first character
# right at the last one
# while left < right loop
# if left and right have same character
# left += 1, right -= 1
# at any time its not equal return False
# return True at end of loop

Implement: two-pointer

text.replace(" ", "")
cleaned = ''.join(filter(str.isalnum, text)) 

'''
'''
def is_symmetrical_title(title):
    t = title.lower() 
    cleanedTitle = ''.join(filter(str.isalnum, t))
    leftPtrIndx = 0
    rightPtrIndx = len(cleanedTitle)-1
    while(leftPtrIndx < rightPtrIndx):
        if(cleanedTitle[leftPtrIndx] != cleanedTitle[rightPtrIndx]):
            return False
        leftPtrIndx += 1
        rightPtrIndx -= 1
    return True
print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

'''


'''
Understand: 
    Input: string of lowercase and uppercase letters
    Output: string of letters without adjacent duplicate letters where the only difference is case
    Edge Cases: empty string or string with only one letter is base case
        must work on string that only contains adjacent duplicate letters where the only difference is case
Plan:
    loop through string, check if each char is lowercase
        if yes, push onto stack
        if no, pop the stack and check if current char .lower == popped 
            if this is false, push them back onto the stack
    at the end, pop everything off stack and add it to a string
    return the reversed string
I mean I can if you don't want to I was just asking cuz I did the last one
You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase English letters, you want to remove any pairs of adjacent characters where one is the lowercase version of a letter and the other is the uppercase version of the same letter. Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.
'''


def clean_post(post):
    stack = []
    stack.append("")
    
    for char in post:
        if char == char.lower():
            stack.append(char)
        elif char != char.lower():
            popped = stack.pop()
            if char.lower() != popped:
                stack.append(popped)
                stack.append(char)
    newStr = ''.join(stack)
    return newStr
                
                
            


print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 
'''
Example Output:

post

s
'''