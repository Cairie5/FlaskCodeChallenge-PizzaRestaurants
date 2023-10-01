# seed.py

from app import db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Create some restaurants
    restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    # Create some pizzas
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Add pizzas to restaurants
    restaurant1.pizzas.append(pizza1)
    restaurant1.pizzas.append(pizza2)
    restaurant2.pizzas.append(pizza1)

    # Create some restaurant-pizza associations
    restaurant_pizza1 = RestaurantPizza(price=10, pizza=pizza1, restaurant=restaurant1)
    restaurant_pizza2 = RestaurantPizza(price=12, pizza=pizza2, restaurant=restaurant1)
    restaurant_pizza3 = RestaurantPizza(price=11, pizza=pizza1, restaurant=restaurant2)

    # Add data to the session and commit
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.add(restaurant_pizza1)
    db.session.add(restaurant_pizza2)
    db.session.add(restaurant_pizza3)
    db.session.commit()

if __name__ == '__main__':
    seed_data()
