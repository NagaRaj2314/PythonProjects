j1 = int(input("Capacity of jug 1: "))
j2 = int(input("Capacity of jug 2: "))
g = int(input("Amount of water to be measured: "))
def apply_rule(ch, x, y):
    # Rule 1: Fill jug 1
    if ch == 1:
        # Empty space in jug 1 should be less than its capacity
        if x < j1:
            return j1, y
        else:
            print("Rule cannot be applied")
            return x, y
    # Rule 2: Fill jug 2
    if ch == 2:
        # Empty space in jug 2 should be less than its capacity
        if y < j2:
            return x, j2
        else:
            print("Rule cannot be applied")
            return x, y
    # Rule 3: Transfer all water from jug 1 to jug 2
    if ch == 3:
        # Jug 1 should not be empty and jug 1 + jug 2 should not exceed capacity of jug 2
        if x > 0 and x + y <= j2:
            return 0, x + y
        else:
            print("Rule cannot be applied")
            return x, y
    # Rule 4: Transfer all water from jug 2 to jug 1
    if ch == 4:
        # Jug 2 should not be empty and jug 1 + jug 2 should not exceed capacity of jug 1
        if y > 0 and x + y <= j1:
            return x + y, 0
        else:
            print("Rule cannot be applied")
            return x, y
    # Rule 5: Transfer some water from jug 1 to jug 2 until jug 2 is full
    if ch == 5:
        # Jug 1 should not be empty and jug 1 + jug 2 should be more than or equal to capacity of jug 2
        if x > 0 and x + y >= j2:
            return x - (j2 - y), j2
        else:
            print("Rule cannot be applied")
            return x, y
    # Rule 6: Transfer some water from jug 2 to jug 1 until jug 1 is full
    if ch == 6:
        # Jug 2 should not be empty and jug 1 + jug 2 should be more than or equal to capacity of jug 1
        if y > 0 and x + y >= j1:
            return j1, y - (j1 - x)
        else:
            print("Rule cannot be applied")
            return x, y
    # Rule 7: Empty jug 1
    if ch == 7:
        # Check if jug 1 is not already empty
        if x > 0:
            return 0, y
        else:
            print("Rule cannot be applied")
            return x, y
    # Rule 8: Empty jug 2
    if ch == 8:
        # Check if jug 2 is not already empty
        if y > 0:
            return x, 0
        else:
            print("Rule cannot be applied")
            return x, y
    # Invalid choice
    else:
        print("INVALID CHOICE")
        return x, y
# Initialize capacity of both jugs as 0
x = y = 0
while True:
    if (x == g) or (y == g):
        print('GOAL ACHIEVED!')
        break
    else:
        print("================================RULES=================================")
        print("Rule 1: Fill jug 1")
        print("Rule 2: Fill jug 2")
        print("Rule 3: Transfer all water from jug 1 to jug 2")
        print("Rule 4: Transfer all water from jug 2 to jug 1")
        print("Rule 5: Transfer some water from jug 1 to jug 2 until jug 2 is full")
        print("Rule 6: Transfer some water from jug 2 to jug 1 until jug 1 is full")
        print("Rule 7: Empty jug 1")
        print("Rule 8: Empty jug 2")
        ch = int(input("Enter rule to apply: "))
        x, y = apply_rule(ch, x, y)
        print("================================STATUS================================")
        print("CURRENT STATE:", end=" ")
        print(x, y)
