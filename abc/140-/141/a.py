def weather(s):
    if s == "Sunny":
        return "Cloudy"
    if s == "Cloudy":
        return "Rainy"
    if s == "Rainy":
        return "Sunny"


s = input().strip()
print(weather(s))
