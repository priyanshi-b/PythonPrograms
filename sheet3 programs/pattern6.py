rows= 5
cols = 5  
for i in range(rows):
    for j in range(cols):
        if j == 0 or j == cols - 1:
            print("*", end=" ")
        else:
            print("_", end=" ")
    print() 

