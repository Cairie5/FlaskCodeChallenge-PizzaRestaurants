# seed.py

from app import app
from random import randint, choice as rc, sample # Import the random module
from models import db, Restaurant, Pizza, RestaurantPizza, app
from faker import Faker

# List of random restaurant names
restaurant_names = [
    "Spice Delight Cafe",
    "The Hungry Palate Bistro",
    "Fusion Flavors Grill",
    "Cozy Corner Eats",
    "Taste of Tuscany Trattoria",
    "The Urban Garden Cafe",
    "Savory Spice Kitchen",
    "Seafood Sensations Shack",
    "The Rustic Rooster Diner",
    "Flavor Fusion Bistro",
    "Street Food Safari",
    "Sushi Samurai House",
    "The Gourmet Galley",
    "Fireside Grill & Tavern",
    "Mediterranean Breeze Bistro",
    "The Wholesome Plate",
    "Harborview Oyster Bar",
    "Crisp & Crave Creperie",
    "The Spicy Noodle Hut",
    "Farm-to-Table Feastery",
    "El Paso Enchilada Express",
    "Sweet Serenity Bakery",
    "The Bamboo Garden",
    "Urban Elegance Eatery",
    "Taste of India Palace",
    "Pizza Perfection Parlor",
    "Spice Route Kitchen",
    "The Blue Bayou Bistro",
    "Crispy Crust Pizzeria",
    "Zen Garden Sushi Lounge"
]

# List of random restaurant ingredients
restaurant_ingredients = [
    "Fresh Basil Leaves",
    "Aged Balsamic Vinegar",
    "Roasted Red Peppers",
    "Gourmet Truffle Oil",
    "Goat Cheese Crumbles",
    "Wild Mushroom Blend",
    "Sun-Dried Tomatoes",
    "Crispy Bacon Bits",
    "Caramelized Onions",
    "Pineapple Chunks",
    "Szechuan Peppercorns",
    "Blackened Cajun Spice",
    "Mango Salsa",
    "Jalapeño Pepper Rings",
    "Dijon Mustard",
    "Blue Cheese Dressing",
    "Sweet Chili Sauce",
    "Toasted Almond Slivers",
    "Pickled Ginger",
    "Sriracha Mayo",
    "Pesto Sauce",
    "Candied Walnuts",
    "Artichoke Hearts",
    "Honey Glazed Ham",
    "Smoked Paprika",
    "Lemon Zest",
    "Horseradish Cream",
    "Kimchi",
    "Capers",
    "Garam Masala"
]

fake = Faker()

with app.app_context():
        # Create some restaurants with random names
        db.session.query(Restaurant).delete()
        db.session.query(RestaurantPizza).delete()
        db.session.query(Pizza).delete()
    
        restaurants = []
        for i in range(100):
           r = Restaurant(
                name = rc(restaurant_names),
                address = fake.address()
            )
           restaurants.append(r)
    
        db.session.add_all(restaurants)
        db.session.commit()
    
        pizzas = []
        for i in range(100):
            p = Pizza(
                name = rc(restaurant_ingredients),
                    ingredients = ','.join(sample(restaurant_ingredients,3)),            
            )
        pizzas.append(p)
        
        db.session.add_all(pizzas)
        db.session.commit()
    
    
        restaurant_pizza = []
        for i in range(100):
            rp = RestaurantPizza(
                price=randint(1,30),          
            )
            restaurant_pizza.append(rp)
        
        db.session.add_all(restaurant_pizza)
        db.session.commit()
        