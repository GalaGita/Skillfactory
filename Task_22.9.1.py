while True:
    numbers = input('Введите последовательность чисел через пробел:\n')
    try:
        list_of_numbers = list(map(int, numbers.split()))
        break
    except ValueError:
        try:
            list_of_numbers = list(map(float, numbers.split()))
            break
        except ValueError:
            print("Для ввода чисел можно использовать только цифры и символы '.' и '-'. Числа должны разделяться пробелом.")

while True:
    any_number = input("Введите любое число: ")
    try:
        number = int(any_number)
        break
    except ValueError:
        try:
            number = float(any_number)
            break
        except ValueError:
            print("Для ввода числа можно использовать только цифры и символы '.' и '-'.")

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

sorted_numbers = merge_sort(list_of_numbers)
print(f'Введенная вами последовательность чисел отсортирована в порядке возрастания: \n{sorted_numbers}')

def binary_search(array, element, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if array[middle] < element < array[middle+1]:
        return middle
    elif array[middle] == element:
        return middle - 1
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

print("Поиск элемента последовательности, который меньше заданного вами числа, а следующий за ним больше или равен этому числу.")

if sorted_numbers[0] >= number:
    print(f'"Элемент не найден. В вашей последовательности нет чисел меньше {number}.')
elif sorted_numbers[-1] <= number:
    print(f'Элемент не найден. В вашей последовательности нет чисел больше {number} или равных {number}.')
else:
    print(f'Элемент найден. Номер позиции (индекс) элемента в отсортированной в порядке возрастания последовательности: {binary_search(sorted_numbers, number, 0, len(sorted_numbers) - 1)}')
