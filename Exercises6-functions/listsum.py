def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [4, 6, 1, 2, 5]
print(list_sum(numbers))