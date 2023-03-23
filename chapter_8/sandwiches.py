def make_sandwich(*ingredients):
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient.title()}")

make_sandwich("hamburguer", "cheddar cheese", "bacon", "tomato")
make_sandwich("chicken", "catchup", "cheese")
make_sandwich("egg")
