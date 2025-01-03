def distinct_numbers(numbers):
    # Create an empty list for our results
    distinct_list = []
    
    print("Adding unique numbers:")
    # First, add each new number we find
    for num in numbers:
        if num not in distinct_list:
            distinct_list.append(num)
            print(f"Added {num}, current list: {distinct_list}")
        else:
            print(f"Skipped {num} (already in list)")
    
    print("\nBefore sorting:", distinct_list)
    # Then sort the list
    distinct_list.sort()
    print("After sorting:", distinct_list)
    
    return distinct_list

# Test with example numbers
numbers = [5, 2, 8, 2, 1, 5, 9, 2, 8, 3]
result = distinct_numbers(numbers)