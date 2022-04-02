import random
import sys #allows you to exit the game
from time import sleep #Provides a hold while explaining the rules

kelime_list = ["python", "software", "data", "coding"]
tahmin_edilen = []
gizli_kelime = random.choice(kelime_list)
kelime_uzunlugu = len(gizli_kelime)
alfabe = "abcdefghijklmnoprstuvwxyz"
kullanılan_harf =[]

def kurallar():
    for karakter in gizli_kelime:
        tahmin_edilen.append("-")
    print("The word we must guess is" , kelime_uzunlugu , "letters")
    sleep(1)
    print("You have 5 guesses.")
    sleep(1)
    print("If you don't know in 5 times, you lose.")
    print(tahmin_edilen)

def kelimeTahmin_etme():
    while True:
        kelime_tahmin = input("Want to guess the whole word? If you guess wrong, you lose. \n")
        if kelime_tahmin == "yes":
            kelime_tahminDeneme = input("Guess the word: ")
            if kelime_tahminDeneme == gizli_kelime:
                print("Congratulations, this is true word!")
                sys.exit()
            else:
                print("You guessed the wrong word. Game over")
                sleep(1)
                print("The word is: ", gizli_kelime)
                sys.exit()
        elif(kelime_tahmin == "no"):
            print("The game continues.")
            break
        else:
            print("Please answer yes or no")
            continue

def harfTahmin_etme():
    tahminSayisi=0

    while tahminSayisi < 10:
        kelimeTahmin_etme()
        harf_deneme = input("Try a lette: ")
        if not harf_deneme in alfabe:
            print("Please type a character from the alphabet")
        elif harf_deneme in kullanılan_harf:
            print("You said this letter before.")
        else:
            kullanılan_harf.append(harf_deneme)
        if harf_deneme in gizli_kelime:
            print("Right guess")
            for x in range(0, kelime_uzunlugu):
                if gizli_kelime[x] == harf_deneme:
                    tahmin_edilen[x] = harf_deneme
                    print(tahmin_edilen)
                if not "-" in tahmin_edilen:
                    print("You won!!!")
                    break
        else:
            print("You guessed wrong. Try again.")
            tahminSayisi += 1
        if tahminSayisi == 10:
            print("You lost. Hidden word: " , gizli_kelime)


kurallar()
harfTahmin_etme()
            
            
        

        


