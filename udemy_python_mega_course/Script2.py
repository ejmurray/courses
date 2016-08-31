print(1)
def currency_converter(rate, euros):
   dollars=euros*rate
   return dollars

functions=[currency_converter(100, 1000),currency_converter(100, 2000)]
print(functions)
