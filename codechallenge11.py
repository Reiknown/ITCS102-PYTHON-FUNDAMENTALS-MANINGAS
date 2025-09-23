for i in range(1, 13, 1):
    for c in range(12, i, -1):
        print(" ", end=" ")
    for d in range(1, i, 1):
            print("*", end=" ")
    for e in range(0, i, 1):
            print("*", end=" ")
    print()
for i in range(1, 13, 1):
    for c in range(0, i, 1):
        print(" ", end=" ")
    for d in range(11, i, -1):
        print("*", end=" ")
    for e in range(12, i, -1):
        print("*", end=" ")
    print()
