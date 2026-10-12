'''
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, implement a 
function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule 
each mapping the artists playing at the venue to their set times. 
Return a dictionary containing the key-value pairs that are the same in each schedule.

def identify_conflicts(venue1_schedule, venue2_schedule):
    pass
Example Usage:

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
Example Output:

{"Stromae": "9:00 PM", "HARDY": "7:00 PM"}

Understand
    - Input: 2 dicts, venue1 and venue2 scheudles
    - Output: 1 dict, match schedule (duplicate from 2 dict input)
    - Edge Cases:
        - Either is empty
        - One is longer than the other

Plan
    - Init an empty conflict_dict
    - For loop key in first dict
        - Check for key in second dict
        - If key exist, check for value match
            - If match, insert to conflict_dict
    - Return conflict_dict
'''

def identify_conflicts(venue1_schedule, venue2_schedule):
    conflict_dict = {}
    
    for key in venue1_schedule:
        if venue2_schedule[key] != None:
            if venue2_schedule.get(key) == venue1_schedule.get(key):
                conflict_dict[key] = venue1_schedule.get(key)

    return conflict_dict

venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))
