
def maximumLengthSubstring(string: str) ->int:
    l, r = 0, 0
    max_len = 1
    counter = {}

    counter[string[0]] = 1

    while r <len(string) -1:
        r+=1
        if counter.get(string[r]): 
            counter[string[r]] += 1
        else :
            counter[string[r]] = 1

        while counter[string[r]] == 3:
            counter[string[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return print(max_len)

input_string = input("Digite a string: ")
maximumLengthSubstring(input_string)           


