from secrets import token_bytes

def random_key(length):
    # generate length random bytes
    tb = token_bytes(length)
    return int.from_bytes(tb,"big")

def encrypt(original):
    original_bytes = original.encode()
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    encrypted = original_key ^ dummy
    return dummy, encrypted

def decrypt(key1, key2):
    decrypted = key1 ^ key2
    # book says something about how adding 7 is important because it 'rounds up'
    # and prevents off by one errors 
    print(key1)
    print(key2)
    print(decrypted.bit_length())

    temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, 'big')
    return temp.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("O")
    result = decrypt(key1, key2)
    print(result)