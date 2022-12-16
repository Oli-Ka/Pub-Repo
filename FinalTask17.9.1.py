chain = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
num = int(input('Введите число: '))
print('Введенная последовательность: ', (chain))

if num not in chain:
    chain.append(num)
print('Число добавлено в последовательность: ', (chain))

chain.sort()
print('Отсортировано по возрастанию: ', (chain))

def search_poz():
    if num == chain[0]:
        x = num
        print('Поиск не возможен, т.к. нет элементов меньше введенного числа')

    else:
        array = chain

        def binary_search(array, element, left, right):
            if left > right:
                return False

            middle = (right + left) // 2
            if array[middle] == element:
                return middle

            elif element < array[middle]:
                return binary_search(array, element, left, middle - 1)
            else:
                return binary_search(array, element, middle + 1, right)
        print('Номер позиции элемента (меньше введенного пользователем числа): ', (binary_search(array, num, 0, len(array) - 1) - 1))

search_poz()