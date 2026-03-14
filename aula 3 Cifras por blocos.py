"""
Cifras por Blocos - Modos de Utilização
========================================

Uma cifra por blocos (como AES) divide a mensagem em blocos de tamanho fixo
e encripta cada bloco independentemente. Porém, isto cria problemas de segurança.

Modos de Utilização são esquemas que definem como aplicar a cifra a blocos
para contornar estes problemas e aumentar a segurança.

Modos Comuns:
1. ECB (Electronic Code Book) - Modo simples mas INSEGURO
2. CBC (Cipher Block Chaining) - Encadeamento de blocos (SEGURO)
3. CFB (Cipher Feedback) - Converte block cipher em stream cipher
4. OFB (Output Feedback) - Keystream independente da mensagem

AES Nota: AES é um algoritmo de cifra por blocos que opera em blocos de 128 bits
e não define um modo específico. O modo deve ser escolhido conforme a necessidade.

Comparação detalhada de todos os modos      
          
Comparação de Modos de Utilização de Cifras por Blocos (AES):
╔═══════╦═════════════╦═══════════╦══════════╦═══════════════╦═══════════════╗
║ Modo  ║ IV Req.     ║ Padding   ║ Erro Prop║ Keystream     ║ Uso Recomendado
╠═══════╬═════════════╬═══════════╬══════════╬═══════════════╬═══════════════╣
║ ECB   ║ Não         ║ Sim       ║ Não      ║ Independente  ║ ❌ NUNCA!      ║
║       ║             ║           ║          ║               ║ (Inseguro)     ║
╠═══════╬═════════════╬═══════════╬══════════╬═══════════════╬═══════════════╣
║ CBC   ║ Sim         ║ Sim       ║ Sim      ║ Dependente    ║ ✓ Recomendado  ║
║       ║             ║           ║          ║ plaintext     ║ (Com autenticação)║
╠═══════╬═════════════╬═══════════╬══════════╬═══════════════╬═══════════════╣
║ OFB   ║ Sim         ║ Não       ║ Não      ║ Independente  ║ ✓ Bom para:    ║
║       ║             ║           ║          ║ (stream)      ║ tempo real,    ║
║       ║             ║           ║          ║               ║ sem padding    ║
╠═══════╬═════════════╬═══════════╬══════════╬═══════════════╬═══════════════╣
║ CFB   ║ Sim         ║ Não       ║ Não      ║ Dependente    ║ ✓ Alternativa  ║
║       ║             ║           ║          ║ ciphertext    ║ a OFB          ║
║       ║             ║           ║          ║ (stream)      ║ (com error rec)║
╚═══════╩═════════════╩═══════════╩══════════╩═══════════════╩═══════════════╝

LEGENDA:
• IV Req.: Requer Initialization Vector
• Padding: Requires padding para mensagens não-múltiplos do bloco
• Erro Prop.: Propagação de erro (1 erro afeta múltiplos bytes)
• Keystream: Origem do fluxo de chave

REGRAS DE OURO para cifras por blocos:

1️⃣  NUNCA use ECB em produção!
    ❌ ECB revela padrões
    ❌ Blocos idênticos produzem ciphertexts idênticos
    ❌ Exemplo de insegurança: imagens encriptadas em ECB mostram padrões

2️⃣  USE CBC + HMAC para confidencialidade e integridade
    ✓ CBC é seguro contra ataques comuns
    ✓ HMAC adiciona autenticação
    ✓ Combinação (SHA256) é padrão

3️⃣  USE OFB/CFB para streaming sem padding
    ✓ Não requer padding
    ✓ Sem propagação de erro
    ✓ Bom para comunicação em tempo real

4️⃣  NUNCA reutilize o mesmo (Chave, IV) em CBC
    ⚠️  Mesmo plaintext: diferentes IVs = diferentes ciphertexts (bom)
    ⚠️  Mesmo plaintext: MESMO IV = MESMO ciphertext (mau!)

5️⃣  Use modos autenticados quando possível
    ✓ GCM (Galois/Counter Mode)
    ✓ Combina encriptação e autenticação
    ✓ Detecta modificação

📊 RECOMENDAÇÕES MODERNAS (2024):
    • Para encriptação simétrica: AES-256-CBC + HMAC-SHA256
    • Para streaming: AES-256-CTR ou ChaCha20-Poly1305
    • Para máxima segurança: XChaCha20-Poly1305
    
⚠️  EVITAR:
    • DES (obsoleto)
    • RC4 (vulnerável a ataques)
    • AES com ECB (nunca!)
    • Chaves fracas ou IVs aleatórios fracos

AES é uma cifra por blocos que requer um MODO para funcionar:

🎯 RESUMO FINAL:

ECB ❌
  → Nunca usar em dados reais
  → Apenas para educação
  → Insecure (padrões visíveis)

CBC ✓✓✓
  → Seguro e recomendado
  → Standard em banking e comércio
  → Requer padding PKCS7
  → Requer IV aleatório
  → Requer autenticação (HMAC)

OFB ✓✓
  → Bom para streaming
  → Sem propagação de erro
  → Sem padding
  → Independente da mensagem

CFB ✓✓
  → Alternativa a OFB
  → Keystream depende do ciphertext
  → Sem propagação de erro
  → Sem padding

🔐 AES é seguro quando usado com:
   • Chave forte (256 bits)
   • IV aleatório (para CBC/OFB/CFB)
   • Modo apropriado (CBC, OFB, CFB, GCM)
   • Autenticação (HMAC ou AEAD)
   • Nunca ECB!

"""

