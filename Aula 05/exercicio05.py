# Exercicio 5
# Faça um programa que peça uma senha ao usuário.
# 
# Se a senha for igual a "Abacaxi" deve aparecer a mensagem "Entrada liberada"
# 
# Caso contrário deve aparecer a mensagem "Senha incorreta"

senhaUsuario = str(input("Digite a senha: "))
if senhaUsuario == 'Abacaxi':
    print("Entrada Liberada!")
else:
    print("Senha Incorreta")