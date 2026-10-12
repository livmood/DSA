'''
understand:
input: 2 strings
output: 1 int
edge cases: empty string: return 0, None input: return None
plan:
initialize count int
initialize a set for endangered
convert endangered to set
iterate through observed species
check if each character is in endangered
if it is, count += 1
return count


implement:

As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.
'''
def count_endangered_species(endangered_species, observed_species):
    if len(endangered_species) == 0 or len(observed_species) == 0:
        return None
    count = 0
    endangered_set = set()
    for c in endangered_species:
        endangered_set.add(c)
    for c in observed_species:
        if c in endangered_set:
            count += 1
    return count
# Example Usage:

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  

