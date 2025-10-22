def evennum_checker(numbers):
    numbers2 = numbers
    for number in numbers2:
        if number % 2 != 0: #if the number is not divisible by 2 it will be removed from the list
            numbers2.remove(number)
    return numbers2

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:\n",numbers)
print("List without uneven numbers:\n",evennum_checker(numbers))