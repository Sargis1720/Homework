"""FUNCTIONS"""
import random

# 1. We'll say that an element in an array is "alone" if there are values before and after it, and those values are
# different from it. Return a version of the given array where every instance of the given value which is alone is
# replaced by whichever value to its left or right is larger.
# Ենթադրենք տարրը "միայնակ" է, եթե նրանից առաջ կամ հետո գտնվող տարրերի արժեքը տարբերվում է իր արժեքից։ Ստեղծել ֆունկցիա,
# որը կվերցնի լիստ որպես արգումենտ և կվերադարձնի այդ լիստը ձևափոխված այնպես, որ բոլոր միայնակ տարրերը փոխարինված լինեն
# իրենցից աջ կամ ձախ գտնվող առավելագույն արժեք ունեցող տարրով ([4, 4, 1, 3, 3], այստեղ 1-ը կփոխարինվի 4-ով):








# 2. Write a function to create and print a list where the values are square of numbers between 1 and 30
# (both included).
# Ստեղծել ֆունկցիա, որը կստեղծի և կտպի լիստ, որի արժեքները [1, 30] միջակայքում գտնվող թվերի քառակուսիներն են։

# def numbers():
#     a = [i * i for i in range(1, 31)]
#     return [a]
#
# print(numbers())



# 3. Write a function which will take one argument n. Return a list of size n, that will contain random numbers
# from (-100, 400).
# Ստեղծել ֆունկցիա, որը կվերցնի մեկ արգումենտ՝ n: Վերադարձնել n երկարությամբ լիստ, որը կպարունակի (-100, 400)
# միջակայքում գտնվող պատահական թվեր։

# mylist = []
# def num_1(n):
#     x = random.randint(-100,400)   # չգիտեմ ինչքանովա պայմանին բավարարում
#     mylist.append(x)
#     return mylist
#
# print(num_1(mylist))


# 4. Write a function, that will take a list of words as an argument and return all the words in the list that start
# with a vowel.
# Ստեղծել ֆունկցիա, որը կվերցնի լիստ որպես արգումենտ (սթրինգերի) և կվերադարձնի մեկ այլ լիստ, որը կպարունակի այդ լիստի
# բոլոր այն բառերը, որոնք սկվում են ձայնավորով։



# vowels = 'aeiouy'
#
# def get_vowels_count(str):
#  str = str.casefold()
#
#
#  count = {}.fromkeys(vowels, 0)
#
#  for char in str:
#    if char in count:
#      count[char] += 1
#
#  return count
#
# str = '''All that is gold does not glitter,
#          Not all those who wander are lost;
#          The old that is strong does not wither,
#          Deep roots are not reached by the frost.
#          From the ashes a fire shall be woken,
#          A light from the shadows shall spring;
#          Renewed shall be blade that was broken,
#           The crownless again shall be king'''
#
# print(get_vowels_count(str))






# 5. We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each).
# Write a function to return the number of small bars to use, assuming we always use big bars before small bars. Return
# -1 if it can't be done.
# Մենք ուզում ենք պատրաստել որոշակի x կշռով շոկոլադ։ Ունենք փոքր և մեծ շոկոլադե սալիկներ, որոնք համապատասխանաբար
# կշռում են 1 և 5 կգ։ x կգ շոկոլադը պատրաստելու համար առաջինը օգտագործելու ենք մեծ սալիկները, ապա փոքր։ Սալիկները
# կտրատել հնարավոր չէ։ Գրել ֆունկցիա, որը կվերադարձնի անհրաժեշտ փոքր սալիկների քանակը։ Եթե հնարավոր չէ տրված սալիկների
# քանակով պատրաստել անհրաժեշտ շոկոլադը՝ վերադարձնել -1։
# Ֆւնկցիայի սահմանումն ունի հետևյալ տեսքը, որտեղ small, big -> հասանելի փոքր և մեծ սալիկների քանակը, իսկ goal-ը
# վերոնշյալ x-ն է։


def make_chocolate(small, big, goal):
    pass


# 6. Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other
# is "far", differing from both other values by 2 or more. Return False otherwise.
# Գրել ֆունկցիա, որը կվերցնի երեք ամբողջ թիվ որպես արգումենտ։ Վերադարձնել True, եթե b-ն կամ c-ն իրենց բացարձակ արժեքով
# տարբերվում են a-ից առավելագույնը 1-ով, երբ միաժամանակ մյուս երկուսը տարբերվում են իրարից 2-ով։ Հակառակ դեպքում
# վերադարձնել False




# 7. Write a function that gets a numerical list as an argument. Find the sum of the elements. If a certain element is
# 13 stop the count and return whatever was the sum before that.
# Ստեղծել ֆունկցիա, որը կգումարի տրված լիստի բոլոր թվերը և կվերադարձնի այն։ Եթե տարրերից մեկը 13 է, դադարեցնել հաշվարկը
# և վերադարձնել մինչև այդ պահը հաշված գումարը։





# 8. Write down the following functions in a lambda form
# Գրել հետևյալ ֆունկցիաների լամբդա տարբերակները


# a = lambda x: x ** 2
# print(a(5))




# a =  (lambda r, pi: (pi * r) ** 2)
# print(a(2, 3.14))




# b = (lambda x, y, p: (x + y) ** p)
# print(b(5,6,2))




# 9. Create a list from 1-100. Using the filter function, return a new list containing only the numbers ending with 7.
# Ստեղծել 1-100 թվերը պարունակող լիստ։ Օգտագործելով ֆիլտր ֆունկցիան, վերադարձնել նոր լիստ, որը կպարունակի օրիգինալի
# միայն այն թվերը, որոնք վերջանում են 7-ով

# def number():
#     b = []
#     a = [i for i in range(1, 100) if i % 10 == 7]
#     b.append(a)
#     return b
# print(number())

# չեմ հասկանում ինչիա գրում որ չէմ օգտագործում փոփոխականը

# def num_1():
#     ls_1 = (i for i in range(1, 100) if i % 10 == 7)
#     lst_2 = list(filter(num_1, lst_1))
#     return list_2
#
# print(num_1())



# 10. Create a function that will take a string as an argument. Return a new string which is the original string with
# each letter doubled. For example 'cat' will become 'ccaatt'
# Ստեղծել ֆունկցիա, որը կվերցնի սթրինգ։ Վերադարձնել սթրինգ, որը կլինի օրիգինալ սթրինգը, սակայն ամեն տառ կլինի
# կրկնապատկված։ Օրինակ cat—ը կվերադարձնի 'ccaatt'

# word = "cat"
# def double_str():
#     a =	(''.join(x * 2 for x in word))
#     return a
# print(double_str())
