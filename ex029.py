                #fateamento de texto

frase='curso em video python' #a contagem da frase começa a parti do 0,levando em consideração os espaços vazios
print(frase[3:13])
print(frase[1:15]) # o 15 marca a podição 15,mas ele nao é levado em consideração,ou seja, vai ate a posição 14
print(frase[1:15:2]) #2 significa que vai pular de 2 em 2
print(frase[1::2]) #tiramos o 15 significa então que vai levar em consideração a frase toda
print(frase[::2]) # tiramos o 1 e o 15,ou seja, o inicio e o final. então sera levada em consideração toda a frase pulando de 2 em 2
print(frase.count('o')) #vai contar quantos (o) tem na frase
print(frase.upper()) #deixa a frase maiuscula
print(len(frase)) #vai nos dizer quantos caracteres/letras tem a frase
print('video' in frase) #vai me dizer se a palavra video esta em frase
frase=print(frase.replace('curso','everton')) # vai trocar a palavra curso por everton

print('''fdfdfdsdfjksdfjkdsjfdsfkjdsfdsj   
      dfdsfdsfdsfdsjkfjkdsfkjdsjfsddfdsf
      fdsfsdfsdhfhjdsfhsdfsdfsdfkdsjkffds
      dsfhdsvfhjdsfsdjfsdjfjkdskjfhdshffd
      fdshkfjkdsfkdsnklfndsklfkdskfdskfk''') #use aspas triplas para textos grandes