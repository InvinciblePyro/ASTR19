import random
import string
import time

def id_generator(size=6, chars=string.ascii_uppercase + string.digits): 
    return ''.join(random.choice(chars) for _ in range(size))

def TxtPerLetter(text, speed):
    rand_word = (id_generator(len(text)))
    for i in range(len(text)):
        while rand_word[i] != text[i]: 
            time.sleep(speed)
            print(rand_word)
            rand_word = (rand_word[0:i]) + (id_generator(1)) + (rand_word[i+1:])
        print(rand_word + "🟢") 

        
def main():
    TxtPerLetter("HELLOWORLD", 0.03)



if __name__ == "__main__": main()
