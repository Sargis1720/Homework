"""MODULES"""
import re
import os
import random
from datetime import datetime
import time

random_words = '''baptizable hypnopaedia
tramless
ward
biprism
palagonitic
epicism
platycodon
hexagon
triduum
congenialize
sodbuster
lodesman
noneastern
doorbells
chalcotrichite
explicanda
trowie
detailedly
habitue
oatland
combustor
incitative
splenulus
archsewer
semaphore
polarise
pacificist
pretracheal
sporadial
merited
serab
huic
tib
fixidity
burbles
lathes
unomitted
swampy
standelwort
mogiphonia
declivent
overwend
quashes
planariform
pithecolobium
polystelic
symmetrophobia
millistere
panthea
brachydactylic
superorganism
cementification
surveiling
scrooges
haunching
ribber
unsuitableness
unperuked
elodeaceae
unwall
creosols
nonmythologic
reliances
emblazes
unconsolably
electrolyzer
orbitally
pinnula
unilobe
thoroughgoingness
worshipers
spondias
nitramino
unsadistic
unreelers
strengthfulness
cascadite
litus
legerity
subglenoid
rememberer
claribel
thrall
wattling
semistaminate
tabriz
philodramatic
quindecim
externize
handclasps
winterkill
unisonant
stampsman
received
stetting
daroo
jinglingly
unporcelainized
undeliverable'''.split()


# 1. Hangman!
# Create the hangman game. A list containing random words is provided. Each time the program runs, one random word must
# be selected. Then the user will try to guess the letters of the word. They will have lives equal to the length of the
# word. Now, about the formatting. Say we have the word car. The program must then output underscores equal to the
# length of the word.

# Guess a letter!
# _ _ _
#
# if we input 'a', the program will output:

# Guess a letter!
# _ a _

# and so on.

# Ստեղծում ենք մեր սեփական "Կախաղան" խաղը։ Ծրագիրը պահելու է պատահական բառ տրված "random_words" ֆայլից: Խաղացողը պետք է
# գուշակի տառ։ Եթե տառը բառի մեջ գոյություն չունի, խաղացողը կորցնում է "կյանք" (կյանքերը բառի երկարության չափ են): Եթե
# տառը կա, այն բացվում է և խաղացողը անցնում է հաջորդ տառը գուշակելուն։ Ծրագրի աշխատանքը պետք է հետևյալ տեսքն ունենա։
# Ենթադրենք բառը car է։ Կոնսոլում հետևյալ տեսքստն ենք տեսնելու

# Guess a letter!
# _ _ _

# Եթե ներմուծենք a, կստանանք հետևյալ տեսքստը

# Guess a letter!
# _ a _

# և այդպես շարունակ։ Եթե խաղացողի կյանքերը սպառվեն, տեղեկացրեք նրան և խաղից դուրս եկեք։ Հաղթելու դեպքում տպեք
# շնորհավորանք

# with open('random_words.txt', 'r') as file:          # ոնց գրում եմ ծրագիրը չի ընդունում, ինչումնա իմ սխալը ?
#     for word in file:  #FIXME file.readlines() մեթոդը պետք է կանչես։ Դա է վերադարձնում բոլոր տողերը լիստի մեջ
#         random_words = word


# def guess_the_words():
#     secret = random.choice(random_words)
#     print(secret)
#     guesses = 'aeiou'
#     lives = len(secret)
#     while lives > 0:
#         missed = 0
#         for letter in secret:
#             if letter in guesses:
#                 print(letter, end=' ')
#             else:
#                 print('_', end=' ')
#                 missed += 1
#
#         print()
#
#         if missed == 0:
#             print('\nYou Win!')
#             print('Thank you for game')
#             break
#
#         guess = input('\nguess a letter: ')
#         guesses += guess
#
#         if guess not in secret:
#             lives -= 1
#
#             print('\n', lives, 'more lives')
#             if lives == 0:
#                 print('\n\nThe word was')
#                 print(secret)
#                 return secret
#
#
# print(guess_the_words())

# 2. Write a function that will return the longest word in the random words file from the previous exercise.
# Գրել ֆունկցիա, որը կվերադարձնի "random_words" ֆայլի ամենաերկար բառը։


# def len_word(n):
#     res = re.findall(r"\w+", n)
#     n = max(res, key=lambda x: len(x))
#     return n
#
#
# random_words = 'car, exercise, function, Write'
# print(len_word(random_words))

# 3. Write a function that will take a string containing the path to a file as an argument and return its size in
# kilobytes.
# Գրել ֆունկցիա, որը կվերցնի սթրինգ արգումենտ։ Սթրինգը պետք է լինի որոշակի ֆայլի path-ը։ Ապա վերադարձնել այդ ֆայլի
# չափսերը կիլոբայթերով։ Հուշում՝ օգտվել os մոդուլից:

# def string_2(n: str) -> str:  # return-ի տիպը str ես նշել, բայց a-ն ամբողջ թիվ է
#     a = os.path.getsize(n)
#     return a
#
#
# path = str("C:\Program files")
# print(string_2(path))


# 4. Create a random number generator without using random module. The implementation is up to you. You may use
# current timestamp as a random seed.
# Գրել ֆունկցիա, որը կվերադարձնի պատահական թիվ։ Պատահական թվերի գեներատոր պարունակող մոդուլ չօգտագործել։ Իմպլեմենտացիան
# կախված է ձեզնից։ Մտածեք որոշակի ալգորիթմ և ըստ դրա գեներացրեք թիվ։ Կարող եք օգտագործել մեր անցած seed-ի գաղափարը։

def rand_numb():
    current_datetime = datetime.now()
    current_date = datetime.now()
    a = (current_datetime.second * 4 + 154 - 159 / 12)
    b = (current_datetime.microsecond)

    return int(a) * int(b)


print(rand_numb())

# 5. Create a file and put your shopping list in it. The file must start with current day's date.
# Ստեղծել ֆայլ, որը կպահի ձեր գնումների ցուցակը (ինչ ապրանք։ քանի հատ)։ Ֆայլը պետք է սկսվի տվյալ օրվա ամսաթվով։
