'''
 10 // 3  resultado vai ser inteiro
'''
nome = 'Gabriel'
peso = 76
altura = 1.80
IMC = peso / (altura * altura)
print('o IMC do ', nome, ' é ', IMC, '. Ele possui', peso, 'KG, e tem', altura,'m de altura')

# introdução a f-strings. é a possibilidade de colocar variaveis dentro de strings
                                                                        #formatação de decimais
texto = f'{nome} tem {altura}m de altura e pesa {peso}kg, e seu IMC é de {IMC:.3f}'

print(texto)
print(f"{nome} disse oi")