import random

leftycardnumber = random.randint(1,13)
rightycardnumber = random.randint(1,13)

print ("Lefty played a")
print(leftycardnumber)
print("")
print("Righty played a")
print(rightycardnumber)

if leftycardnumber >= rightycardnumber:
  print("Lefty wins")

elif leftycardnumber <= rightycardnumber:
  print("Righty wins")
  
elif leftycardnumber == rightycardnumber:
  print("Tie")