

def recursive_sum(numbers):
    
    if len(numbers) == 0:
        return 0


    return numbers[0] + recursive_sum(numbers[1:])



def find_largest(numbers):

    if len(numbers) == 1:
        return numbers[0]

    
    if len(numbers) == 0:
        raise ValueError("The array must contain at least one number.")


    largest_rest = find_largest(numbers[1:])


    return max(numbers[0], largest_rest)



def recursive_count(numbers, target):
    
    if len(numbers) == 0:
        return 0


    if numbers[0] == target:
        return 1 + recursive_count(numbers[1:], target)

    return recursive_count(numbers[1:], target)


print("===== RECURSIVE ARRAY TOOLKIT =====")


print("\n1. SUM THE ARRAY")
print("Empty array:", recursive_sum([]))
print("One number:", recursive_sum([5]))
print("Several numbers:", recursive_sum([2, 4, 6, 8]))
print("Positive and negative:", recursive_sum([10, -5, 3, -2]))


print("\n2. FIND THE LARGEST NUMBER")
print("One number:", find_largest([7]))
print("Largest at beginning:", find_largest([20, 5, 10, 15]))
print("Largest at end:", find_largest([3, 8, 12, 25]))
print("Negative numbers:", find_largest([-10, -3, -7, -1]))


print("\n3. COUNT A CHOSEN NUMBER")
print("Empty array:", recursive_count([], 5))
print("Repeated number:", recursive_count([2, 5, 2, 8, 2], 2))
print("Number not found:", recursive_count([1, 3, 4, 6], 5))

print("\n===== END OF PROGRAM =====")

