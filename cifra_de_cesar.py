def encriptar_cifra_de_cesar(texto, chave_da_cifra):
    texto_encriptado = ""
    for char in texto:
        if char.isalpha(): # Verifica se o caractere é uma letra do alfabeto
            Caracteres_de_texto_encriptado = chr((ord(char) #Converte o caractere char em seu valor Unicode (ou ASCII). Por exemplo, ord('a') retorna 97 e ord('A') retorna 65.
                                - ord('a' if char.islower() else 'A') #retorna VERDADEIRO se a letra for minuscula ou FALSO CASO CONTRARIO
                                + chave_da_cifra) % 26 # Aplica o operador módulo 26 para garantir que o resultado esteja no intervalo de 0 a 25, o que corresponde às 26 letras do alfabeto. Isso é importante para o wrap-around; por exemplo, se a soma ultrapassar 25 (como 25 + 3), o módulo garantirá que voltamos ao início do alfabeto (neste caso, 28 % 26 = 2)
                                + ord('a' if char.islower() else 'A'))
            texto_encriptado += Caracteres_de_texto_encriptado
        else:
            texto_encriptado += char
    return texto_encriptado

def desencriptar_cifra_de_cesar(texto, chave_da_cifra):
    return encriptar_cifra_de_cesar(texto, -chave_da_cifra)

parar_programa = 0
while parar_programa == 0:
    # texto_cifrado = "Teste cifra de cesar"
    # chave_da_cifra = 3

    texto_cifrado = input("Insira o texto a encriptar: ")
    chave_da_cifra = int(input("Insira o valor da chave: "))

    print("\nENCRIPTAR: ")
    mensagem_encriptada = encriptar_cifra_de_cesar(texto_cifrado, chave_da_cifra)
    print("Mensagem cifrada:", mensagem_encriptada)

    print("\nDESENCRIPTAR: ")
    mensagem_desencriptada = desencriptar_cifra_de_cesar(mensagem_encriptada, chave_da_cifra)
    print("Mensagem decifrada:", mensagem_desencriptada)

    parar_programa = int(input("\nInsira 0 para continuar ou 1 para parar: "))

print("Programa parou!")