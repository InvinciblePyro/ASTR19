import random
import string
import time

txt = "HELLO"
def id_generator(size=6, chars=string.ascii_uppercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size))

def funTextThing(text, speed):
    rand_word = (id_generator(len(text)))
    new_rand_word = rand_word

    for i in range(len(text)):
        #rand_word = (id_generator(1)) + rand_word[i+1:]
        while new_rand_word[i] != text[i]: 
            time.sleep(speed)
            print(new_rand_word)
            new_rand_word = (new_rand_word[0:i]) + (id_generator(1)) + (rand_word[i+1:])
        print(new_rand_word + "🟢") 

        
def main():
    funTextThing(txt, 0.03)



if __name__ == "__main__": main()
