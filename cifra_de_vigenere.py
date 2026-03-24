"""
Cifra de Vigenère - Algoritmo de Criptografia
================================================

A Cifra de Vigenère é uma generalização da Cifra de César que utiliza
uma chave com múltiplos caracteres para encriptar mensagens.

FUNCIONAMENTO:
- Cada letra da mensagem é deslocada por um valor diferente
- O valor de deslocamento é determinado pela chave (que se repete)
- Cada letra da chave define o deslocamento para a letra correspondente

EXEMPLO PRÁTICO (funciona por matriz de letras):
    Mensagem: ATACARAAMANHA
    Chave:    SENHASENHASE
    
    A(+S): A + 18 = S
    T(+E): T + 4 = X
    A(+N): A + 13 = N
    ...

VANTAGENS:
✓ Mais segura que a Cifra de César (não tem padrões fixos)
✓ Simples de implementar
✓ Chave pode ser uma palavra fácil de memorizar

DESVANTAGENS:
✗ Vulnerável à análise de frequência se a chave for curta
✗ Análise de Kasiski pode quebrar a cifra

⚠️  SEGURANÇA:
  • A força depende do comprimento e aleatoriedade da chave
  • Nunca reutilizar a mesma chave para muitas mensagens
  • Usar chaves longas e aleatórias para melhor segurança

💡 CURIOSIDADE:
  • Usada por militares durante séculos
  • Quebrada por Friedrich Kasiski em 1863
  • Hoje substitui-se por criptografia moderna (RSA, AES, etc.)
"""

# ==================== FUNÇÕES AUXILIARES ====================

def processar_chave(chave: str) -> list:
    """
    Converte a chave (texto) em números (0-25).
    
    Exemplo:
        "SENHA" → [18, 4, 13, 7, 0]
        
    Args:
        chave: String com a chave (ex: "SENHA")
    
    Returns:
        list: Lista de números de 0-25 representando os deslocamentos
    """
    chave = chave.upper().replace(" ", "")
    chave_numeros = []
    
    for letra in chave:
        if letra.isalpha():
            # Converter letra para número (A=0, B=1, ..., Z=25)
            numero = ord(letra) - ord('A')
            chave_numeros.append(numero)
    
    return chave_numeros


def expandir_chave(chave_numeros: list, tamanho_mensagem: int) -> list:
    """
    Expande a chave para ter o mesmo comprimento da mensagem.
    A chave repete-se conforme necessário.
    
    Exemplo:
        chave_numeros = [18, 4, 13, 7, 0]  # "SENHA"
        tamanho_mensagem = 13
        resultado = [18, 4, 13, 7, 0, 18, 4, 13, 7, 0, 18, 4, 13]
    
    Args:
        chave_numeros: Chave convertida em números
        tamanho_mensagem: Comprimento da mensagem
    
    Returns:
        list: Chave expandida repetida
    """
    chave_expandida = []
    
    for i in range(tamanho_mensagem):
        # Modulo para repetir a chave
        indice_chave = i % len(chave_numeros)
        chave_expandida.append(chave_numeros[indice_chave])
    
    return chave_expandida


# ==================== ENCRIPTAÇÃO ====================

def encriptar_vigenere(mensagem: str, chave: str) -> str:
    """
    Encripta uma mensagem usando a Cifra de Vigenère.
    
    Processo:
    1. Converter chave em números
    2. Expandir chave para o tamanho da mensagem
    3. Para cada letra da mensagem:
       - Obter a posição (A=0, Z=25)
       - Somar o valor da chave (módulo 26)
       - Converter de volta para letra
    
    Fórmula: C[i] = (M[i] + K[i]) mod 26
    
    Args:
        mensagem: Texto a encriptar (ex: "ATACARAAMANHA")
        chave: Chave para encriptação (ex: "SENHA")
    
    Returns:
        str: Mensagem encriptada (maiúsculas, sem espaços)
    """
    # Processar entrada
    mensagem = mensagem.upper().replace(" ", "")
    chave_numeros = processar_chave(chave)
    
    # Validar
    if len(chave_numeros) == 0:
        raise ValueError("A chave deve conter pelo menos uma letra!")
    
    # Expandir chave
    chave_expandida = expandir_chave(chave_numeros, len(mensagem))
    
    # Encriptar
    mensagem_encriptada = []
    
    for i, letra in enumerate(mensagem):
        if letra.isalpha():
            # Converter letra para número (A=0, B=1, ..., Z=25)
            pos_letra = ord(letra) - ord('A')
            
            # Aplicar deslocamento da chave
            pos_encriptada = (pos_letra + chave_expandida[i]) % 26
            
            # Converter de volta para letra
            letra_encriptada = chr(pos_encriptada + ord('A'))
            mensagem_encriptada.append(letra_encriptada)
    
    return ''.join(mensagem_encriptada)


