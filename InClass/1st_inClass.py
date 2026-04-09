import random
import string
import time

import numpy as np

def id_generator(size=6, chars=string.ascii_uppercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size))

def TxtLeftToRight(text, speed):
    text = text.upper()
    rand_word = (id_generator(len(text)))
    for i in range(len(text)):
        while rand_word[i] != text[i]: 
            time.sleep(speed)
            print(rand_word)
            rand_word = (rand_word[0:i]) + (id_generator(1)) + (rand_word[i+1:])
        print(rand_word + "🟢") 

def TxtPerLetter(text, speed):
    rand_word = (id_generator(len(text)))
    while rand_word != text:
    

        for i in range(len(text)):
            if rand_word[i] == text[i] : print(f"{rand_word[i]} IN {text}!!")
            rand_word = (id_generator(len(text)))           

        time.sleep(speed)
        print(rand_word)


def main():
    TxtLeftToRight("bleh", 0.05)


if __name__ == "__main__": main()
