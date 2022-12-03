#CSC 321, Lab 2 (part 2), Hank Tsai
#Modes of Operation 

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def modify_bits(cipherArr): 
    cipherArr[17] = cipherArr[17] ^ 122
    cipherArr[23] = cipherArr[23] ^ 124
    cipherArr[28] = cipherArr[28] ^ 122 
    return bytes(cipherArr)

def submit(input, key, IV): 
    input = input.replace(';', '%3B')
    input = input.replace('=', '%3D')
    modified = "userid=456;userdata=" + input + ";session-id=31337"
    padded = pad(modified.encode('utf-8'), AES.block_size) 
    aes = AES.new(key, AES.MODE_CBC, IV)
    ciphertext = aes.encrypt(padded)
    attacked = modify_bits(list(ciphertext))
    return attacked

def verify(string, key, IV): 
    aes = AES.new(key, AES.MODE_CBC, IV)
    decrypted = aes.decrypt(string) 
    unpadded = unpad(decrypted, AES.block_size) 
    return ';admin=true;' in str(unpadded) 

def main():
    key = get_random_bytes(16) 
    IV = get_random_bytes(16) 
    text = submit('Hank Tsai p2 AadminAtrueA', key, IV) 
    result = verify(text, key, IV)
    print('Result for flipping bit attack ', result) 

if __name__ == "__main__":
    main()