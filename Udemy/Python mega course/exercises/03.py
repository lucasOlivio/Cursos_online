def celsius_f(celsius):
    f = (celsius * 9/5) + 32
    return f

celsius = float(input("Celsius:"))

if celsius < -273.15:
    print("nononononono")
else:
    print(celsius_f(celsius))
