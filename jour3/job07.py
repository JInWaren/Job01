alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
j = 0

for i in range(1, 27):
    print(alphabet[j:j+i])
    j = j + i


def alphabet():
    alphabet = "abcdefghijklmnopqrstuvwxyz" * 10
    j = 0

    for i in range(1, 27):
        print(alphabet[j:j+i])

alphabet()