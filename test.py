n = 7
perfect_number = 0

for i in range(1, n):
    
    if n % i == 0:
        if n == i:
            continue
        perfect_number += i

print(perfect_number)