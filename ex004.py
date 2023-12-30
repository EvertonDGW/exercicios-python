nome = input('qual o seu nome:')
print('prazer em te conhecer {:=^20}'.format(nome)) # {:20} vai fazer o nome digitado aparecer em 20 caracteres
                                                    # {:>20} o sinal de maior vai fazer com que o nome digitado se mova 20 caracteres para direita
                                                    # {:<20} o sinal de menor vai fazer com que o nome digitado se mova 20 caracteres para esquerda
                                                    # {:^20} o sinal de circunflexo vai fazer com que o nome digitado fique centralizado em 20 caracteres
                                                    # {:=^20} vai centralizar e a redor vai colocar o sinal de (=) repetidamente 