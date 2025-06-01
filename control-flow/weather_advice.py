# Define clothing recommendations in a dictionary
recommendations = {
    "sunny": "Wear a t-shirt and sunglasses.",
    "rainy": "Don't forget your umbrella and a raincoat.",
    "cold": "Make sure to wear a warm coat and a scarf."
}

# Prompt user input
weather = input("What's the weather like today? (sunny/rainy/cold): ").strip().lower()

# Get and print recommendation based on the weather
advice = recommendations.get(weather, "Sorry, I don't have recommendations for this weather.")
print(advice)