# ==================== DECRIPTAÇÃO ====================

def decriptar_vigenere(mensagem_encriptada: str, chave: str) -> str:
    """
    Decripta uma mensagem encriptada com a Cifra de Vigenère.
    
    Processo (inverso da encriptação):
    1. Converter chave em números
    2. Expandir chave para o tamanho da mensagem
    3. Para cada letra da mensagem encriptada:
       - Obter a posição (A=0, Z=25)
       - Subtrair o valor da chave (módulo 26)
       - Converter de volta para letra
    
    Fórmula: M[i] = (C[i] - K[i]) mod 26
    
    Args:
        mensagem_encriptada: Texto encriptado (ex: "SXUCFXFFKFBQF")
        chave: Chave para decriptação (mesma usada na encriptação)
    
    Returns:
        str: Mensagem original em claro
    """
    # Processar entrada
    mensagem_encriptada = mensagem_encriptada.upper().replace(" ", "")
    chave_numeros = processar_chave(chave)
    
    # Validar
    if len(chave_numeros) == 0:
        raise ValueError("A chave deve conter pelo menos uma letra!")
    
    # Expandir chave
    chave_expandida = expandir_chave(chave_numeros, len(mensagem_encriptada))
    
    # Decriptar
    mensagem_original = []
    
    for i, letra in enumerate(mensagem_encriptada):
        if letra.isalpha():
            # Converter letra para número (A=0, B=1, ..., Z=25)
            pos_letra = ord(letra) - ord('A')
            
            # Remover deslocamento da chave (operação inversa)
            pos_original = (pos_letra - chave_expandida[i]) % 26
            
            # Converter de volta para letra
            letra_original = chr(pos_original + ord('A'))
            mensagem_original.append(letra_original)
    
    return ''.join(mensagem_original)


# ==================== EXEMPLO ====================


def interface_interativa():
    """Interface interativa para encriptação e decriptação"""
    print("\n" + "=" * 70)
    print("INTERFACE INTERATIVA - Cifra de Vigenère")
    print("=" * 70)
    
    while True:
        print(f"\n🔐 Escolha uma operação:")
        print(f"   1. Testar cifra de Vigenère")
        print(f"   2. Sair")
        
        opcao = input(f"\nInsira o número (1-2): ").strip()
        
        if opcao == "1":
            mensagem = input(f"Insira o texto a encriptar: ").strip()
            chave = input(f"Insira a chave: ").strip()
            
            if mensagem and chave:
                resultado = encriptar_vigenere(mensagem, chave)
                print(f"\n✅ ENCRIPTADO: '{resultado}'")
                resultado = decriptar_vigenere(resultado, chave)
                print(f"\n✅ DECRIPTADO: '{resultado}'")
            else:
                print(f"\n❌ Erro: Preencha todos os campos!")
        
        elif opcao == "2":
            print(f"\n👋 Até à próxima!")
            break
        
        else:
            print(f"\n❌ Opção inválida! Escolha 1 ou 2.")


# ==================== EXECUÇÃO PRINCIPAL ====================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("CIFRA DE VIGENÈRE - Criptografia com Chave Repetida")
    print("=" * 70)
    interface_interativa()

