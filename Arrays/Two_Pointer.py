#Given a string, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(string):
    res = ''
    l, r = 0, 0 #Pointers left and right

    while r < len(string):
        if string[r] != ' ':
            r += 1
        else:
            res += string[l:r+1][::-1]
            r += 1
            l = r

    res += ' '
    res += string[l:r + 2][::-1]
    return res[1:]


input_string = ""
result = reverseWords(input_string)
print(result)