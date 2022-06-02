# Lister
Deltagere = []
Vegetar = []
Kylling = []
Oksekød = []


# definere stat menu
def start( ):
	linier(32)
	print("* Tilmelding til julefrokosten *")
	linier(32)
	print("Tilføj nye gæster (1) : ")
	print("Fjern gæster      (2) : ")
	print("Udskriv liste     (3) : ")
	print("Afbryd            (4) : ")
	return input ("Indtast  \"1 - 4\" : ")

# definere valg af mad
def food():
  print()
  print("Valg af mad")
  linier(10)
  print("Vælg Vegetar       (1) : ")
  print("Vælg Kylling       (2) : ")
  print("Vælg Oksekød       (3) : ")
  print("Ingen Mad          (4) : ")
  return input("Vælg mad  \"1 - 4\" : ")

# definere linier i UI
def linier(num):
	for i in range(num):
		print("*", end="")
	print()

run = True
while run:
  x = start( )

  if (x) == "1":
    print("Tilføj en deltager")
    name = input("Navn : ")
    name = name.capitalize()
    Deltagere.append(name)

#Tilføje valg af mad når der er tastet et navn
    mad = True
    while mad:
      y = food()

      if (y) == "1":
        Vegetar.append(name)
        print(f"{name} er tilføjet listen")
        mad = False
      
      elif (y) == "2":
        Kylling.append(name)
        print(f"{name} er tilføjet listen")
        mad = False
      
      elif (y) == "3":
        Oksekød.append(name)
        print(f"{name} er tilføjet listen")
        mad = False
      
      elif (y) == "4":
        print(f"{name} er tilføjet listen")
        mad = False
      
      else:
        print ("Det forstod jeg ikke \n Prøv igen")
      
     

# Fjerne en deltager
  elif (x) == "2":
    print("Fjern en deltager")
    name = input("Navn : ")
    for i in Deltagere:  
      if i == name:
        Deltagere.remove(i) 
        print(f"Deltageren {name} er slettet og mad valg fjernet")
    for i in Vegetar:
      if i == name:
        Vegetar.remove(i)   
    for i in Kylling:
      if i == name:
        Kylling.remove(i)     
    for i in Oksekød:
      if i == name:
        Oksekød.remove(i) 



 # udskriv
  elif (x) == "3":
    print()
    z = len(Deltagere)
    print (f"Antal af deltagere : {z}")
    linier(25)
    print()
    count = 0  
    while count < len(Deltagere):
      print (Deltagere [count])
      count += 1
    
    print()
    a = int(len(Vegetar))
    if a == 0:
      print ("Ingen der ønsker Vegetar")
    else:
      print(f"Antal af vegetar : {a}")
    linier(25)
    print()
    vege = 0
    while vege < len(Vegetar):
      print (Vegetar [vege])
      vege += 1
 
    print()
    b = int(len(Kylling))
    if b == 0:
      print ("Ingen der ønsker Kylling")
    else:
      print(f"Antal af Kylling : {b}")
    linier(25)
    print()
    kyl = 0
    while kyl < len(Kylling):
      print (Kylling [kyl])
      kyl += 1

    print()
    c = int(len(Oksekød))
    if c == 0:
      print ("Ingen der ønsker Oksekød")
    else:
      print(f"Antal af oksekød : {c}")
    linier(25)
    print()
    okse = 0
    while okse < len(Oksekød):
      print (Oksekød [okse])
      okse += 1

    print()
    linier(25)
    print(f"Antal der spiser {a+b+c}")
    linier(25)

    

# exit af programmet
  elif (x) == "4":
    linier(50)
    x = input("Er du sikker på at du vil forlade programmet \n DETTE VIL SLÆTTE ALT (ja) ")
    if x == ("ja"):
      run = False

  else :
    print("Det forstod jeg ikke \n Prøv igen")


print ("Farvel!!!")
