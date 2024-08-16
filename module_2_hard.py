num = int(input("Введите число от 3 до 21: "))
password = ''
for i in range(1, 20):
    for j in range(i + 1, 20):
        if num % (i + j) == 0:
            password += str(i) + str(j)
print(password)
