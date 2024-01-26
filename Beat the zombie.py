#Create a list of possible weapons.
weapons = ["Baseball bat", "Sword", "Crow bar", "Gun", "Flamethrower"]

# In a variable called ‘zombieWeakness’ store the name of one of the weapons from the list.
zombieWeakness = weapons[4]

# Output messages telling the user that they have encountered a zombie and should prepare to fight.
print("As you are walking home from school a zombie pops out of no where and tries to attack you \n")

# Output the list of weapons to the user.  Ask if they want to type 1 to use one from the list or 2 to pick their own.  If they type 1 then they should input the weapon name - store it to a new variable. If they type 2 they should input the weapon name - add it to the list and save it to a new variable.
print("You look beside you and find a briefcase full of these weapons")
print(weapons)
number = input("\n if you want to use a weapon from the list type 1, if you want to enter your own weapon type 2: ")
if number == "1":
  userweapon = input("pick the weapon you want to use by name")
else:
  userweapon = input("enter the name of the weapon you want to use")
  weapons.append(number)
# If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  Otherwise output a message saying that they have lost.
if userweapon != weapons[4]:
  print("You try to fight back but the zombie eats you!")
else:
  print("You try to fight back and you beat the zombie!")

