#Dada uma string, inverta a ordem dos caracteres em cada palavra dentro de uma frase, preservando os espaços em branco e a ordem inicial das palavras.

def reverseWords(string):
    res = ''
    l, r = 0, 0 #Ponteiros para o inicio e fim da palavra

    while r < len(string): 
        if string[r] != '': #Move o ponteiro r ate um espaco em branco ou seja o fim da palavra
            r += 1
        else:
            res += string[l:r+1][::-1] #Adiciona a palavra invertida a string de res
            r += 1
            l = r

    res += ' '
    res += string[l:r][::-1] #Inverte a ultima palavra
    return res[1:]


input_string = input("Digite a string: ")
result = reverseWords(input_string)
print(result)