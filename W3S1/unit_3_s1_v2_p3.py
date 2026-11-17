'''
You are given a string schedule representing the lineup of shows on a streaming platform, where each character in the string represents a different show. A duplicate removal consists of choosing two adjacent and equal shows and removing them from the schedule.

We repeatedly make duplicate removals on schedule until no further removals can be made.

Return the final schedule after all such duplicate removals have been made. The answer is guaranteed to be unique.

def remove_duplicate_shows(schedule):
  pass
Example Usage:

print(remove_duplicate_shows("abbaca")) 
print(remove_duplicate_shows("azxxzy")) 

Understand:
    Input: a string, schedule
    output: a string, schedule

Plan:
    initialize a stack. 
    for each character in the string, peek the stack. if the peek is equal to the current character, then pop that off the stack, and skip to the next character. else, push current character onto the stack. 
    then, use the join method to pop everything off into a string, which we return.

'''
def remove_duplicate_shows(schedule):
  stack = []
  for char in schedule:
    if stack and stack[-1] == char:
      stack.pop()
    else:
      stack.append(char)
  result = "".join(stack)
  return result

print(remove_duplicate_shows("abbaca")) 
print(remove_duplicate_shows("azxxzy")) 