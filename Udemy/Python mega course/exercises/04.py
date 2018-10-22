def celsius_f(celsius):
    if celsius < -273.15:
        return "nononononono"
    else:
        return (celsius * 9/5) + 32

temperatures=[10,-20,-289,100]

for temp in temperatures:
    print(celsius_f(temp))
