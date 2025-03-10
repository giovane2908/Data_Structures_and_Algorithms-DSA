#Given a string, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

def reverseWords(string):
    res = ''
    l, r = 0, 0 #Ponteiros para o inicio e fim da palavra

    while r < len(string): 
        if string[r] != '': #move o ponteiro r ate um espaco em branco ou seja o fim da palavra
            r += 1
        else:
            res += string[l:r+1][::-1] #adiciona a palavra invertida a string de res
            r += 1
            l = r

    res += ' '
    res += string[l:r][::-1] #iverter a ultima palavra
    return res[1:]


input_string = "hello world"
result = reverseWords(input_string)
print(result)