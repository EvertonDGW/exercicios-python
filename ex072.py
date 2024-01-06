for i in range(10): #chamamos isso aqui de iteração.. range(start,stop.step) como so tem 1 valor definido dentro de range, ele e o stop (pare) a contagem vai de 0 a 9
    if i == 2:
        print('i é 2, pulando...')
        continue #Então, quando i é igual a 2, o bloco if i == 2 é executado, mas o bloco for j in range(1, 3) não é. 
    #Portanto, quando i é igual a 2, o primeiro loop continua para a próxima iteração(o elemento dentro de range que vai de 0 ate 9) sem executar o restante do código dentro do loop, incluindo o segundo loop. Isso é uma característica do continue – ele pula para a próxima iteração do loop imediatamente após ser encontrado.
                

    if i == 8:
        print('i é 8, seu else não executará')
        break #A função do break é interromper imediatamente a execução do loop mais externo (for i in range(10)) quando a condição if i == 8 é verdadeira. Ou seja, quando o valor de i atinge 8, o loop é interrompido, e o programa continua com a execução do código após o loop.
        #se voce remover o break, else sera executado

    for j in range(1, 3):  # aqui é outra iteração... 1 representa o start e o 3 represeta o stop a contagem vai de 1 a 2
        print(i, j) #pelo fato de usar o print para exibir as 2 iterações, uma tem que acompanhar o resultado da outra. porque elas ocupam espaços em cada linha

else: #esse else esta associado ao primeiro loop/iteração --> for i in range(10)

    #O bloco else no final será executado se o loop for i in range(10) for concluído sem a execução de break. No caso, a mensagem "For completo com sucesso!" será impressa ao finalizar todas as iterações do loop for. Se houver um break (como no caso quando i == 8), o bloco else não será executado.

    print('For completo com sucesso!')

    #imagine uma contagem de 0 a 10, o loop for vai analisar cada numero, isso e a iteração
    # o resultado dessa iteração dentro de range, sera armazenada dentro da variavel (i)
    #for i in range(10): --> loop externo
    #for j in range(1, 3): --> loop interno
    #else esta associada com o loop externo que seri --> for i in range(10):
    #lembre-se interações occorem nos loop for ou while