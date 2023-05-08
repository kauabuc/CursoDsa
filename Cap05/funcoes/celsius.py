Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = map(lambda celsius: (celsius * 1.8) + 32, Celsius)
print(list(Fahrenheit))
