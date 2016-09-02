import random, string

vowels = "aeiouy"
consonants = "bcdfghjklmnpqrstvwxz"
letters=string.ascii_lowercase

l1 = input("Input a letter: (v)owel | (c)onsonant | any (l)etter: ")
l2 = input("Input a letter: (v)owel | (c)onsonant | any (l)etter: ")
l3 = input("Input a letter: (v)owel | (c)onsonant | any (l)etter: ")

def generator():
   if l1 == 'v':
      letter1=random.choice(vowels)
   elif l1 == 'c':
      letter1=random.choice(consonants)
   elif l1 == 'l':
      letter1 = random.choice(letters)
   else:
      letter1 = l1;
      
   if l2 == 'v':
      letter2=random.choice(vowels)
   elif l2 == 'c':
      letter2=random.choice(consonants)
   elif l2 == 'l':
      letter2 = random.choice(letters)
   else:
      letter2 = l2;
      
   if l1 == 'v':
      letter3=random.choice(vowels)
   elif l3 == 'c':
      letter3=random.choice(consonants)
   elif l3 == 'l':
      letter3 = random.choice(letters)
   else:
      letter3 = l3;
      
   return letter1+letter2+letter3

for i in range(20):
   print(generator())