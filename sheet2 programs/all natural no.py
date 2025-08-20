N = int(input("Enter a natural number: "))
if N > 0:
    for i in range(N, 0, -1):
        print(i)
else:
    print("Please enter a natural number greater than 0.")
