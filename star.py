key = int(input("Enter the range :"))

for i in range(key):
    i = i + 1
    for j in range(i):
        print("*", end="")
    print("\n")
