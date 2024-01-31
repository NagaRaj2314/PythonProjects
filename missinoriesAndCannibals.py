print("Game Start\nNow the task is to move all of them to the right side of the river")
print("Rules:\n1. The boat can carry at most two people\n2. If cannibals outnumber missionaries, the cannibals would eat the missionaries")
lM, lC = 3, 3
rM, rC = 0, 0
k = 0
print("\nM M M C C C | --- | \n")
try:
    while True:
        while True:
            print("Left side -> right side river travel")
            uM = int(input("Enter number of Missionaries travel => "))
            uC = int(input("Enter number of Cannibals travel => "))
            if uM + uC == 0 or uM + uC > 2 or lM - uM < 0 or lC - uC < 0:
                print("Invalid input! Re-enter: ")
            else:
                lM -= uM
                lC -= uC
                rM += uM
                rC += uC
                for _ in range(lM): print("M ", end="")
                for _ in range(lC): print("C ", end="")
                print("| --> | ", end="")
                for _ in range(rM): print("M ", end="")
                for _ in range(rC): print("C ", end="")
                print("\n")
                k += 1
                if (lC == 3 and lM == 1) or (lC == 3 and lM == 2) or (lC == 2 and lM == 1) or \
                        (rC == 3 and rM == 1) or (rC == 3 and rM == 2) or (rC == 2 and rM == 1):
                    print("Cannibals eat missionaries: You lost the game")
                    break
                if rM + rC == 6:
                    print("You won the game! Congrats")
                    print("Total attempt:", k)
                    break
                break
        while True:
            print("Right side -> Left side river travel")
            userM = int(input("Enter number of Missionaries travel => "))
            userC = int(input("Enter number of Cannibals travel => "))
            if userM + userC == 0 or userM + userC > 2 or rM - userM < 0 or rC - userC < 0:
                print("Invalid input! Re-enter: ")
            else:
                lM += userM
                lC += userC
                rM -= userM
                rC -= userC
                k += 1
                for _ in range(lM): print("M ", end="")
                for _ in range(lC): print("C ", end="")
                print("| <-- | ", end="")
                for _ in range(rM): print("M ", end="")
                for _ in range(rC): print("C ", end="")
                print("\n")
                break
except EOFError as e:
    print("\nInvalid input. Please retry!!")
