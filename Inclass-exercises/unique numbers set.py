numbers = (1,2,3,3,4,3,4,5,6,2,7,3,8,9,12,35)

def unique_numbers(numbers):
    num = set(numbers)
    return num

def count(numbers):
    num = set(numbers)
    return len(num)

print("Your unique numbers are", unique_numbers(numbers))
print("You have a total of", count(numbers), "unique numbers.")

