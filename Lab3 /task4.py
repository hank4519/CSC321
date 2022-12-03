from Crypto.Hash import SHA256
import time
# from bitstring import BitArray



def part1():
    h = SHA256.new(b'hello')
    print("hello ", h.hexdigest())
    h = SHA256.new(b'Hello')
    print("Hello ", h.hexdigest())
    h = SHA256.new(b'hEllo')
    print("hEllo ", h.hexdigest())
    h = SHA256.new(b'heLlo')
    print("heLlo ", h.hexdigest())
    h = SHA256.new(b'helLo')
    print("helLo ", h.hexdigest())
    h = SHA256.new(b'hellO')
    print("hellO ", h.hexdigest())


def part2Truncate(input, size):
    h = SHA256.new(input)
    return h.hexdigest()[0:size + 1]


def find_collision(size):
    hash_map = dict()
    i = 0
    flag = True
    while flag:
        h = SHA256.new(bytes(str(i), encoding="utf8"))
        hash_result = h.hexdigest()
        hash_result = bin(int(hash_result, base=16))[0:size + 1]


        if hash_result in hash_map:
            print("String", i, "\thashes to\t", hash_result)
            print("String", hash_map[hash_result], "\thashes to\t", hash_result)
            print("\n")
            flag = False

        hash_map[hash_result] = i

        i += 1

if __name__ == "__main__":
    # part1()
    xandy = dict()
    
    for i in range(8, 50, 2):
        st = time.time()
        find_collision(i)
        et = time.time()
        elapsed_time = et - st
        print("it takes ", elapsed_time, " seconds", "for", i, "bits")
        xandy[i] = elapsed_time

    print(xandy)