from typing import Tuple, List
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib


# ==================== CIFRA DE BLOCO SIMPLIFICADA (EDUCACIONAL) ====================

def simple_block_encrypt(block: bytes, key: bytes) -> bytes:
    """
    Encriptação de bloco simplificada (educacional).
    Substitui cada byte: (byte + key_byte) % 256
    
    Nota: Isto é apenas para demonstração. Em produção, usa-se AES.
    """
    return bytes([(b + k) % 256 for b, k in zip(block, key)])


def simple_block_decrypt(block: bytes, key: bytes) -> bytes:
    """
    Decriptação de bloco simplificada (educacional).
    Inverte: (byte - key_byte) % 256
    """
    return bytes([(b - k) % 256 for b, k in zip(block, key)])


BLOCK_SIZE = 16  # 16 bytes = 128 bits (como AES)


# ==================== MODO ECB (Electronic Code Book) ====================

class ECB_Mode:
    """
    Modo ECB - Electronic Code Book
    
    ⚠️ INSEGURO! Não usar em produção!
    
    Características:
    - Cada bloco é encriptado independentemente
    - Blocos idênticos produzem ciphertexts idênticos
    - Revela padrões na mensagem
    - Não usa IV (Initialization Vector)
    """
    
    def __init__(self, key: bytes):
        # Ajustar chave para tamanho válido de AES (16, 24 ou 32 bytes)
        key_len = len(key)
        if key_len <= 16:
            self.key = hashlib.md5(key).digest()  # 16 bytes
        elif key_len <= 24:
            self.key = hashlib.sha256(key).digest()[:24]  # 24 bytes
        else:
            self.key = hashlib.sha256(key).digest()  # 32 bytes
    
    def encrypt(self, plaintext: str) -> Tuple[bytes, None]:
        """
        Encripta usando ECB.
        
        Args:
            plaintext: Texto em claro
            
        Returns:
            Tuplo: (ciphertext, None) - ECB não usa IV
        """
        plaintext_bytes = plaintext.encode('utf-8')
        
        # Padding PKCS7
        padding_len = BLOCK_SIZE - (len(plaintext_bytes) % BLOCK_SIZE)
        plaintext_bytes += bytes([padding_len] * padding_len)
        
        # Encriptar bloco por bloco
        ciphertext = b''
        for i in range(0, len(plaintext_bytes), BLOCK_SIZE):
            block = plaintext_bytes[i:i+BLOCK_SIZE]
            # Usar AES para cada bloco
            cipher = AES.new(self.key, AES.MODE_ECB)
            encrypted_block = cipher.encrypt(block)
            ciphertext += encrypted_block
        
        return ciphertext, None
    
    def decrypt(self, ciphertext: bytes, _=None) -> str:
        """
        Decripta usando ECB.
        
        Args:
            ciphertext: Texto encriptado
            _: Ignorado (ECB não usa IV)
            
        Returns:
            str: Mensagem original
        """
        plaintext_bytes = b''
        
        # Decriptar bloco por bloco
        for i in range(0, len(ciphertext), BLOCK_SIZE):
            block = ciphertext[i:i+BLOCK_SIZE]
            cipher = AES.new(self.key, AES.MODE_ECB)
            decrypted_block = cipher.decrypt(block)
            plaintext_bytes += decrypted_block
        
        # Remover padding
        padding_len = plaintext_bytes[-1]
        plaintext_bytes = plaintext_bytes[:-padding_len]
        
        return plaintext_bytes.decode('utf-8')


