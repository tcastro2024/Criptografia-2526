"""
One-Time Pad (OTP) - Algoritmo de Criptografia
----------------------------------------------
O One-Time Pad é um método de criptografia (teoricamente inquebrável)
que utiliza uma chave aleatória do mesmo tamanho da mensagem.

Características:
- Chave: sequência aleatória do mesmo comprimento da mensagem
- Operação: XOR (ou Adição Modular)
- Segurança: Perfeita se a chave for verdadeiramente aleatória e usada apenas uma vez
- Desvantagem: A chave deve ser tão longa quanto a mensagem

✓ VANTAGENS:
  • Segurança teórica perfeita (Teorema de Shannon)
  • Simples de implementar
  • Impossível quebrar sem a chave

✗ DESVANTAGENS:
  • A chave deve ser tão longa quanto a mensagem
  • A chave deve ser verdadeiramente aleatória
  • A chave deve ser util apenas uma vez
  • Difícil de gerir chaves longas e aleatórias
  • Impossível detectar erros de transmissão

APLICAÇÕES PRÁTICAS:
  • Comunicações diplomáticas secretas (Linha Vermelha)
  • Espionagem e operações militares
  • Hoje em dia: substitui-se por criptografia de chave pública

"""

import os
import random
from typing import Tuple

# ==================== Utilizando Adição Modular (Mod 26) ====================
# Aplicável para texto apenas (letras A-Z)

def encriptar_aditivo(mensagem: str, chave: list) -> list:
    """
    Encripta uma mensagem usando adição modular (módulo 26 para letras).
    
    Args:
        mensagem: Texto em claro (apenas letras)
        chave: Lista de números aleatórios (0-25)
    
    Returns:
        list: Texto encriptado como números
    """
    mensagem = mensagem.upper().replace(" ", "")
    
    if len(chave) < len(mensagem):
        raise ValueError(f"Chave insuficiente: {len(chave)} < {len(mensagem)}")
    
    ciphertext = []
    for i, letra in enumerate(mensagem):
        if letra.isalpha():
            # Converter letra para número (A=0, B=1, ..., Z=25)
            pos_letra = ord(letra) - ord('A')
            # Aplicar adição modular: (posição + chave) mod 26
            pos_encriptada = (pos_letra + chave[i]) % 26
            ciphertext.append(pos_encriptada)
    
    return ciphertext


def decriptar_aditivo(ciphertext: list, chave: list) -> str:
    """
    Decripta uma mensagem encriptada com adição modular.
    
    Args:
        ciphertext: Lista de números encriptados
        chave: Lista de números aleatórios (0-25)
    
    Returns:
        str: Mensagem original em claro
    """
    if len(chave) < len(ciphertext):
        raise ValueError(f"Chave insuficiente: {len(chave)} < {len(ciphertext)}")
    
    plaintext = []
    for i, numero in enumerate(ciphertext):
        # Inverter adição modular: (número - chave) mod 26
        pos_original = (numero - chave[i]) % 26
        # Converter número para letra
        letra = chr(pos_original + ord('A'))
        plaintext.append(letra)
    
    return ''.join(plaintext)


# ==================== TESTES E EXEMPLOS ====================

def exemplo_aditivo():
    """Demonstração do One-Time Pad com Adição Modular"""
    print("\n" + "=" * 60)
    print("EXEMPLO 2: One-Time Pad com Adição Modular (Mod 26)")
    print("=" * 60)
    
    # Mensagem a encriptar
    #mensagem = "SEGURANCAINFORMATICA"
    mensagem = input("Digite a mensagem a encriptar (apenas letras): ")
    print(f"\n1. Mensagem original: '{mensagem}'")
    
    # Gerar chave aleatória (números de 0-25)
    chave = [random.randint(0, 25) for _ in range(len(mensagem))]
    print(f"2. Chave aleatória (números de 0-25):")
    print(f"   {chave}")
    
    # Encriptação
    ciphertext = encriptar_aditivo(mensagem, chave)
    #print(f"\n3. Texto encriptado (números):")
    #print(f"   {ciphertext}")
    
    # Converter para letras para visualização
    ciphertext_letras = ''.join([chr(num + ord('A')) for num in ciphertext])
    print(f"Texto encriptado: '{ciphertext_letras}')")
    
    # Decriptação
    plaintext = decriptar_aditivo(ciphertext, chave)
    print(f"\n4. Texto decriptado: '{plaintext}'")
    
    # Verificação
    #print(f"\n5. Verificação: {mensagem} == {plaintext}? {mensagem == plaintext}")


# ==================== EXECUÇÃO PRINCIPAL ====================

if __name__ == "__main__":
    exemplo_aditivo()
