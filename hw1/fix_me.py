"""
Программа для вывода среднего значение из списка
Версия 1.1
"""


def calculate_average(nums):
    "функция считает среднее значение"
    total = sum(nums)
    count = len(nums)
    return total / count


result = calculate_average(nums=[10, 15, 20])
print("The average is:", result)
