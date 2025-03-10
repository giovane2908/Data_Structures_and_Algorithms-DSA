#Dado um array ordenado de números inteiros de 1 até n, qual é a posição de um número específico x dentro desse array usando a busca binária? Além disso, quantos passos são necessários para encontrar o número?

def binary_search(nums, n):
    left = 0 
    right = len(nums) - 1  
    steps = 0

    while left < right:
        steps += 1
        mid = int((left + right) / 2)

        if nums[mid] == n:
            print(f"Found {n} in {steps} steps")
            return mid
        elif nums[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

    return -1
number = int(input("Digite o numero a ser buscado: "))
array_len = int(input("Digite o tamanho do array: "))
array_len = [i for i in range(1, array_len+1)]

binary_search(array_len, number)

