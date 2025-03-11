
def binary_search(nums, n, left, right):

    while left < right:
        mid = int((left + right) / 2)

        if nums[mid] == n:
            return mid
        elif nums[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def exponential_search(array, target):
    if array[0] == target:
        return 0
    n = len(array)
    i = 1

    while i < n and array[i] < target:
        i *= 2 
    if array[i] == target:
        return i

    return binary_search(array, target, i // 2, min(i, n-1))

array = int(input("Digite o tamanho do array: "))
array = [i for i in range(1, array+1)]
target = int(input("Digite o numero a ser buscado: "))

result = exponential_search(array, target)

print(result)

