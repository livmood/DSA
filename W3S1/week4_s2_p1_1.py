'''
Your day consists of various tasks, each requiring a certain amount of time. To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available. You need to identify if there is a pair of tasks whose combined time matches the available slot.

Given a list of integers representing the time required for each task and an integer representing the available time slot, write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Understand:
    Input: a list of integers
    Output: a boolean

Implement:
    for each time in task_times, check is available_time minus current time in subset of array from current index + 1 to end
        if yes, return True
    at end of loop, return False
    the time complexity of checking if soemthing is in the subset is o(n) and we check n times so time complexity is o(n^2)
    the space complexity is o(1) because we are not storing anything

def find_task_pair(task_times, available_time):
  pass
Example Usage:

task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))
Example Output:

True
True
False
'''
def find_task_pair(task_times, available_time):
    for timeIndx in range(len(task_times)):
        if available_time - task_times[timeIndx] in task_times[timeIndx+1:]:
            return True
    return False

task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))