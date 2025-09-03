"""
Lesson: Lists and Dictionaries in Python
----------------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how lists and dictionaries store and organize data.
"""

# --- Section 1: Making a List ---

# Lists keep items in order.
# Example: foods = ["pizza", "sushi", "ice cream"]

# TODO: Create a list of 5 of your favorite foods.

foods = ["ramen","errms", "ohhh", "banana"]

# Access items by index (first = 0):
print("The first food is"+ str({foods[0]}))
print("The last food is"+ str({foods[3]}))

# Bug Exploration:
# Try printing foods[100] below.
# Q: What error do you get, and what does it mean?



# --- Section 2: Changing a List ---

# Lists can grow and shrink using built-in methods.

# TODO: Add a new food to the end of your list with .append()


# TODO: Insert a food at the beginning with .insert()


# TODO: Remove one food from the list with .remove()


# TODO: How many foods are in the list? Use len()


# Bug Exploration:
# Try removing something that isn’t in the list:
# foods.remove("chocolate")
# Q: What happens? Why?


# --- Section 3: Loops with Lists ---

# TODO: Write a for loop that prints each food in your list one by one.
i=0
for i in range(len(foods)):
    print(foods[i])

# Bug Exploration:
# Change your loop to go past the length of the list:
for i in range(4):
    print(f"Index {i} → {foods[i]}")
# Q: Why does this cause an error?


# --- Section 4: Dictionaries (Key–Value Pairs) ---

# Dictionaries let us label data with keys.
# Example: 
me = {
    "name": "Kevin",
    "age": 30,
    "student": False
    }

# TODO: Make a dictionary with at least 3 pieces of information about yourself.

me = {
    "name": "Katie",
    "age": 88,
    "favorite_color":"Yellow"
    }
print(f"My name is {me['name']}")
print(f"My age is {me['age']}")
print(f"My favorite color is {me['favorite_color']}")
# Access values using keys by using the .get() method rather than indexing
# print(f"My name is {me['name']}")
# print(f"My age is {me['age']}")
# print(f"My favorite color is {me['favorite_color']}")

# Bug Exploration:
# Try printing a key that doesn’t exist.
# print(me["hometown"])
# Q: What kind of error is this? How could you check if a key exists before using it? Why is the .get() method useful here?

#wrong paranthesis? 
# --- Section 5: Changing a Dictionary ---

# TODO: Add a new key-value pair.


# TODO: Change the value of an existing key.

me['age']=494
# TODO: Remove one key-value pair.


# Bug Exploration:
# Try removing a key that doesn’t exist:
# me.pop("grade")
# Q: What happens? Is this similar to removing from a list?


# --- Section 6: Loops with Dictionaries ---

# TODO: Write a loop that prints both the keys and values in your dictionary using .items()


# Bug Exploration:
# What happens if you loop over just the dictionary without calling .items()?
# for key in me:
#     print(key)

# Q: Why does it only print the keys? How can you change your for loop to print key and value pairs?


# --- Section 7: Mixing Lists and Dictionaries ---

# TODO: Create a list of dictionaries. 
# Example: a list of 3 friends, where each friend has a name and favorite food.
lucas= {
    "name":"lucas",
    "fav_food": "boiled eggs"
}
sarah= {
    "name":"Sarah",
    "fav_food": "sandwich"
}
katie= {
    "name":"Katie",
    "fav_food": "m&ms"
}
list=[lucas,sarah,katie]
# TODO: Print the favorite food of the second friend.

print(f"her name is{sarah['name']}")
print(f"her fav food is{sarah['fav_food']}")

# TODO: Loop through and print "<name> likes <food>" for each friend.

for i in range(len(list)):
    print(f"their name is{list[i]['name']}")
    print(f"their name is{list[i]['fav_food']}")
# Bug Exploration:

# What happens if you try to access friend["hobby"] when "hobby" doesn’t exist in the dictionary?
# Q: How might you prevent this kind of error in real programs?
#it's a key error 

# --- Section 8: Reflection ---
# Answer in comments:
# 1. How is a list different from a dictionary?
# a list includes several components that are not given a specific vaiable name, while for dictionary, there is a special variable name for each component 
# 2. When would you want to use a dictionary instead of a list? when you're looking for something specific and 
# 3. Can you think of a real-world situation where combining lists and dictionaries would be useful?
# 4. What types of mistakes gave you the most errors today?
# 5. How might noticing errors actually help you learn?