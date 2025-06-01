# weather_advice.py

def get_weather_recommendation(weather):
    recommendations = {
        'sunny': 'Wear a t-shirt and sunglasses.',
        'rainy': "Don't forget your umbrella and a raincoat.",
        'cold': 'Make sure to wear a warm coat and a scarf.'
    }
    return recommendations.get(weather.lower(), "Sorry, I don't have recommendations for this weather.")

def main():
    weather_input = input("What's the weather like today? (sunny/rainy/cold): ")
    recommendation = get_weather_recommendation(weather_input)
    print(recommendation)

if name == "main":
    main()
