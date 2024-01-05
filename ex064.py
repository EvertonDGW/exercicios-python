"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas: #primeiro e executado a coluna. depois e executado o while que ta fora 
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

    #basicamente o while interno vai ser executado primeiro, depois é executado o while externo


print('Acabou')