# ==================== MODO CBC (Cipher Block Chaining) ====================

class CBC_Mode:
    """
    Modo CBC - Cipher Block Chaining
    
    ✓ SEGURO - Recomendado
    
    Características:
    - Cada bloco é XORado com o anterior antes de encriptação
    - Requer IV (Initialization Vector)
    - Blocos idênticos produzem ciphertexts diferentes
    - Erro em um bloco afeta os blocos subsequentes (propagação)
    """
    
    def __init__(self, key: bytes):
        # Ajustar chave para tamanho válido de AES (16, 24 ou 32 bytes)
        key_len = len(key)
        if key_len <= 16:
            self.key = hashlib.md5(key).digest()  # 16 bytes
        elif key_len <= 24:
            self.key = hashlib.sha256(key).digest()[:24]  # 24 bytes
        else:
            self.key = hashlib.sha256(key).digest()  # 32 bytes
    
    def encrypt(self, plaintext: str) -> Tuple[bytes, bytes]:
        """
        Encripta usando CBC.
        
        Args:
            plaintext: Texto em claro
            
        Returns:
            Tuplo: (ciphertext, iv)
        """
        plaintext_bytes = plaintext.encode('utf-8')
        iv = os.urandom(BLOCK_SIZE)
        
        # Padding PKCS7
        padding_len = BLOCK_SIZE - (len(plaintext_bytes) % BLOCK_SIZE)
        plaintext_bytes += bytes([padding_len] * padding_len)
        
        # Encriptar bloco por bloco com CB
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(plaintext_bytes)
        
        return ciphertext, iv
    
    def decrypt(self, ciphertext: bytes, iv: bytes) -> str:
        """
        Decripta usando CBC.
        
        Args:
            ciphertext: Texto encriptado
            iv: Initialization Vector usado na encriptação
            
        Returns:
            str: Mensagem original
        """
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext_bytes = cipher.decrypt(ciphertext)
        
        # Remover padding
        padding_len = plaintext_bytes[-1]
        plaintext_bytes = plaintext_bytes[:-padding_len]
        
        return plaintext_bytes.decode('utf-8')


# ==================== MODO OFB (Output Feedback) ====================

class OFB_Mode:
    """
    Modo OFB - Output Feedback
    
    ✓ SEGURO - Stream Cipher baseado em Block Cipher
    
    Características:
    - Converte block cipher em stream cipher
    - Keystream é independente da mensagem/ciphertext
    - Requer IV
    - Sem propagação de erro
    - Não requer padding
    """
    
    def __init__(self, key: bytes):
        # Ajustar chave para tamanho válido de AES (16, 24 ou 32 bytes)
        key_len = len(key)
        if key_len <= 16:
            self.key = hashlib.md5(key).digest()  # 16 bytes
        elif key_len <= 24:
            self.key = hashlib.sha256(key).digest()[:24]  # 24 bytes
        else:
            self.key = hashlib.sha256(key).digest()  # 32 bytes
    
    def encrypt(self, plaintext: str) -> Tuple[bytes, bytes]:
        """
        Encripta usando OFB.
        
        Args:
            plaintext: Texto em claro (qualquer comprimento)
            
        Returns:
            Tuplo: (ciphertext, iv)
        """
        plaintext_bytes = plaintext.encode('utf-8')
        iv = os.urandom(BLOCK_SIZE)
        
        # Usar AES em modo OFB
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        ciphertext = cipher.encrypt(plaintext_bytes)
        
        return ciphertext, iv
    
    def decrypt(self, ciphertext: bytes, iv: bytes) -> str:
        """
        Decripta usando OFB.
        
        Args:
            ciphertext: Texto encriptado
            iv: Initialization Vector usado na encriptação
            
        Returns:
            str: Mensagem original
        """
        cipher = AES.new(self.key, AES.MODE_OFB, iv)
        plaintext_bytes = cipher.decrypt(ciphertext)
        
        return plaintext_bytes.decode('utf-8')


