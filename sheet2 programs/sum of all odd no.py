A = int(input("Enter an integer A: "))
sum_of_odds = 0
for i in range(1, A + 1):
   
    if i % 2 != 0:
        sum_of_odds += i

print("The sum of all odd numbers from 1 to", A, "is:", sum_of_odds)
