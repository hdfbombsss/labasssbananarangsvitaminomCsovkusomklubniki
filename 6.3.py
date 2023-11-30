def count_elements_less_than_C(arr, C):
    count = 0
    for element in arr:
        if element < C:
            count += 1
    return count

def find_max_element(arr):
    max_element = arr[0]
    for element in arr:
        if element > max_element:
            max_element = element
    return max_element

def main():
    n = int(input("Введите количество элементов в списке: "))
    arr = []
    for i in range(n):
        element = int(input(f"Введите элемент {i+1}: "))
        arr.append(element)
    C = int(input("Введите число C: "))

    count = count_elements_less_than_C(arr, C)
    max_element = find_max_element(arr)

    print(f"Количество элементов списка, меньших {C}: {count}")
    print(f"Максимальный элемент списка: {max_element}")

if __name__ == "__main__":
    main()
