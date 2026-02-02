total = 0

while True:
    num = int(input("Enter a number to add to the total: "))
    if num == 0:
        break
    total += num

print(f"Total: {total}")