def cel2fahr(c):
   if c < -273.15:
      return "Can't convert. The informed temperature is lower than 273.15 C."
   else:   
      return c*1.8+32   

#print(cel2fahr(-274))
