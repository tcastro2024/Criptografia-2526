# RSA

import rsa

# Gerar chaves
(public_key, private_key) = rsa.newkeys(512)

print("Criptografia Assimetric utilizando RSA\n")

mensagem = input("Digite a mensagem a ser criptografada por RSA: ")

# Criptografar a mensagem
mensagem_criptografada = rsa.encrypt(mensagem.encode(), public_key)

# Descriptografar a mensagem
mensagem_descriptografada = rsa.decrypt(mensagem_criptografada, private_key).decode()

print("Chaves:")
print("Chave pública:", public_key)
print("Chave privada:", private_key)

print("Mensagem original:", mensagem, ", Tamanho:", len(mensagem))
print("Mensagem criptografada:", mensagem_criptografada, ", Tamanho:", len(mensagem_criptografada))
print("Mensagem descriptografada:", mensagem_descriptografada, ", Tamanho:", len(mensagem_descriptografada))

print("Teste de erro com RSA, utiliar a chave publica para encriptar e descriptografar a mensagem criptografada:")

try:
    mensagem_descriptografada_erro = rsa.decrypt(mensagem_criptografada, public_key).decode()
    print("Mensagem descriptografada com chave pública (deve falhar):", mensagem_descriptografada_erro)
except Exception as e:
    print("Erro ao descriptografar com chave pública (esperado):", e)   