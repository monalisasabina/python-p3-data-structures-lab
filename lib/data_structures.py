spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

spicy_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }

# should return a list of strings with the names of each spicy food
def get_names(spicy_foods):
    
    return [food["name"] for food in spicy_foods]

print(get_names(spicy_foods))


# returns a list of dictionaries where the heat level is greater than 5
def get_spiciest_foods(spicy_foods):
    
      return [food for food in spicy_foods if food["heat_level"] > 5]

print(get_spiciest_foods(spicy_foods))



# output to the terminal each spicy food 
def print_spicy_foods(spicy_foods):
    
    for food in spicy_foods:

        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')
    
print_spicy_foods(spicy_foods)


# takes a list of spicy foods and a string represesnting a cuisine and
# returns a single dictionary for the spicy foods whose cuisine matches
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
     
     for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

print(get_spicy_food_by_cuisine(spicy_foods,"American"))


# takes a list of spicy_foods and outputs to the terminal ONLY foods that
# have heat level greater than 5
def print_spiciest_foods(spicy_foods):

    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    # return spiciest_foods

print(print_spiciest_foods(spicy_foods))    


# takes a list of spicy-food and return an integer representing the average 
# representing the average heat level of all array
def get_average_heat_level(spicy_foods):

    print([food["heat_level"] for food in spicy_foods])
    
    return sum([food["heat_level"] for food in spicy_foods]) /len(spicy_foods)

print(get_average_heat_level(spicy_foods))


# takes a list of spicy_foods and a new spicy_food and returns the original
# list with the new spicy_food
def create_spicy_food(spicy_foods, spicy_food):
     
     spicy_foods.append(spicy_food)

     return spicy_foods

print(create_spicy_food(spicy_foods, spicy_food))
    
