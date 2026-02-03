frase = "Buenos dias a todos Buenos a"
div = frase.split(" ")  
dic = {}

for x in range(len(div)):
    if div[x] in dic:
        dic[div[x]] = (dic[div[x]]) + 1
        print (dic[div[x]])
    else:
        dic[div[x]] = 1
    print (dic)

def cadena(frase):
    div = frase.split(" ")  
    dic = {}

    for x in range(len(div)):
        if div[x] in dic:
            dic[div[x]] = (dic[div[x]]) + 1
            print (dic[div[x]])
        else:
            dic[div[x]] = 1
        #print (dic)
    return dic

frase = input()
print(cadena(frase))
