'''
You are designing an app for your festival to help attendees have the best experience possible! As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    pass
Example Usage:

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
Example Output:

{'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
{'message': 'Artist not found'}

 U 
    - Input: Name of the artist we're tryna find in the festival schedule 
    - Output: Dictionary that shows the schedule of the artist we're tryna find
    - Edge Cases: the artist isn't found. Empty festival schedule.

 P
    - Loop through the dictionary 
    - check if the key matches with the artist's parameter 
        - if the key does match we return value of that key
        - else we show error after looping through entire dictionary
'''

def get_artist_info(artist, festival_schedule):
    for schedule_artist, schedule in festival_schedule.items():
        if schedule_artist == artist:
            return schedule
    return {"message": "Artist not found"}

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
