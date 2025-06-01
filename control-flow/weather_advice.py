# Ask the user to input the current weather
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Check for the 'sunny' condition
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

# Check for the 'rainy' condition
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")

# Check for the 'cold' condition
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")

# Handle unexpected input
else:
    print("Sorry, I don't have recommendations for this weather.")
