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

def get_names(spicy_foods):
    spicy_food_names = []
    for spicy_food in spicy_foods:
        if 'name' in spicy_food:
            spicy_food_names.append(spicy_food['name'])
    return spicy_food_names
  
def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if 'heat_level' in food and isinstance(food['heat_level'], int) and food ['heat_level'] > 5:
            spiciest_foods.append(food)
    return spiciest_foods
    
 


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name', 'Unknown')
        cuisine = food.get('cuisine', 'Unknown')
        heat_level = food.get('heat_level', 0)

        emoji_heat_level = "🌶" * heat_level

        print(f"{name} ({cuisine}) | Heat Level: {emoji_heat_level}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food.get('heat_level')
        name = food.get('name')
        cuisine = food.get('cuisine')
        emoji_heat_level = "🌶" * heat_level

        if heat_level > 5:
            print(f"{name} ({cuisine}) | Heat Level: {emoji_heat_level}")


def get_average_heat_level(spicy_foods):
    all_heat_levels = []
    for food in spicy_foods:
        heat_level = food.get('heat_level')
        all_heat_levels.append(heat_level)
    return sum(all_heat_levels) / len(all_heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