# ==================== MODO CFB (Cipher Feedback) ====================

class CFB_Mode:
    """
    Modo CFB - Cipher Feedback
    
    ✓ SEGURO - Stream Cipher baseado em Block Cipher
    
    Características:
    - Converte block cipher em stream cipher
    - Keystream depende do ciphertext (feedback)
    - Requer IV
    - Sem propagação de erro
    - Não requer padding
    - 1 erro no ciphertext afeta apenas 1 byte do plaintext
    """
    
    def __init__(self, key: bytes):
        # Ajustar chave para tamanho válido de AES (16, 24 ou 32 bytes)
        key_len = len(key)
        if key_len <= 16:
            self.key = hashlib.md5(key).digest()  # 16 bytes
        elif key_len <= 24:
            self.key = hashlib.sha256(key).digest()[:24]  # 24 bytes
        else:
            self.key = hashlib.sha256(key).digest()  # 32 bytes
    
    def encrypt(self, plaintext: str) -> Tuple[bytes, bytes]:
        """
        Encripta usando CFB.
        
        Args:
            plaintext: Texto em claro (qualquer comprimento)
            
        Returns:
            Tuplo: (ciphertext, iv)
        """
        plaintext_bytes = plaintext.encode('utf-8')
        iv = os.urandom(BLOCK_SIZE)
        
        # Usar AES em modo CFB
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        ciphertext = cipher.encrypt(plaintext_bytes)
        
        return ciphertext, iv
    
    def decrypt(self, ciphertext: bytes, iv: bytes) -> str:
        """
        Decripta usando CFB.
        
        Args:
            ciphertext: Texto encriptado
            iv: Initialization Vector usado na encriptação
            
        Returns:
            str: Mensagem original
        """
        cipher = AES.new(self.key, AES.MODE_CFB, iv)
        plaintext_bytes = cipher.decrypt(ciphertext)
        
        return plaintext_bytes.decode('utf-8')


# ==================== DEMONSTRAÇÕES ====================

def exemplo_ecb():
    """Demonstração do modo ECB - Insegurança por padrões"""
    print("=" * 70)
    print("EXEMPLO 1: Modo ECB (Electronic Code Book) - INSEGURO")
    print("=" * 70)
    
    chave = b"chave_secreta_long"
    
    # Mensagem com blocos repetidos
    mensagem = "BLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOA"
    
    print(f"\n1. Chave secreta: {chave}")
    print(f"2. Mensagem original: '{mensagem}'")
    print(f"3. Padrão: 'BLOCOA' repetido 11 vezes")
    
    # Encriptar com ECB
    cipher = ECB_Mode(chave)
    ciphertext, _ = cipher.encrypt(mensagem)
    
    print(f"\n4. Texto encriptado (hex):")
    print(f"   {ciphertext.hex()}")
    
    # Mostrar padrão repetido
    blocksize = 16
    print(f"\n5. Análise de blocos encriptados:")
    for i in range(0, min(80, len(ciphertext)), 16):
        block = ciphertext[i:i+16].hex()
        print(f"   Bloco {i//16}: {block}")
    print("O bloco 3b77f02f25530a93d4099c302fb6d988 repete-se provando que exite um padrão, ou seja, não é seguro!")
    
    print(f"\n5. ⚠️  PROBLEMA: Blocos encriptados repetidos!")
    print(f"   Padrões na mensagem original são visíveis no ciphertext!")
    
    # Decriptar
    plaintext = cipher.decrypt(ciphertext, None)
    print(f"\n6. Texto decriptado: '{plaintext}'")


