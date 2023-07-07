total = 0
for num in range(1, 101):
    if num % 2 == 0:
        total += num
        print(num)

print(f"Sum of all even numbers from 1 to 100 is {total}")
 