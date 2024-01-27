#!/usr/bin/python3
def uppercase(str):
    for i in str:
        j = ord(i)
        if (j > 96) and (j < 123):
            j = j - 32
        print("{}".format(chr(j)), end='')
    print('')
