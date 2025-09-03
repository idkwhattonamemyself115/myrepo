"""
Lesson: Conditionals in Python
------------------------------
This file is intentionally incomplete.
Your job is to experiment, fill in blanks, and notice how conditionals change what happens.
"""

# --- Section 1: True or False? (Boolean Expressions) ---

# Conditionals always depend on something being True or False.
# Let's explore.

# TODO: Create two variables. One that represents age, and the other a boolean that is True if you are a student and false if you are not:

age=16
student=True
# What happens when we compare numbers?
print("Is age greater than 18?", )
print("Is age less than 13?", )

# What happens when we compare equality?
print("Is age exactly 16?", )

# What happens when we use a variable directly?
print("Is student status True?", )

# Reflection Question (write your answer in a comment):
# Q: Why do all of these print either True or False?


# --- Section 2: If Statements ---

# Problem: You want to check if someone can vote (age >= 18).
# First, try without conditionals (just print something no matter what).

print("You can vote!")   # TODO: What’s wrong with this approach?
#cuz you don't really know if the person is legal to vote or not, ur just assuming

# Now add an IF statement:
# if ___:
#     print("You can vote!")

if age>=18:
    print("you can vote!")

# --- Section 3: If/Else ---

# TODO: Write a program that checks if a number is even or odd.
# Steps to guide you:
# 1. Make a variable called num
# 2. Use the modulo operator (%) to check if num % 2 == 0
# 3. If even, print "Even number"
# 4. Otherwise, print "Odd number"

num=23

if num % 2==0:
    print("it's even")
else:
    print("it's odd")
# --- Section 4: If / Elif / Else ---

# TODO: Imagine a grading system:
#   - 90 or above → "A"
#   - 80 or above → "B"
#   - 70 or above → "C"
#   - 60 or above → "D"
#   - below 60   → "F"

# Write this using if / elif / else statements.

grade=60
if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else:
    print("F")

# --- Section 5: Nesting Conditionals ---

# TODO: Ask two questions:
#   1. Is the person a student?
#   2. Is their age under 18?
# If both are true, print "You are a student and a minor."
# Otherwise, print something else.
student=input("Is the person a student?")
age=input("Is their age under 18?")
if student=="yes" and age=="yes":
    print("You are a student and a minor")
else:
    print("you're not both a student and a minor")


# --- Section 6: Reflection ---
# Answer in comments:
# 1. What does a conditional REQUIRE in order to run effectively? a conditional require an if else statement and two equal signs that set up the conditional 
#    (Think: a test/condition that evaluates to True or False)
# 2. How do elif and else make your code shorter or more readable?
    # you can just ignore the same conditional if earlier codes already cover that. e.g. for the grading thing, i don't have to write it as if grade<=90 and grade>=80, because the grade can;t exceed 90, or else it would make the earlier conditional true. 
# 3. Can you think of a situation in real life where you’d use multiple conditionals?
    #  yes. So if I know that have workjob on B block, or I that I have my half credits on B block, I would finish my work the night before because I know that I don't have a free block the next day. 
