def isArmstrong(num):
    original = n
    sum = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        sum = sum + rem**3

    if original == sum:
        print(f"{original} is an Armstrong number")
    else:
        print(f"{original} is not an Armstrong number")

for n in range(100, 1000):
    isArmstrong(n)
