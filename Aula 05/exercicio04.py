# Exercicio 4
# Escreva um programa que peça a nota de um aluno
# 
# Se a nota for 7 ou mais deve aparecer a mensagem: "Aprovado"
# 
# Caso contrário deve aparecer a mensagem: "Reprovado"

notaAluno = float(input("Digite a nota do aluno(a): "))

if notaAluno >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")