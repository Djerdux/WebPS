from hashlib import sha256
from random import shuffle, randint, seed

def magic(id, data: str):
    
    # print(id)
    id = id.split()


    seed(int(id[0]))

    k = ''
    # print(id[1])
    for i in id[1]:
        if randint(0, 1):
            k += str(int(i, 16))
    # print(k)
    k = int(k)

    seed(k)

    st = list('0123456789abcdefghigklmnopqrstuvwxyz-!@.#$')
    shuffle(st)
    st = ''.join(st)
    l = len(st)

    data = list(data.lower())
    shuffle(data)


    for i in range(len(data)):
        data[i] = data[i].upper() if randint(0, 1) == 1 else data[i]


    h = sha256(''.join(data).encode('utf-8')).hexdigest()

    bts = bin(int.from_bytes(h.encode(), 'big'))
    bts = bts.count('1') * l * k + randint(0, 100)

    len_pass = 30

    if k % 30 > 12:
        len_pass = k % 30
    else:
        len_pass = 30 - k % 30


    data = ''
    for _ in range(len_pass):
        symb = st[bts % l]
        if symb.isalpha() and randint(0, 1):
            symb = symb.upper()

        data += symb
        bts //= l
        if bts < l:
            bts *= randint(10, 200)
        if bts == 0:
            bts = randint(10, 200)

    return data
    

if __name__ == "__main__":
    print(magic(2, "GoogleGeorgeMailRu"))

