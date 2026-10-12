'''
Understand:
inputs: species_list: list of dictionaries
    where each dictionary has kv pairs name (string), habitat (string), population (number)
output
    name (string) with lowest population
edge cases:
    species_list is empty -> None
    return lowest index when multiple species are habe lowest population
    check for negative population
Plan:
if length of species_list is 0, return None
set minimum_name to first species_list element's name
set minimum to first species_list element's population
from second species to end of species_list
if current species population is less than minimum
    set minimum_name to current name
    set minimum to current population
return minimum_name

Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.
'''
def most_endangered(species_list):
    if len(species_list) == 0:
        return None
    minimum_name = species_list[0]["name"]
    minimum_population = species_list[0]["population"]
    for current_species in species_list:
        if current_species["population"] < minimum_population:
            minimum_population = current_species["population"]
            minimum_name = current_species["name"]
    return minimum_name
# Example Usage:


species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

print(most_endangered(species_list))
