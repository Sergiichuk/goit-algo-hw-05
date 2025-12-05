def binary_search_with_upper_bound(arr, target):

    iterations = 0
    left = 0
    right = len(arr) - 1

    # тут будемо зберігати верхню межу
    upper_bound = None

    # звичайний двійковий пошук
    while left <= right:
        iterations += 1  
        mid = (left + right) // 2  

        if arr[mid] >= target:
            upper_bound = arr[mid]
            right = mid - 1  
        else:
            left = mid + 1

   
    return iterations, upper_bound


numbers = [0.5, 1.2, 2.0, 3.3, 4.8, 5.5, 7.7]

target = 3.0

result = binary_search_with_upper_bound(numbers, target)

print(result)
