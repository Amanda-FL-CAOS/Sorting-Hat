#variables:
grifindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

Q1 = """
Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
"""
opção = input(Q1)
if opção == "1":
  grifindor += 1
  ravenclaw += 1

elif opção == "2":
  hufflepuff += 1
  slytherin += 1

else:
  print("Wrong input.")

Q2 = """
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
"""
opção = input(Q2)
if opção == "1":
  hufflepuff += 2

elif opção == "2":
  slytherin += 2

elif opção == "3":
  ravenclaw += 2

elif opção == "4":
  grifindor += 2

else:
  print("Wrong input.")

Q3 = """
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
"""
opção = input(Q3)
if opção == "1":
  hufflepuff += 4

elif opção == "2":
  slytherin += 4

elif opção == "3":
  ravenclaw += 4

elif opção == "4":
  grifindor += 4

else:
  print("Wrong input.")

#the results:
print("The hat is ready to make a choice...")
points = {'Gryffindor': grifindor,'Ravenclaw': ravenclaw,'Hufflepuff': hufflepuff,'Slytherin': slytherin}
winner = max(points, key=points.get)
print(winner)

print("score:")
print("🦁 Gryffindor: ", grifindor)
print("🦅 Ravenclaw: ", ravenclaw)
print("🦡 Hufflepuff: ", hufflepuff)
print("🐍 Slytherin: ", slytherin)
