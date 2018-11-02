#Exercise 17

import random as rn
import time as tm


# ektyposi pinaka / lista epou tha emfanistei se 3x3
def table_3x3(positions):
    print "\n"
    print " ", positions[0], "|", positions[1], "|", positions[2]
    print " ---+---+---"
    print " ", positions[3], "|", positions[4], "|", positions[5]
    print " ---+---+---"
    print " ", positions[6], "|", positions[7], "|", positions[8]
    print "\n"

# epistrefei to position pou epaikse o paiktis
def readPosition(player, positions):
   # emfanisi table me tis theseis kai ta noumera
    table_3x3(positions)
    table_3x3(range(9))

    # oso to tetragwno den einai egyro
    while True:

        # epilogh position apo paikti
        print player, "Select square:"
        position = int(input())
        if position < 0 or position > 8:
            print "Select between 0 and 8!"
        elif positions[position] != " ":
            print "The", position, " it is not empty"
        else: # egyri timi
            break
    return position


# anakoinosi tis epilogis toy paikti, pos einai einai h thesi pou paiktis kai positions ta koutakia
def play(player, pos, positions):


    print "O paikths", player, "paizei sto:", pos

    #  symplirosi thesis
    positions[pos] = player

# elegxei an yparxei 3da
def check(player, positions):
    # gia kathe triada thesewn
    for triple in triples:

        pos_a, pos_b, pos_c = triple
        # elegxei an o paikths exei katalavei mia triada
        if positions[pos_a] == positions[pos_b] == positions[pos_c] == player:
            return True

    return False



# elegxei an ypatxei 3da opou o paiktis exeis epileksei tis 2 apo 3s thesis/ epistrefi thn kenh thesi h none
def check_partial(player, positions):
    #
    for triple in triples:
        #3 thesis ths triadas
        pos_a, pos_b, pos_c = triple
        # an o paikths exei katalabei tis 2 apo tis 3 theseis
        if (positions[pos_a] == positions[pos_b] == player and
                positions[pos_c] == " "):
            return pos_c
        elif (positions[pos_a] == positions[pos_c] == player and
              positions[pos_b] == " "):
            return pos_b
        elif (positions[pos_b] == positions[pos_c] == player and
              positions[pos_a] == " "):
            return pos_a

    return None


# epistrefei ton paikth poy exei seira

def next_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

# epistrefei lista me tis diathesimes theseis
def available(positions):
    return [s for s in range(9) if positions[s] == " "]

#epistrefei ti thesi p prepei na paiksei o X
def paper_position(positions):
    # poses kiniseis exei kanei o paikths x
    moves = positions.count("X")
    if moves >= 2:
        # ginetai elegxos an mporei na kanei triliza o paikths x
        position = check_partial("X", positions)
        if position is not None:
            return position
        # elegxei an mporei o paikths O na kanei triliza
        position = check_partial("O", positions)
        if position is not None:
            return position
    # se aythn thn periptwsh epilegei mia tyxaia thesh
    return rn.choice(available(positions))

# dhmioyrgia pliadas h opoia periexei tis pithanes triadea
triples = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6))

# mia lista kenh me 9 theseis(9 thesis tis trilizas)
positions = 9 * [" "]

# kathorizoume poios paizei prwtos
player = "X"

# orizoume to x na einai o ypologisths
computer = "X"

empty_positions = 9

#arxikopoihsh me bolean, sthn arxh false giati den yparxei triliza
triliza = False

while empty_positions > 0 and not triliza:
    if player == computer:
        position = paper_position(positions)
    else:
        position = readPosition(player, positions)

    # simplirosi thesi
    play(player, position, positions)

    empty_positions -= 1

    # elegxos gia triliza
    triliza = check(player, positions)

    # enallagh paikth
    player = next_player(player)

# ektypwnei ton teliko pinaka
table_3x3(positions)

if triliza:
    print "Triliza!! won ", next_player(player)
else:
    print "Draw, no one wins"

