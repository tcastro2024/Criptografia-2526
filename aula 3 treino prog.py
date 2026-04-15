
'''
1.1 - Olá Mundo: Escreva um programa que exiba a mensagem "Olá,
Mundo!" no ecrã.
'''
''' 
print("Olá, Mundo!")

nome = "Andre"
idade = 45

print(f"Olá, {nome}! Você tem {idade} anos.")

a = 5
b = 3

soma = a + b
print(f"A soma de {a} e {b} é: {soma}")

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é pode ir a um evento.")
elif idade < 18 and idade >= 16:
    print("Você pode ir a um evento, mas precisa de um responsável.")
else:
    print("Você não pode ir a um evento.")

for i in range(1, 6, 2):
    print(i)

nota = 0


# 0 != -1 -> verdade
while nota != -1:
    #entra no while
    #pedimos uma nota ao utilizador
    nota = float(input("Digite uma nota ou -1 para sair: "))

    if nota == -1:
        break

    print("Classifica notas:")
    if nota < 10:
        print("Nota negativa.")
    elif nota >= 10 and nota < 14:
        print("Nota satisfatória.")
    elif nota >= 14 and nota < 18:
        print("Nota muito boa.")
    elif nota >= 18 and nota <= 20:
        print("Nota excelente.")
    else:
        print("Nota inválida!")


frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]
for fruta in frutas:
    print(fruta)


def saudacao(nome):
    return f"Olá, {nome}!"


def classificar_nota(nota):
    if nota < 10:
        return "Nota negativa."
    elif nota >= 10 and nota < 14:
        return "Nota satisfatória."
    elif nota >= 14 and nota < 18:
        return "Nota muito boa."
    elif nota >= 18 and nota <= 20:
        return "Nota excelente."
    else:
        return "Nota inválida!"

quantidade_notas = int(input("Digite a quantidade de notas a serem classificadas: "))   

for i in range(1, quantidade_notas + 1):
    nota = float(input(f"Digite a nota {i}: "))
    print(classificar_nota(nota))


print(saudacao("Carlos"))
print(classificar_nota(nota))

'''
'''
1.2 - Soma de Dois Números: Escreva um programa que solicite ao
utilizador que insira dois números e, em seguida, exiba a soma desses
números.
'''
#numero1 = float(input("Digite o primeiro número: "))
#numero2 = float(input("Digite o segundo número: "))
#numero1 = 5.0
#numero2 = 3.0 comentario apenas uma linha

'''
comentario multiplas linhas
'''
#soma = numero1 + numero2
#print(f"A soma dos números é: {soma}")
#print("A soma dos números é: " + str(soma)) # o str() é para converter o numero em string para concatenar com a mensagem

'''
1.3 - Calculadora Simples: Crie uma calculadora que permita ao utilizador
realizar operações de adição, subtração, multiplicação e divisão com dois
números inseridos.
'''
'''
# cria variaveis
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")   
# operacao é a mesma coisa que uma variavel do tipo string/cordas
# ou seja, texto
#numero1 = 10
#numero2 = 5    
#operacao = "*" # exemplo de operação, pode ser +, -, *, /

# * == +
if operacao == "+":
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    resultado = numero1 / numero2
    print(f"O resultado da divisão é: {resultado}")
else:
    print("Operação inválida!")

print("Fim do programa.")
'''
'''
1.4 - Média de Notas: Escreva um programa que calcule a média de três
notas inseridas pelo utilizador
'''
''' 
#variaveis
nota1 = float(input("Digite a primeira nota: "))   
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.3f}")
print("Media: ",(nota1 + nota2 + nota3) / 3)

# Utilizando uma função/método para calcular a média
def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    return media

media = calcular_media(nota1, nota2, nota3)
print(f"A média das notas é: {media:.3f}")
'''
'''
1.5 - Contagem Regressiva: Crie um programa que conte de 10 até 1 e, em
seguida, exiba a mensagem "Feliz Ano Novo!".
'''

# Contagem regressiva
# o range() é uma função que gera uma sequência de números,
#  o primeiro argumento é o início da sequência, 
# o segundo argumento é o fim da sequência (não incluído)
#  e o terceiro argumento é o passo (incremento ou decremento). No caso, estamos contando de 10 até 1,
#  então o início é 10, o fim é 0 (não incluído) e o passo é -1 (decremento).
''' 
for i in range(10, 0, -1): 
    print(i)        
print("Feliz Ano Novo!")
'''

'''
1.6 - Verificação de Número Par ou Ímpar: Escreva um programa que peça
ao utilizador para inserir um número e determine se ele é par ou ímpar.
'''
# Verificação de número par ou ímpar
'''
numero = int(input("Digite um número: "))
if numero % 2 == 0: # o operador % é o operador de módulo, que retorna o resto da divisão
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
    '''

'''
1.7 - Tabuada de Multiplicação: Crie um programa que peça ao utilizador
para inserir um número e, em seguida, exiba a tabuada de multiplicação
desse número.
'''
'''
i = 0

numero = int(input("Digite um número para ver a tabuada: "))

print(f"Tabuada de {numero}:")
while i < 10:
    i += 1
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
'''
''''
1.8 - Conversor de Temperatura: Escreva um programa que permita ao
utilizador converter uma temperatura de graus Celsius para Fahrenheit ou
de Fahrenheit para graus Celsius, dependendo da escolha do utilizador.
'''
'''
# 0º C = 32º F
celsius = float(input("Digite a temperatura em Celsius: ")) 
#"45.7" o float vai converter para um número real/decimal

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
'''

'''
1.9 - Adivinhar o Número: Crie um jogo onde o programa escolhe um
número aleatório entre 1 e 100. O utilizador deve tentar adivinhar o
número. O programa deve fornecer dicas sobre se o palpite do utilizador é
muito alto ou muito baixo

'''
import random

numero_secreto = random.randint(1, 100) # gera um número aleatório entre 1 e 100
tentativa = 0
while tentativa != -1:
    palpite = int(input("Digite seu palpite (entre 1 e 100) ou -1 para desistir: "))
    tentativa += 1

    if palpite < numero_secreto:
        print("Muito baixo! Tente novamente.")
    elif palpite > numero_secreto:
        print("Muito alto! Tente novamente.")
    else:
        print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativa} tentativas.")
        break