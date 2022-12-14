def celsius_to_fahrenheit(c):
    a, b = 40, 1.8
    return ((c + a) * b) - a


daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]

daily_temp_f = list(map(celsius_to_fahrenheit, daily_temp_c))

limit = 80
temp_above_80 = list(filter(lambda x: x > limit, daily_temp_f))

print(len(temp_above_80))