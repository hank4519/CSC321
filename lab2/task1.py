#CSC 321, Lab 2 (part 1), Hank Tsai
#Modes of Operation 

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def cbc_encrypt(): 
    key = get_random_bytes(16) 
    IV = get_random_bytes(16) 
    cbc = open("cbc.bmp", "wb")
    #change cbc to ecb
    aes = AES.new(key, AES.MODE_ECB)
    with open("cp-logo.bmp", "rb") as image_file: 
        prev = IV
        header = image_file.read(54)
        cbc.write(header)
        body = image_file.read(16)
        while body: 
            if len(body) < 16: 
                body = body + b"\x00"*(16-len(body)%16)
            xoring = bytes([a ^ b for a, b in zip(body, prev)])
            new_data = aes.encrypt(xoring)
            prev = new_data 
            cbc.write(new_data)
            body = image_file.read(16)
    cbc.close() 

def ecb_encrypt(): 
    key = get_random_bytes(16) 
    ecb = open("ecb.bmp", "wb")
    aes = AES.new(key, AES.MODE_ECB)
    with open("cp-logo.bmp", "rb") as image_file:
        header = image_file.read(54)
        ecb.write(header) 
        body = image_file.read(16) 
        while body: 
            if len(body) < 16: 
                body = body + b"\x00"*(16-len(body)%16)
            new_data = aes.encrypt(body)
            ecb.write(new_data)
            body = image_file.read(16)
    ecb.close()

def main():
    ecb_encrypt() 
    cbc_encrypt()


if __name__ == "__main__":
    main()



