# Напишите программу, которая определит количество различных комбинаций американских монет(2 цента, 5 центов,
# 10 центов, 20 центов, 50 центов, 1 и 2 доллара), которые могут сложиться в определенную сумму.

try:
    summa = int(input("Vvedite summu v centah:"))
    while True:
        if summa > 0:
            summa += 1
            break
        else:
            summa = int(input("Ne goditsa, davai ponovoi:"))
except ValueError:
    print("Budet kasar")
    summa = 1001


def calculate_combinations(summa):
    matrix = [[1] * summa for i in range(8)]
    # инициализирую единичками сразу

    matrix[1][0] = 2  # в первом элементе номинал
    matrix[2][0] = 5
    matrix[3][0] = 10
    matrix[4][0] = 20
    matrix[5][0] = 50
    matrix[6][0] = 100
    matrix[7][0] = 200

    for i in range(1, 8):
        if i > 2:
            matrix[i - 2] = 0  # удаляю ряд, который больше не нужен
        for c in range(1, summa):
            value = matrix[i][0]  # беру номинал
            if value < c:
                matrix[i][c] = matrix[i][c - value] + matrix[i - 1][c]
            elif value == c:
                matrix[i][c] = matrix[i - 1][c] + 1
            else:
                matrix[i][c] = matrix[i - 1][c]

    print(f"Varikov razmena: {matrix[-1][-1]}")


if __name__ == '__main__':
    calculate_combinations(summa)  
