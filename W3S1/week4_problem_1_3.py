'''
You have been tasked with identifying the most popular NFT creators in your collection. A creator is considered "popular" if they have created more than one NFT in the collection.

Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Understand:
    Input: a list of dictionaries
    output: a list of strings

Plan:
    initialize a dictionary where the key is creator name and the value is the number of times they show up in the collection
    initialize a result list of strings
    loop through the list of nft dictionaries
        for every nft dictionary, check, is the creator_name in our creator_dictionary?
            if yes, is the value = 1?
                if yes, add the name to our list. then increment the value at that creator_name in creator_dict.
                thus, the only case where our creator_name is in creator_dictionary and the value is not 1 is when the value is greater than 1, which implies we have already added it to our list
            if no, then add creator_name to our creator_dictionary and set the value to 1
    return the result list

def identify_popular_creators(nft_collection):
    pass
Example Usage:

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
Example Output:

['ArtByAlex']
['SpaceArt']
[]
'''
def identify_popular_creators(nft_collection):
    creator_dict = {} # creator_name : int >= 1
    result = []
    for nft in nft_collection:
        if nft['creator'] in creator_dict:
            if creator_dict[nft['creator']] == 1:
                result.append(nft['creator'])
                creator_dict[nft['creator']] += 1
        else:
            creator_dict[nft['creator']]=1
    return result

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))