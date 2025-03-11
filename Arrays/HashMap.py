#Dada uma string, encontre o primeiro caractere não repetido e retorne seu índice. Se não existir, retorne -1.
def fistUniqChar(str: str) -> int:  

    d = {}

    for id, char in enumerate(str):
        if not d.get(char):
            d[char] = [id, 1]
        else:
            d[char] [1] += 1
    for char, value in d.items():
        if value[1] == 1:
            return value[0]
        
    return -1

str = str(input("digite a string: "))
result = fistUniqChar(str)
print(result)
