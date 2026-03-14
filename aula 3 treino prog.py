
'''
1.1 - Olá Mundo: Escreva um programa que exiba a mensagem "Olá,
Mundo!" no ecrã.
'''
#print("Olá, Mundo!")

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
#variaveis
nota1 = float(input("Digite a primeira nota: "))   
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas é: {media:.3f}")
print("Media: ",(nota1 + nota2 + nota3) / 3)


