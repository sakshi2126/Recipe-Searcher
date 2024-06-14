import streamlit as st

# Recipe dictionary with categories
recipes = {
    "Breakfast": {
        "tea": {
            1: {"water": "1 cup", "tea leaves": "1 teaspoon", "sugar": "To taste"},
            2: {"water": "2 cups", "tea leaves": "2 teaspoons", "sugar": "To taste"},
            3: {"water": "3 cups", "tea leaves": "3 teaspoons", "sugar": "To taste"},
        },
        "coffee": {
            1: {"coffee powder": "1 tablespoon", "sugar": "To taste", "milk": "1/2 cup", "water": "1/2 cup"},
            2: {"coffee powder": "2 tablespoons", "sugar": "To taste", "milk": "1 cup", "water": "1 cup"},
            3: {"coffee powder": "3 tablespoons", "sugar": "To taste", "milk": "1 1/2 cups", "water": "1 1/2 cups"},
        },
        "scrambled eggs": {
            1: {"eggs": "2", "milk": "1 tablespoon", "salt": "Pinch", "pepper": "Pinch", "butter": "1 teaspoon"},
            2: {"eggs": "4", "milk": "2 tablespoons", "salt": "Pinch", "pepper": "Pinch", "butter": "2 teaspoons"},
            3: {"eggs": "6", "milk": "3 tablespoons", "salt": "Pinch", "pepper": "Pinch", "butter": "3 teaspoons"},
        },
        "oatmeal": {
            1: {"rolled oats": "1/2 cup", "water": "1 cup", "salt": "Pinch"},
            2: {"rolled oats": "1 cup", "water": "2 cups", "salt": "Pinch"},
            3: {"rolled oats": "1 1/2 cups", "water": "3 cups", "salt": "Pinch"},
        },
        "pancakes": {
            1: {"flour": "1/2 cup", "milk": "3/4 cup", "eggs": "1", "sugar": "1 tablespoon"},
            2: {"flour": "1 cup", "milk": "1 1/2 cups", "eggs": "2", "sugar": "2 tablespoons"},
            3: {"flour": "1 1/2 cups", "milk": "2 1/4 cups", "eggs": "3", "sugar": "3 tablespoons"},
        },
        "smoothie": {
            1: {"fruit": "1 cup", "yogurt": "1/2 cup", "milk": "1/2 cup", "honey": "1 tablespoon"},
            2: {"fruit": "2 cups", "yogurt": "1 cup", "milk": "1 cup", "honey": "2 tablespoons"},
            3: {"fruit": "3 cups", "yogurt": "1 1/2 cups", "milk": "1 1/2 cups", "honey": "3 tablespoons"},
        },
    },
    "Lunch": {
        "sandwich": {
            1: {"bread": "2 slices", "meat": "2 ounces", "cheese": "1 slice", "vegetables": "To taste"},
            2: {"bread": "4 slices", "meat": "4 ounces", "cheese": "2 slices", "vegetables": "To taste"},
            3: {"bread": "6 slices", "meat": "6 ounces", "cheese": "3 slices", "vegetables": "To taste"},
        },
        "salad": {
            1: {"lettuce": "2 cups", "tomato": "1/2", "cucumber": "1/4", "dressing": "2 tablespoons"},
            2: {"lettuce": "4 cups", "tomato": "1", "cucumber": "1/2", "dressing": "4 tablespoons"},
            3: {"lettuce": "6 cups", "tomato": "1 1/2", "cucumber": "3/4", "dressing": "6 tablespoons"},
        },
        "fried rice": {
            1: {"rice": "1 cup (cooked)", "eggs": "1", "vegetables": "1/2 cup", "soy sauce": "1 tablespoon"},
            2: {"rice": "2 cups (cooked)", "eggs": "2", "vegetables": "1 cup", "soy sauce": "2 tablespoons"},
            3: {"rice": "3 cups (cooked)", "eggs": "3", "vegetables": "1 1/2 cups", "soy sauce": "3 tablespoons"},
        },
    },
    "Dinner": {
        "pasta": {
            2: {"pasta": "8 ounces", "sauce": "1/2 cup", "water": "4 cups", "salt": "1 teaspoon"},
            3: {"pasta": "12 ounces", "sauce": "3/4 cup", "water": "6 cups", "salt": "1 1/2 teaspoons"},
            4: {"pasta": "16 ounces", "sauce": "1 cup", "water": "8 cups", "salt": "2 teaspoons"},
        },
    }
}

def scale_quantity(quantity, factor):
    if quantity.lower() == "to taste":
        return quantity
    try:
        quantity_value = float(quantity.split()[0])
        quantity_unit = quantity.split()[1]
        scaled_value = quantity_value * factor
        return f"{scaled_value:.2f} {quantity_unit}"
    except (ValueError, IndexError):
        return quantity

st.title("Recipe Generator")

categories = list(recipes.keys())
selected_category = st.selectbox("Select a category:", categories)

if selected_category:
    food_options = list(recipes[selected_category].keys())
    food_name = st.selectbox("Select a food item:", food_options)
    num_people = st.number_input("Enter number of people:", min_value=1, value=10)

    if st.button("Generate Recipe"):
        if food_name in recipes[selected_category]:
            recipe = recipes[selected_category][food_name].get(num_people, None)

            if not recipe:
                max_serving = max(recipes[selected_category][food_name].keys())
                base_recipe = recipes[selected_category][food_name][max_serving]
                scaling_factor = num_people / max_serving
                recipe = {
                    ingredient: scale_quantity(quantity, scaling_factor)
                    for ingredient, quantity in base_recipe.items()
                }

            st.subheader(f"Recipe for {food_name.capitalize()} (Serves {num_people})")
            for ingredient, quantity in recipe.items():
                st.write(f"- {ingredient.capitalize()}: {quantity}")
        else:
            st.warning(f"Sorry, no recipe found for {food_name.capitalize()}.")


