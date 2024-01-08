"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""

import os

lista = []  # Inicializa uma lista vazia chamada 'lista' para armazenar valores

while True:  # Loop infinito para manter o programa em execução
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')  # Captura a opção do usuário

    if opcao == 'i':  # Se a opção for 'i', o usuário deseja inserir na lista
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal
        valor = input('Valor: ')  # Solicita ao usuário um valor
        lista.append(valor)  # Adiciona o valor à lista
    elif opcao == 'a':  # Se a opção for 'a', o usuário deseja apagar um elemento da lista
        indice_str = input('Escolha o índice para apagar: ')  # Solicita ao usuário o índice para apagar

        try:
            indice = int(indice_str)  # Converte a entrada para um número inteiro
            del lista[indice]  # Remove o elemento na posição indicada pelo índice
        except ValueError:
            print('Por favor, digite número inteiro.')  # Trata erro se a entrada não for um número
        except IndexError:
            print('Índice não existe na lista')  # Trata erro se o índice não existir na lista
        except Exception:
            print('Erro desconhecido')  # Trata outros erros desconhecidos
    elif opcao == 'l':  # Se a opção for 'l', o usuário deseja listar os elementos da lista
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do terminal

        if len(lista) == 0:
            print('Nada para listar')  # Mensagem se a lista estiver vazia

        for i, valor in enumerate(lista):  # Percorre a lista e imprime cada elemento com seu índice
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')  # Mensagem para opção inválida
