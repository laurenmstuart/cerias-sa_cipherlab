#!/usr/bin/python

##file: vigenere-solution.py
##author: Lauren M. Stuart laurenmstuart@gmail.com
##created for CERIAS Student Association activity CipherLab
## -- feb 11, 2016, please email with questions!

##    Copyright (C) 2016 Lauren M. Stuart
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random

_alphabet = 'abcdefghijklmnopqrstuvwxyz'
## we'll use _alphabet.find() to find the index
##(and therefore integer value) of a letter
## the underscore is a personal naming convention for global variables

_mod = 26
## the length of our alphabet, and our modulus

_mode = 'E'
#_mode = 'D'
##set our mode to 'E'ncrypt or 'D'ecrypt; comment out the line that should not be used

_message = 'hailhailtooldpurdueallhailtoouroldgoldandblackhailhailtooldpurdueourfriendshipmaysheneverlackevergratefulevertruethusweraiseoursonganewofthedayswespentwithyouallhailourownpurduehailhailtooldpurdueallhailtoouroldgoldandblackhailhailtooldpurdueourfriendshipmaysheneverlackevergratefulevertruethusweraiseoursonganewofthedayswespentwithyouallhailourownpurduehailhailtooldpurdueallhailtoouroldgoldandblackhailhailtooldpurdueourfriendshipmaysheneverlackevergratefulevertruethusweraiseoursonganewofthedayswespentwithyouallhailourownpurduehailhailtooldpurdueallhailtoouroldgoldandblackhailhailtooldpurdueourfriendshipmaysheneverlackevergratefulevertruethusweraiseoursonganewofthedayswespentwithyouallhailourownpurduehailhailtooldpurdueallhailtoouroldgoldandblackhailhailtooldpurdueourfriendshipmaysheneverlackevergratefulevertruethusweraiseoursonganewofthedayswespentwithyouallhailourownpurduehailhailtooldpurdueallhailtoouroldgoldandblackhailhailtooldpurdueourfriendshipmaysheneverlackevergratefulevertruethusweraiseoursonganewofthedayswespentwithyouallhailourownpurduehailhailtooldpurdueallhailtoouroldgoldandblackhailhailtooldpurdueourfriendshipmaysheneverlackevergratefulevertruethusweraiseoursonganewofthedayswespentwithyouallhailourownpurdue'
##to start, make the message without spaces or punctuation
## --> gain a level: change the code to allow for spaces and [some] punctuation in the message
## --> gain a level: change the code to strip all non-alphabetical characters from an arbitrary message

_ciphertext = ''
## to start, make an empty ciphertext variable;
##  copy and paste the output of the encryption when it's done


_key = 'cerias'
##to start, make the key without spaces or punctuation
## --> gain a level: change the code to allow for spaces and [some] punctuation in the key
##     (this may be easier after you have done the same for the message)


##--> gain a level: change the code to accept arbitrary text for key via console input
##--> gain a level: change the code to accept text from a written file

def main():
    
    ## get the key length. use len(str) on strings, .length() on lists

    if _mode == 'E':
        encrypt_message(_key, _message)

    elif _mode == 'D':
        decrypt_message(_key, _ciphertext)


def encrypt_message(key, message):

    keylength = len(key)
    
    keycursor = 0
    ##set our key pointer to the first character
    
    ciphertext = ''
    ##start a new empty string to put encrypted letters into
    

    for letter in message:
        letter = letter.lower()
        ##change the letter to lowercase for simplicity (in case it is not)

        Mvalue = _alphabet.find(letter)
        ##get the integer value of the letter in the message

        Kletter = _key[keycursor]
        ##get the letter at the cursor's current position in the key
        Kletter = Kletter.lower()
        ##change the letter to lowercase for simplicity (in case it is not)

        Kvalue = _alphabet.find(Kletter)
        ##get the integer value of the letter in the key

        if Mvalue != -1 and Kvalue != -1:
        ##make sure both the values are in range
        ## This is a good practice for secure programming!
        ## gain a level: why is this a good practice for secure programming?

            Cvalue = (Mvalue + Kvalue) % _mod
            ##add the two integer values together, and "wrap around" by using the modulus

            #print("Mvalue " + str(Mvalue) + " Kvalue " + str(Kvalue))
            ##this is a commented-out print statement used to debug
            
            Cletter = _alphabet[Cvalue]
            ##get the letter with the integer value of Cvalue

            ciphertext += Cletter
            ##add the new letter to our building ciphertext string
            ## use += for strings, and .append() for lists

            keycursor = (keycursor + 1) % keylength
            ##update our cursor (remember to wrap around the key as well)

        else:
            print("you've got a non-alphabetic character")

    print(ciphertext)
    ##print the new ciphertext at the end




def decrypt_message(key, ciphertext):

    keylength = len(key)
    
    keycursor = 0
    ##set our key pointer to the first character
    
    plaintext = ''
    ##start a new empty string to put encrypted letters into
    

    for letter in ciphertext:
        letter = letter.lower()
        ##change the letter to lowercase for simplicity (in case it is not)

        Cvalue = _alphabet.find(letter)
        ##get the integer value of the letter in the message

        Kletter = _key[keycursor]
        ##get the letter at the cursor's current position in the key
        Kletter = Kletter.lower()
        ##change the letter to lowercase for simplicity (in case it is not)

        Kvalue = _alphabet.find(Kletter)
        ##get the integer value of the letter in the key

        if Cvalue != -1 and Kvalue != -1:
        ##make sure both the values are in range
        ## This is a good practice for secure programming!
        ## --> gain a level: why is this a good practice for secure programming?

            Mvalue = (Cvalue - Kvalue) % _mod
            ##subtract the key letter value from the ciphertext letter value,
            ## and "wrap around" by using the modulus
            
            #print("Cvalue " + str(Cvalue) + " Kvalue " + str(Kvalue))
            ##this is a commented-out print statement used to debug
            
            Mletter = _alphabet[Mvalue]
            ##get the letter with the integer value of Mvalue

            plaintext += Mletter
            ##add the new letter to our building plaintext string
            ## use += for strings, and .append() for lists

            keycursor = (keycursor + 1) % keylength
            ##update our cursor (remember to wrap around the key as well)

        else:
            print("you've got a non-alphabetic character")

    print(plaintext)
    ##print the new plaintext at the end
    



##if this file is run on its own, rather than imported, call main()
if __name__ == '__main__':
    main()


