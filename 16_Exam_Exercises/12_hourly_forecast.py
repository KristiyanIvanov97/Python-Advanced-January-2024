def forecast(*args):
    weathers = {"Sunny": [], "Cloudy": [], "Rainy": []}
    for location, weather in args:
        weathers[weather].append(location)

    # sorted_locations = sorted(some_dict.items(), key=lambda x: x[1])
    # print(sorted_locations)
    result = ""

    for weather, locations in weathers.items():
        for location in sorted(locations):
            result += f"{location} - {weather}\n"

    return result[:-1]


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
