'''
There are n users in a queue waiting to stream their favorite movies, where the 0th user is at the front of the queue and the (n - 1)th user is at the back of the queue.

You are given a 0-indexed integer array movies of length n where the number of movies that the ith user would like to stream is movies[i].

Each user takes exactly 1 second to stream a movie. A user can only stream 1 movie at a time and has to go back to the end of the queue (which happens instantaneously) in order to stream more movies. If a user does not have any movies left to stream, they will leave the queue.

Return the time taken for the user at position k (0-indexed) to finish streaming all their movies.

def time_required_to_stream(movies, k):
  pass
Example Usage:

print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0))

Understand:
    Input: array containing integers, and an integer k representing an index
    Output: an integer representing time
    Edge cases: k is larger than n, index is out of bounds

Plan:
    lets implement this using a queue.
    


'''
from collections import deque
def time_required_to_stream(movies, k):
  queue = deque()
  count = 0
  for i in range(len(movies)):
    queue.append((i, movies[i]))
  while queue:
    currMovie = queue.popleft()
    if currMovie[0] == k and currMovie[1] == 1:
      return count+1
    elif currMovie[1] > 0:
      queue.append((currMovie[0], currMovie[1]-1))
      count+=1
      


print(time_required_to_stream([2, 3, 2], 2))
print(time_required_to_stream([5, 1, 1, 1], 0)) 
