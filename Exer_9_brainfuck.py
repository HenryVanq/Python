# Exercise 9 programma to opoio metafrazei th glwssa brainfuck gia to Hello World.
#++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
from __future__ import print_function

def bf(characters, left, right, data, index):

    #dimioyrgia pinaka (lista), arxikopoihsh me to 0 se kathe thesi
    array = [0] * 30000
    #arxikopoihsh pointer
    ptr = 0

    #arxikopoihsh i(toy input)
    i = 0
    # to i kanei diaperasi sto input tou xristi
    while i <= len(characters) - 1:
        # apothikeyei to xaraktira sti metavliti s
        s = characters[i]
        # ean einai > +ptr alliws midenizetai
        if s == '>':
            ptr += 1
            if ptr >= len(array):
                ptr = 0
        # an einai < -1ptr kai an einai < 0 to -1 se sxesi me to input
        elif s == '<':
            ptr -= 1
            if ptr < 0:
                ptr = len(array) - 1
        # +1 o deiktis deomenwn
        elif s == '+':
            array[ptr] += 1
        # -1 o deiktis deomenwn
        elif s == '-':
            array[ptr] -= 1
        # emfanisi dedomenou
        elif s == '.':
            print(chr(array[ptr]), end="")
        # index = dedomeno tou input, an to s einai dexete to opemeno char
        elif s == ',':
            if index >= 0 and index < len(data):
                array[ptr] = ord(data[index])
                index += 1
            else:
                array[ptr] = 0 # ektos input
        #an o deitkhs dedodmenwn einai 0 kai to loop 1 oso einai > 0 psaxnei to ]
        elif s =='[':
            if array[ptr] == 0:
                loop = 1
                while loop > 0:
                    i += 1
                    c = characters[i]
                    if c == '[':
                        loop += 1
                    elif c == ']':
                        loop -= 1
        # antistixi diadikasia mexri na vrei to [
        elif s == ']':
            loop = 1
            while loop > 0:
                i -= 1
                c = characters[i]
                if c == '[':
                    loop -= 1
                elif c == ']':
                    loop += 1
            i -= 1
        i += 1

if __name__ == "__main__":
    characters = raw_input("Copy/paste this : ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.):  ")
    bf(characters, 0, len(characters) - 1, "", 0)

