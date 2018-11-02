# Exercise 3 

# input
x = raw_input("write something: ")


# rot_13 kodikopoiei to input toy xristi

def rot_13(s):

    # apothikeyi to keimeno se ROT13
    rot_13_text = ""

    # mesw tis ord ginete h antistixisi kathe gramma pou eisagei o xristis me ton pinaka ASCII
    for i in s:
        character = ord(i)

       # ginete elegxos an einai kefaleo h mikro, an einai prin h meta to M kai m kai kanei +13 theseis
        if character >= ord('a') and character <= ord('z'):
            if character > ord('m'):
                character = character - 13
            else:
                character = character + 13
        elif character >= ord('A') and character <= ord('Z'):
            if character > ord('M'):
                character = character - 13
            else:
                character = character + 13

       # ginete prosthiki twn grammatwn se ROT13 h chr antistoixei to noumero se gramma ston pinaka ASCII
        rot_13_text = rot_13_text + chr(character)

    return rot_13_text

# Print ta apotelesmata
print 'Text : ', x
print 'ROT13 : ', rot_13(x)

