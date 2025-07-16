i = 0
size = int(input("Enter the size of the pattern: "))
while i < size:
    j = 0
    for j in range(size):
        print("*", end="")
    print()
    i += 1
