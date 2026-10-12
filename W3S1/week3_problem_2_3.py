'''
Understand:
inputs: 
    a string of letters with length 26 and a string, (observations) representing the order in which you move
output: 
    an int (time)
edgecases: 
    observations string is empty

Plan: 
    initialize a dictionary
    iterate through the station_layout string and put each character into a dictionary as a key and its index in the string as a value
    initialize running total to 0
    iterate through the string observations and at the current character we look up the value from the dictionary and compare it to the next character's value from the dictionary
        we have a running total and we add the absolute difference between those two values
        keep out of bounds error in mind when creating for loop
    return the running total



In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). To make observations in a specific order represented by a string observations, you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.

Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.
'''
def navigate_research_station(station_layout, observations):
  layout_key = {}
  for current_char_index in range(len(station_layout)):
    # print("current char index: ", str(station_layout[current_char_index]), str(current_char_index))
    layout_key[station_layout[current_char_index]] = current_char_index
  running_total = layout_key.get(observations[0])
  for current_observation in range(len(observations)-1):
    if(layout_key.get(observations[current_observation]) > layout_key.get(observations[current_observation+1])):
        running_total += layout_key.get(observations[current_observation]) - layout_key.get(observations[current_observation+1])
    else:
       running_total += layout_key.get(observations[current_observation+1]) - layout_key.get(observations[current_observation])
  return running_total


# Example usage:
station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))
'''

Example Output:

45
4
Example 2 explanation: The index moves from 0 to 2 to observe 'c', then to 1 for
'b', then to 0 again for 'a'.
Total time = 2 + 1 + 1 = 4.

'''