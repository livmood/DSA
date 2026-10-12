'''
Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    pass
Example Usage:

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
Example Output:

{"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
{}

U
    - Input: 2 StrLists, artists and set_times
    - Output: dict with key = artists, value = set_times
    - Empty lists

P
    -  Create a dict
    -  Check if either is empty, return dict
    -  For loop, counter < len(list), increment counter
        - Insert key at artist[counter] and value at set_times[counter]
    -  Return dict

'''

def lineup(artists, set_times):
    dict = {}

    counter = 0
    while counter < len(artists):
        dict[artists[counter]] = set_times[counter]
        counter += 1

    return dict

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))
