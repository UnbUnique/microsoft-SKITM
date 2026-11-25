"""
Comparative Study: For Loop vs While Loop in Python
Description, Syntax, Use Cases, and Practical Demonstrations
"""

# ==============================================================================
# 1. FOR LOOP
# ==============================================================================
# Description:
# A 'for' loop is used for definite iteration. It iterates over the elements of
# any iterable sequence (such as a range, list, tuple, dictionary, or string)
# and executes the block of code for each item in that sequence.
#
# Syntax:
# for variable in iterable:
#     statement(s)
#
# Key Use Cases:
# 1. When the number of iterations is known before entering the loop (e.g., range(1, 11)).
# 2. Traversing items in data collections (lists, tuples, dictionaries, sets).
# 3. Iterating over characters of a string.
# 4. Pattern printing with fixed rows and columns.

# Demonstration 1: For Loop counting 1 to 5
print("=== 1. For Loop Example (Counting 1 to 5) ===")
for i in range(1, 6):
    print(f"For loop count: {i}")

# Demonstration 2: For Loop traversing a list
print("\n=== 2. For Loop Sequence Traversal ===")
fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")


# ==============================================================================
# 2. WHILE LOOP
# ==============================================================================
# Description:
# A 'while' loop is used for indefinite iteration. It repeatedly executes a block
# of statements as long as a given boolean condition remains True. The loop
# condition is evaluated before each iteration.
#
# Syntax:
# while condition:
#     statement(s)
#
# Key Use Cases:
# 1. When the number of iterations is NOT known beforehand.
# 2. Event-driven loops and game loops that run until a termination flag is set.
# 3. Reading streams, polling sensors, or validating user input repeatedly.
# 4. Algorithms that converge to a threshold (e.g., mathematical approximations).

# Demonstration 3: While Loop counting 1 to 5
print("\n=== 3. While Loop Example (Counting 1 to 5) ===")
j = 1
while j <= 5:
    print(f"While loop count: {j}")
    j += 1

# Demonstration 4: While Loop condition-controlled input validation
print("\n=== 4. While Loop Condition-Controlled Processing ===")
balance = 100
step = 1
while balance > 0:
    deduction = 25
    balance -= deduction
    print(f"Step {step}: Deducted {deduction}, Remaining Balance = {balance}")
    step += 1


# ==============================================================================
# 3. COMPARATIVE SUMMARY TABLE
# ==============================================================================
# --------------------------------------------------------------------------------------
# Feature                   For Loop                        While Loop
# --------------------------------------------------------------------------------------
# Iteration Type            Definite Iteration              Indefinite Iteration
# Condition Mechanism       Implicit (sequence exhaustion)   Explicit (Boolean expression)
# Variable Initialization   Automatic in loop header        Manual before entering loop
# Variable Update           Automatic per step              Manual inside loop body
# Risk of Infinite Loop     Extremely low                   High (if update step missed)
# Primary Use Case          Known ranges & collections      Dynamic conditions & events
# --------------------------------------------------------------------------------------

print("\n=== 5. Comparison Summary ===")
print("For Loop   : Best when iterating over a known sequence or range.")
print("While Loop : Best when repeating until an external condition is met.")
