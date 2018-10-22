def celsius_f(celsius):
    return (celsius * 9/5) + 32

temperatures=[10,-20,-289,100]

file=open("temperaturas.txt","a")

for temp in temperatures:
    if temp >= -273.15:
        file.write(str(celsius_f(temp))+"\n")

file.close()
