"""
Cifras Sequenciais Síncronas (Synchronous Stream Ciphers)
========================================================

Uma cifra sequencial síncrona é um tipo de cifra de fluxo onde:
- O keystream (fluxo de chave) é gerado de forma INDEPENDENTE da mensagem
- Depende apenas da chave secreta e do IV (Initialization Vector)
- A mesma chave + IV produzem sempre a mesma sequência de keystream
- O erro numa posição do ciphertext não afeta posições subsequentes

Características principais:
✓ Rápidas e eficientes
✓ Adequadas para transmissão em tempo real
✓ Sem erro de propagação
✗ Requer sincronização perfeita entre emissor e receptor
✗ Se o IV for reutilizado, a segurança é comprometida

Exemplos reais:
- RC4 (usado em SSL/TLS, WEP)
- AES em modo CTR
- ChaCha20 (usado em TLS 1.3)

Sugestões de Pesquisa:
    hashlib.md5
    hashlib.sha256

╔════════════════════╦═════════════════╦═════════════════╦══════════════════╗
║ Característica    ║ One-Time Pad    ║ Stream Síncrona ║ Block Cipher     ║
╠════════════════════╬═════════════════╬═════════════════╬══════════════════╣
║ Chave             ║ Aleatória       ║ Pseudo-aleatória║ Pseudo-aleatória ║
║ Comprimento       ║ = mensagem      ║ < mensagem      ║ Blocos fixos      ║
║ Segurança         ║ Perfeita        ║ Dependente PRNG ║ Dependente algo  ║
║ Sincronização     ║ Não necessária  ║ Obrigatória     ║ Não necessária   ║
║ Propagação erro   ║ Não existe      ║ Não existe      ║ Sim              ║
║ Velocidade        ║ Rápida          ║ Muito rápida    ║ Moderada         ║
║ Uso prático       ║ Raro (chaves)   ║ Comum (TLS 1.3) ║ Muito comum      ║
║ Exemplos          ║ Linha Vermelha  ║ RC4, ChaCha20   ║ AES              ║
╚════════════════════╩═════════════════╩═════════════════╩══════════════════╝

✓ VANTAGENS:
  • Muito rápidas (processamento em tempo real)
  • Sem propagação de erro
  • Keystream independente da mensagem
  • Ideais para streaming e comunicação em tempo real

✗ DESVANTAGENS:
  • Exigem sincronização perfeita
  • Vulneráveis à reutilização de Nonce
  • Dependem da qualidade do gerador pseudo-aleatório

📌 REGRA DE OURO:
   Nunca usar a mesma combinação (Chave, Nonce) duas vezes!
   Isto revelaria padrões entre as mensagens.

🔐 APLICAÇÕES MODERNAS:
  • TLS 1.3 (ChaCha20-Poly1305)
  • HTTPS/SSL
  • Streaming de vídeo/áudio encriptado
  • Comunicação satellite e militar
  • Sistemas embarcados (eficiência)

"""

import os
from typing import Tuple, List
import hashlib


# ==================== GERADOR DE KEYSTREAM SIMPLES ====================

class AESCounterModeKeystream:
    """
    Implementação de um gerador de keystream usando AES em modo CTR.
    Este é um modo seguro e amplamente utilizado.
    """
    
    def __init__(self, key: bytes, nonce: bytes):
        """
        Inicializar o gerador CTR.
        
        Args:
            key: Chave secreta (qualquer comprimento)
            nonce: Nonce ou IV (número usado uma única vez)
        """
        # Para este exemplo simplificado, usar SHA256 em vez de AES
        self.key = key
        self.nonce = nonce
        self.counter = 0
    
    def next_byte(self) -> int:
        """Gera o próximo byte do keystream"""
        # Combinar nonce, counter e chave usando SHA256
        combined = self.nonce + self.counter.to_bytes(8, 'big') + self.key
        hash_output = hashlib.sha256(combined).digest()
        
        # Retornar o byte atual do hash
        result = hash_output[self.counter % 32]
        self.counter += 1
        
        return result
    
    def generate_keystream(self, length: int) -> bytes:
        """Gera um keystream com o comprimento especificado"""
        return bytes([self.next_byte() for _ in range(length)])
    
    def reset(self):
        """Reiniciar o contador (reconectar ao início)"""
        self.counter = 0


# ==================== CIFRA SEQUENCIAL SÍNCRONA ====================

class SynchronousStreamCipher:
    """Cifra Sequencial Síncrona genérica"""
    
    def __init__(self, key: bytes, nonce: bytes = None):
        """
        Inicializar a cifra.
        
        Args:
            key: Chave secreta
            nonce: IV (Initialization Vector) - se None, gera um aleatório
        """
        self.key = key
        self.nonce = nonce or os.urandom(8)   
        # Criar gerador de keystream
        self.generator = AESCounterModeKeystream(key, self.nonce)
    
    def encrypt(self, plaintext: str) -> Tuple[bytes, bytes]:
        """
        Encripta uma mensagem.
        
        Args:
            plaintext: Mensagem em claro
            
        Returns:
            Tuplo: (ciphertext, nonce)
        """
        plaintext_bytes = plaintext.encode('utf-8')
        
        # Gerar keystream do mesmo comprimento da mensagem
        keystream = self.generator.generate_keystream(len(plaintext_bytes))
        
        # Aplicar XOR entre plaintext e keystream
        ciphertext = bytes([p ^ k for p, k in zip(plaintext_bytes, keystream)])
        
        return ciphertext, self.nonce
    
    def decrypt(self, ciphertext: bytes, nonce: bytes) -> str:
        """
        Decripta uma mensagem.
        
        Args:
            ciphertext: Mensagem encriptada
            nonce: IV usado na encriptação
            
        Returns:
            str: Mensagem original
        """
        # Para cifras síncronas, decriptação é igual a encriptação!
        # Recriamos o gerador com o mesmo nonce
        generator = AESCounterModeKeystream(self.key, nonce)
        
        # Gerar o mesmo keystream
        keystream = generator.generate_keystream(len(ciphertext))
        
        # Aplicar XOR novamente
        plaintext_bytes = bytes([c ^ k for c, k in zip(ciphertext, keystream)])
        
        return plaintext_bytes.decode('utf-8')


# ==================== DEMONSTRAÇÕES ====================

def exemplo_aes_ctr():
    """Demonstração com AES em modo CTR"""
    print("\n" + "=" * 70)
    print("EXEMPLO 2: Cifra Sequencial Síncrona com AES-CTR")
    print("=" * 70)
    
    # Chave secreta
    chave = b"chave_muito_secreta_e_longa" #b significa bytes, ou seja, conversão do texto para bytes
    mensagem = "CONFIDENCIAL: REUNIAO AMANHA AS 14:00"
    
    print(f"\n1. Chave secreta: {chave}")
    print(f"2. Mensagem original: '{mensagem}'")
    
    # Criar cifra com AES
    cipher = SynchronousStreamCipher(chave)
    print(f"3. Código de inicialiação criado (IV - IV - Initialization Vector): {cipher.nonce.hex()}")
    
    # Encriptar
    ciphertext, nonce = cipher.encrypt(mensagem)
    print(f"\n4. Texto encriptado (hex): {ciphertext.hex()}")
    
    # Decriptar
    plaintext = cipher.decrypt(ciphertext, nonce)
    print(f"\n5. Texto decriptado: '{plaintext}'")

# ==================== EXECUÇÃO PRINCIPAL ====================

if __name__ == "__main__":
    exemplo_aes_ctr()

