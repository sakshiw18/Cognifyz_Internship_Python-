def predict_weather(temp):
    if temp < 10:
        return "It's very cold ❄️"
    elif temp < 20:
        return "Weather is cool 🌥️"
    elif temp < 30:
        return "Weather is pleasant 😊"
    elif temp < 40:
        return "It's hot ☀️"
    else:
        return "Extreme heat! Stay safe 🔥"

def weather_chatbot():
    print("🌦️ Weather Chatbot (type 'exit' to quit)")

    while True:
        user_input = input("\nYou: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye! 👋")
            break

        elif "temperature" in user_input or "temp" in user_input:
            try:
                temp = float(input("Enter current temperature (°C): "))
                prediction = predict_weather(temp)
                print("Bot:", prediction)
            except:
                print("Bot: Please enter a valid number!")

        elif "weather" in user_input:
            print("Bot: Please tell me the temperature to predict weather 🌡️")

        else:
            print("Bot: Ask me about temperature or weather!")

# Run chatbot
weather_chatbot()