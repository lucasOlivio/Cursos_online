def currency_converter(rate, euros):
    dollars = euros * rate
    return dollars

r = input("\nrate?\n")
e = input("\neuros?\n")

print("\n",currency_converter(float(r),float(e)))
