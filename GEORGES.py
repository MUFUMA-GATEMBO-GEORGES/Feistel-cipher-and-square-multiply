Quetions 1 

Algorithme pour la génération des clés feistel

def feistel_decrypt(ciphertext, k1, k2):
    # Permutation inverse π^(-1) = 51307246
    perm = [5, 1, 3, 0, 7, 2, 4, 6]

    # Appliquer la permutation inverse π^(-1) à ciphertext
    ciphertext = [ciphertext[perm[i]] for i in range(8)]

    # Diviser C en deux blocs de 4 bits : C = G0 || D0
    G0 = ciphertext[:4]
    D0 = ciphertext[4:]

    # Premier Round
    G1 = xor(P_inverse(D0), k2)
    D1 = xor(G0, or(G1, k2))

    # Deuxième Round
    G2 = xor(P_inverse(D1), k1)
    D2 = xor(G1, or(G2, k1))

    # Concaténer les blocs G2 et D2
    plaintext = G2 + D2

    # Appliquer la permutation inverse π^(-1) à plaintext
    plaintext = [plaintext[perm[i]] for i in range(8)]

    return plaintext

# Fonctions auxiliaires

# Fonction de permutation inverse P^(-1) = 2013
def P_inverse(block):
    perm = [2, 0, 1, 3]
    return [block[perm[i]] for i in range(4)]

# Fonction XOR
def xor(block1, block2):
    return [b1 ^ b2 for b1, b2 in zip(block1, block2)]

# Fonction OR
def or(block1, block2):
    return [b1 | b2 for b1, b2 in zip(block1, block2)]

# Exemple d'utilisation
ciphertext = [1, 0, 1, 1, 0, 1, 0, 0]
k1 = [0, 1, 0, 1]
k2 = [1, 0, 1, 0]

plaintext = feistel_decrypt(ciphertext, k1, k2)
print("Plaintext:", plaintext)

Algorithme de chiffrement de feistel

def feistel_encrypt(plaintext, k1, k2):
    # Permutation π = 46027315
    perm = [4, 6, 0, 2, 7, 3, 1, 5]

    # Appliquer la permutation π à plaintext
    plaintext = [plaintext[perm[i]] for i in range(8)]

    # Diviser N en deux blocs de 4 bits : N = G0 || D0
    G0 = plaintext[:4]
    D0 = plaintext[4:]

    # Premier Round
    D1 = xor(P(G0), k1)
    G1 = xor(D0, or(G0, k1))

    # Deuxième Round
    D2 = xor(P(G1), k2)
    G2 = xor(D1, or(G1, k2))

    # Concaténer les blocs G2 et D2
    ciphertext = G2 + D2

    # Appliquer la permutation inverse π^(-1) à ciphertext
    ciphertext = [ciphertext[perm[i]] for i in range(8)]

    return ciphertext

# Fonctions auxiliaires

# Fonction de permutation P = 2013
def P(block):
    perm = [2, 0, 1, 3]
    return [block[perm[i]] for i in range(4)]

# Fonction XOR
def xor(block1, block2):
    return [b1 ^ b2 for b1, b2 in zip(block1, block2)]

# Fonction OR
def or(block1, block2):
    return [b1 | b2 for b1, b2 in zip(block1, block2)]

# Exemple d'utilisation
plaintext = [1, 0, 1, 1, 0, 1, 0, 0]
k1 = [0, 1, 0, 1]
k2 = [1, 0, 1, 0]

ciphertext = feistel_encrypt(plaintext, k1, k2)
print("Ciphertext:", ciphertext)

algorithme de dechiffrement de feistel

def feistel_decrypt(ciphertext, k1, k2):
    # Permutation inverse π^(-1) = 51307246
    perm = [5, 1, 3, 0, 7, 2, 4, 6]

    # Appliquer la permutation inverse π^(-1) à ciphertext
    ciphertext = [ciphertext[perm[i]] for i in range(8)]

    # Diviser C en deux blocs de 4 bits : C = G0 || D0
    G0 = ciphertext[:4]
    D0 = ciphertext[4:]

    # Premier Round
    G1 = xor(P_inverse(D0), k2)
    D1 = xor(G0, or(G1, k2))

    # Deuxième Round
    G2 = xor(P_inverse(D1), k1)
    D2 = xor(G1, or(G2, k1))

    # Concaténer les blocs G2 et D2
    plaintext = G2 + D2

    # Appliquer la permutation inverse π^(-1) à plaintext
    plaintext = [plaintext[perm[i]] for i in range(8)]

    return plaintext

# Fonctions auxiliaires

# Fonction de permutation inverse P^(-1) = 2013
def P_inverse(block):
    perm = [2, 0, 1, 3]
    return [block[perm[i]] for i in range(4)]

# Fonction XOR
def xor(block1, block2):
    return [b1 ^ b2 for b1, b2 in zip(block1, block2)]

# Fonction OR
def or(block1, block2):
    return [b1 | b2 for b1, b2 in zip(block1, block2)]

# Exemple d'utilisation
ciphertext = [1, 0, 1, 1, 0, 1, 0, 0]
k1 = [0, 1, 0, 1]
k2 = [1, 0, 1, 0]

plaintext = feistel_decrypt(ciphertext, k1, k2)
print("Plaintext:", plaintext)

Quetions 2 

def square_and_multiply(base, exponent, modulo):
    # Convertir l'exposant en binaire
    binary_exponent = bin(exponent)[2:]

    # Initialiser le résultat à 1
    result = 1

    # Parcourir les bits de l'exposant de gauche à droite
    for bit in binary_exponent:
        result = (result * result) % modulo  # Carré modulo
        if bit == '1':
            result = (result * base) % modulo  # Multiplication modulo

    return result

# Entrée des valeurs par l'utilisateur
base = int(input("Entrez la valeur de la base : "))
exponent = int(input("Entrez la valeur de l'exposant : "))
modulo = int(input("Entrez la valeur du modulo : "))

# Appel de l'algorithme des carrés et des multiplications
result = square_and_multiply(base, exponent, modulo)
print("Résultat :", result)