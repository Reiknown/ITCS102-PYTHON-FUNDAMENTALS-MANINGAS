for i in range(1, 11, 1):
    for c in range(10, i, -1):
        print(" ", end=" ")
    for d in range(1, i, 1):
            print("*", end=" ")
    for e in range(1, i, 1):
            print("*", end=" ")
    print()
for i in range(1, 11, 1):
    for c in range(1, i, 1):
        print(" ", end=" ")
    for d in range(10, i, -1):
        print("*", end=" ")
    for e in range(10, i, -1):
        print("*", end=" ")
    print( )