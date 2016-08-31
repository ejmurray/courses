def currency_converter(rate, euros):
   dollars=euros*rate
   return dollars

r=input("Enter rate: ")
e=input("Enter euro: ")
print(currency_converter(float(r),float(e)))
