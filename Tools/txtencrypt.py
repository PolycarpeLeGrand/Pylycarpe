from Crypto.Cipher import AES


# Encryption of files
# In theory, each nonce value should only be used once with each key but i don't care
def encrypt(key, text, nonce):
    cipher = AES.new(str.encode(key), AES.MODE_EAX, nonce=nonce)
    # nonce = cipher.nonce
    ciphertext, _t = cipher.encrypt_and_digest(str.encode(text))
    return ciphertext


def decrypt(key, text, nonce):
    cipher = AES.new(str.encode(key), AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(text)
    return str(plaintext, 'utf-8')


def read_and_valid_key():
    # 16 chars bitable
    k = input('Enter key: ')
    return k


if __name__ == '__main__':
    txt = 'allo je suis une grosse bitte mais je suis cachee alors loeil nu ne saurait me voir lalalalalla'
    #txt = str.encode(txt)
    key = 'cle de 16 bittes'
    nonce = b'oups'
    ct = encrypt(key, txt, nonce)
    res = decrypt(key, ct, nonce)
    print(type(res))
    print(res)

