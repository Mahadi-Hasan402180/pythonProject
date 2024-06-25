"""

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

def main():
    SIZE = 5
    numbers = []
    print(f"Enter {SIZE} numbers:")
    for _ in range(SIZE):
        number = int(input())
        numbers.append(number)

    total_sum = sum_array(numbers)
    print(f"Sum of the elements: {total_sum}")

if __name__ == "__main__":
    main()

"""

def calculate_array_sum(array, size):
    total = 0
    for i in range(size):
        total += array[i]
    return total

if __name__ == "__main__":
    SIZE = 5
    numbers = [0] * SIZE
    print("Enter", SIZE, "numbers:")
    for i in range(SIZE):
        numbers[i] = int(input())

    sum_total = calculate_array_sum(numbers, SIZE)
    print("sum of the elements:", sum_total)