def exemplo_cbc():
    """Demonstração do modo CBC - Seguro"""
    print("\n" + "=" * 70)
    print("EXEMPLO 2: Modo CBC (Cipher Block Chaining) - SEGURO")
    print("=" * 70)
    
    chave = b"chave_secreta_long"
    
    # Mesma mensagem que em ECB
    mensagem = "BLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOABLOCOAB"
    
    print(f"\n1. Chave secreta: {chave}")
    print(f"2. Mensagem original: '{mensagem}'")
    print(f"3. Padrão: 'BLOCOA' repetido 11 vezes")
    
    # Encriptar com CBC
    cipher = CBC_Mode(chave)
    ciphertext, iv = cipher.encrypt(mensagem)
    
    print(f"\n4. IV (Initialization Vector): {iv.hex()}")
    print(f"5. Texto encriptado (hex):")
    print(f"   {ciphertext.hex()}")
    
    # Mostrar que não há padrão repetido
    print(f"\n6. Análise de blocos encriptados:")
    for i in range(0, min(80, len(ciphertext)), 16):
        block = ciphertext[i:i+16].hex()
        print(f"   Bloco {i//16}: {block}")
    
    print(f"\n7. ✓ SEGURANÇA: Mesmo padrão no plaintext produz ciphertexts diferentes!")
    print(f"   Padrões não são visíveis no ciphertext!")
    
    # Decriptar
    plaintext = cipher.decrypt(ciphertext, iv)
    print(f"\n8. Texto decriptado: '{plaintext}'")


def exemplo_ofb():
    """Demonstração do modo OFB - Stream Cipher"""
    print("\n" + "=" * 70)
    print("EXEMPLO 3: Modo OFB (Output Feedback) - SEGURO")
    print("=" * 70)
    
    chave = b"chave_secreta_long"
    mensagem = "MENSAGEM_SECRET_1MENSAGEM_SECRET_2"
    
    print(f"\n1. Chave secreta: {chave}")
    print(f"2. Mensagem original: '{mensagem}'")
    
    # Encriptar com OFB
    cipher = OFB_Mode(chave)
    ciphertext, iv = cipher.encrypt(mensagem)
    
    print(f"\n3. Código de inicialiação criado (IV - Initialization Vector): {iv.hex()}")
    print(f"4. Texto encriptado (hex): {ciphertext.hex()}")
    
    # Decriptar
    plaintext = cipher.decrypt(ciphertext, iv)
    print(f"\n5. Texto decriptado: '{plaintext}'")
    
    # Propriedades do OFB
    print(f"\n6. Propriedades do OFB:")
    print(f"   • Keystream gerado independentemente")
    print(f"   • Sem propagação de erro")
    print(f"   • Pode encriptar qualquer comprimento")


def exemplo_cfb():
    """Demonstração do modo CFB - Stream Cipher com feedback"""
    print("\n" + "=" * 70)
    print("EXEMPLO 4: Modo CFB (Cipher Feedback) - SEGURO")
    print("=" * 70)
    
    chave = b"chave_secreta_long"
    mensagem = "TRANSMISSAO_DE_DADOSCRIPTOGRAFADOS"
    
    print(f"\n1. Chave secreta: {chave}")
    print(f"2. Mensagem original: '{mensagem}'")
    
    # Encriptar com CFB
    cipher = CFB_Mode(chave)
    ciphertext, iv = cipher.encrypt(mensagem)
    
    print(f"\n3. Código de inicialiação criado (IV - Initialization Vector): {iv.hex()}")
    print(f"4. Texto encriptado (hex): {ciphertext.hex()}")
    
    # Decriptar
    plaintext = cipher.decrypt(ciphertext, iv)
    print(f"\n5. Texto decriptado: '{plaintext}'")
    
    # Propriedades do CFB
    print(f"\n6. Propriedades do CFB:")
    print(f"   • Keystream depende do ciphertext (feedback)")
    print(f"   • Sem propagação de erro")
    

# ==================== EXECUÇÃO PRINCIPAL ====================

if __name__ == "__main__":
        #exemplo_ecb()
        #exemplo_cbc()
        #exemplo_ofb()
        exemplo_cfb()
