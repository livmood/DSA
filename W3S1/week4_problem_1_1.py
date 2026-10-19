'''
You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.

Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Understand:
    Input: list of dictionaries
    Output: list of strings

Plan:
    create a result list
    loop through the list of dictionaries
        for every dictionary, add the dict.name to result list
    return result list
    Notes: Do not need to check before adding dict.name since problem specifies that each dictionary contains information such as name.
    The runtime of this solution is o(n), since we are looping through our list of n dictionaries once
    The space complexity is also o(n) since we are storing only n names in our result list

def extract_nft_names(nft_collection):
    pass
Example Usage:

def extract_nft_names(nft_collection):
    pass

Example Output:

['Abstract Horizon', 'Pixel Dreams', 'Future City']
['Crypto Kitty', 'Galactic Voyage']
['Golden Hour']

'''
# Implementation:

def extract_nft_names(nft_collection):
    result = []
    for nft in nft_collection:
        result.append(nft['name'])
    return result

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))