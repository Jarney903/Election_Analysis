# Create a Python list to store your grocery list
glist = ["Milk", "Bread", "Eggs", "Evil Death", "Jelly"]
    # * Milk
    # * Bread
    # * Eggs
    # * Peanut Butter
    # * Jelly
# Print the grocery list
print(glist)

# Change "Peanut Butter" to "Almond Butter" and print out the updated list
glist[3] = "Almond Butter"

# Remove "Jelly" from grocery list and print out the updated list
glist.remove("Jelly")
# or glist.pop(4)

# Add "Coffee" to grocery list and print the updated list
#glist.append("Coffee")
glist.insert(2,"Coffee")

#Replace
glist[3] = "Tacos"

print(glist.index("Tacos"))

Taco_index = glist.index("Tacos")

print(Taco_index)

glist[Taco_index] = "Beer"

print(glist)