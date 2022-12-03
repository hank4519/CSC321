import random
from Crypto.Hash import SHA256

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def part1():
    p = 37
    g = 5

    # alice
    x_alice = random.randint(1, p-2)
    y_alice = pow(g, x_alice, p)  # sent to mal

    # mal
    x_mal_bob = random.randint(1, p-2)
    y_mal_bob = pow(g, x_mal_bob, p)  # sent to bob

    # bob
    x_bob = random.randint(1, p-2)
    y_bob = pow(g, x_bob) % p
    k_bob = pow(y_mal_bob, x_bob, p)  # sent to mal

    # mal
    x_mal_alice = random.randint(1, p-2)
    k_mal_bob = pow(y_bob, x_mal_bob) % p
    y_mal_alice = pow(g, x_mal_alice) % p  # sent to alice
    k_mal_alice = pow(y_alice, x_mal_alice, p)

    # alice
    k_alice = pow(y_mal_alice, x_alice, p)
    k = SHA256.new()
    k.update(bytes(k_alice))
    key_alice = bytes(k.hexdigest()[0:16], encoding='utf8')
    iv = get_random_bytes(16)
    cipher_alice = AES.new(key_alice, AES.MODE_CBC, iv)
    message_alice = pad(bytes("Hi Bob!", encoding='utf8'), AES.block_size)
    ciphertext_alice = cipher_alice.encrypt(message_alice)  # sent to mal

    # mal
    k = SHA256.new()
    k.update(bytes(k_mal_alice))
    key_mal_alice = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_mal_alice = AES.new(key_mal_alice, AES.MODE_CBC, iv)
    mal_decrypt_alice = cipher_mal_alice.decrypt(ciphertext_alice)
    print("Mal decrypts Alice's message: ", end="")
    print(unpad(mal_decrypt_alice, AES.block_size))  # mal decrypts alice's 's message

    k = SHA256.new()
    k.update(bytes(k_mal_bob))
    key_mal_bob = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_mal_bob = AES.new(key_mal_bob, AES.MODE_CBC, iv)
    ciphertext_mal_bob = cipher_mal_bob.encrypt(pad(bytes("Hi Bob!", encoding="utf8"), AES.block_size))  # sent to bob

    # bob
    k = SHA256.new()
    k.update(bytes(k_bob))
    key_bob = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_bob = AES.new(key_bob, AES.MODE_CBC, iv)
    bob_decrypt_mal = cipher_bob.decrypt(ciphertext_mal_bob)
    print("Bob decrypts Mal's message: ", end="")
    print(unpad(bob_decrypt_mal, AES.block_size))  # bob decrypts alice's 's message

    k = SHA256.new()
    k.update(bytes(k_bob))
    key_bob = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_bob = AES.new(key_bob, AES.MODE_CBC, iv)
    message_bob = pad(bytes("Hi Alice!", encoding='utf8'), AES.block_size)
    ciphertext_bob = cipher_bob.encrypt(message_bob)  # sent to mal

    # mal
    k = SHA256.new()
    k.update(bytes(k_mal_bob))
    key_mal_bob_1 = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_mal_bob_1 = AES.new(key_mal_bob_1, AES.MODE_CBC, iv)
    mal_decrypt_bob = cipher_mal_bob_1.decrypt(ciphertext_bob)
    print("Mal decrypts Bob's message: ", end="")
    print(unpad(mal_decrypt_bob, AES.block_size))  # Mal decrypts Bob's 's message

    k = SHA256.new()
    k.update(bytes(k_mal_alice))
    key_mal_bob_1 = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_mal_alice_1 = AES.new(key_mal_bob_1, AES.MODE_CBC, iv)
    ciphertext_mal_alice_1 = cipher_mal_alice_1.encrypt(
        pad(bytes("Hi Alice!", encoding="utf8"), AES.block_size))  # sent to alice

    # alice
    k = SHA256.new()
    k.update(bytes(k_alice))
    key_alice_1 = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_alice_1 = AES.new(key_alice_1, AES.MODE_CBC, iv)
    alice_decrypt_mal = cipher_alice_1.decrypt(ciphertext_mal_alice_1)
    print("Alice decrypts Mal's message: ", end="")
    print(unpad(alice_decrypt_mal, AES.block_size))  # Mal decrypts Bob's 's message
    print("Done with tampering A and B\n\n")


def part2():
    p = 37
    g = 1

    # alice
    x_alice = random.randint(1, p-2)
    y_alice = pow(g, x_alice, p)  # sent to mal

    # bob
    x_bob = random.randint(1, p-2)
    y_bob = pow(g, x_bob, p)
    k_bob = pow(y_alice, x_bob, p)  # sent to mal

    # alice
    k_alice = pow(y_bob, x_alice, p)
    k = SHA256.new()
    k.update(bytes(k_alice))
    key_alice = bytes(k.hexdigest()[0:16], encoding='utf8')
    iv = get_random_bytes(16)
    cipher_alice = AES.new(key_alice, AES.MODE_CBC, iv)
    message_alice = pad(bytes("Hi Bob!", encoding='utf8'), AES.block_size)
    ciphertext_alice = cipher_alice.encrypt(message_alice)  # sent to mal
    print("Alice sends ciphertext: ", end="")
    print(ciphertext_alice)

    # mal
    k = SHA256.new()
    k.update(bytes(1))
    key_mal = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_mal = AES.new(key_mal, AES.MODE_CBC, iv)
    mal_decrypt_alice = cipher_mal.decrypt(ciphertext_alice)
    print("Mal decrypts Alice's message: ", end="")
    print(unpad(mal_decrypt_alice, AES.block_size))  # mal decrypts alice's 's message

    # bob
    k = SHA256.new()
    k.update(bytes(k_bob))
    key_bob = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_bob = AES.new(key_bob, AES.MODE_CBC, iv)
    message_bob = pad(bytes("Hi Alice!", encoding='utf8'), AES.block_size)
    ciphertext_bob = cipher_bob.encrypt(message_bob)  # sent to mal
    print("Bob sends ciphertext: ", end="")
    print(cipher_bob)

    # mal
    k = SHA256.new()
    k.update(bytes(1))
    key_mal = bytes(k.hexdigest()[0:16], encoding='utf8')
    cipher_mal = AES.new(key_mal, AES.MODE_CBC, iv)
    mal_decrypt_bob = cipher_mal.decrypt(ciphertext_bob)
    print("Mal decrypts Bob's message: ", end="")
    print(unpad(mal_decrypt_bob, AES.block_size))  # mal decrypts alice's 's message
    print("Done with setting p = 1")


if __name__ == "__main__":

    part1()
    part2()
