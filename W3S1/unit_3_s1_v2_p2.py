'''
You are given a list watchlist representing a list of shows sorted by popularity for a particular user. The user wants to discover new shows they haven't heard of before by reversing the list to show the least popular shows first.

Using the two-pointer approach, implement a function reverse_watchlist() that reverses the order of the watchlist in-place. This means that the first show in the given list should become the last, the second show should become the second to last, and so on. Return the reversed list.

Do not use list slicing (e.g., watchlist[::-1]) to achieve this.

def reverse_watchlist(watchlist):
  pass
Example Usage:

watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]

print(reverse_watchlist(watchlist))

Understand:
    input: a list watchlist
    output: a list, watchlist, reversed

Plan:
    have two pointers, one at the end and one at the start
    have temp variable. set it to value at start pointer. set start pointer to value at end pointer. set end pointer to value in temp variable. 
    increment start pointer. decrement end pointer.
    repeat until start pointer is equal to or greater than end pointer
'''

def reverse_watchlist(watchlist):
  start = 0
  end = len(watchlist)-1
  while start < end:
    temp = watchlist[start]
    watchlist[start] = watchlist[end]
    watchlist[end] = temp
    start+=1
    end-=1
  return watchlist

watchlist = ["Breaking Bad", "Stranger Things", "The Crown", "The Witcher"]

print(reverse_watchlist(watchlist)) 