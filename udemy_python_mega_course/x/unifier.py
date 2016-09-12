with open ("protocol.txt", 'r') as file:   
   prot = [ i.rstrip() for i in file.readlines()] #read each line as a list member
   
with open ("website.txt", 'r') as file:
   site = [ i.rstrip() for i in file.readlines()]
   
with open ("port.txt", 'r') as file:
   port = [ i.rstrip() for i in file.readlines()]

for i in range(0,len(prot)): #number of lines of one of the files
   print ("Protocol " + prot[i] + " for website " + site[i] + " with port " + port[i])