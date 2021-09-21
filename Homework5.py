"""DATA STRUCTURES"""

# 1. Write a program to multiply all the items in a list.
# Գրել ծրագիր, որը կբազմապատկի լիստի բոլոր թվերը։

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a = [i ** 2 for i in a]
# print(a)





# 2. Write a program to count the number of strings where the string length is 2 or more and the first and last
# character are same from a given list of strings.
# Գրել ծրագիր, որը կհաշվի լիստում եղած 2 կամ ավել երկարություն ունեցող լիստերի քանակը, որոնց առաջին և վերջին տառերը
# նույնն են։

# a = ["apple", "banana", "qiwi","strawberries", "aca", "ab", "b", "bob"]
# num = 0
# for i in a:
#     if len(i) >= 2 and i[0] == i[-1]:
#         num += 1
# print(num)


# 3. Write a program that will remove duplicates from a list. DO NOT use set() method directly on the list.
# Գրել ծրագիր, որը կջնջի դուպլիկատները լիստից։ ՉՕԳՏԱԳՈՐԾԵԼ set() մեթոդը։

# a = ["a", "b", "c", "a", "b", "c", "c"]
# b = []
# [b.append(i) for i in a if not i in b]
# print(b)


# 4. Create a list from 5 user inputs.
# Ստեղծել լիստ 5 ներմուծված թվերից

# a = list(input().split())
# b = [i for i in a]
# print(b)


# 5. Write a program to print the given list after removing the 2nd, 4th and 5th elements.
# Գրել ծրագիր, որը կջնջի տրված լիստի 2-րդ, 4-րդ և 5-րդ էլեմենտները։

# lst = ['Rock', 'Pop', 'Metal','Hip-Hop', 'Rap']
# a = list(lst)
# del a[3:5]
# a.pop(1)
# print(a, end=" ")


# 6. Given a list of ints, print True if the array contains a 2 next to a 2 somewhere.
# Գրել ծրագիր, որը կտպի True, եթե տրված լիստում ինչ-որ տեղ 2 թվին 2 է հաջորդում։

# ls =[1,2,2,4,5,6,7,9]
# s = str(ls)
# '2,2' in s
# print('True')


# 7. Given a list of ints, print True if every element is a 1 or a 4, and False otherwise.
# Գրել ծրագիր, որը կտպի True, եթե լիստի բոլոր էլեմենտները 1 կամ 4 են։ Հակառակ դեպքում տպել False:

# a = [1, 1, 2, 4, 5]
# for i in a:
#     if i == 1 or i == 4:
#         print("True")
#     else:
#         print("False")



# 8. Ask for user input and add that input as a key into the dictionary. If the key exists, warn the user about it and
# do nothing. Assign some arbitrary value to it.
# Պահանջել ներմուծել բանալի և ավելացնել այդ բանալին dictionary-ի։ Եթե այն արդեն գոյություն ունի, տպել, որ բանալին արդեն
# կա և ոչինչ չանել։ Որպես արժեք տեղադրել պատահական օբյեկտ



""""էս մեկը չի ստացվում իմ մոտ, for input() """






# 9. Loop through the values of a dictionary and add them to a new list.
# Ցիկլի միջոցով ավելացնել dictionary—ի արժեքները նոր լիստի մեջ։

# a = {"Arman": "25", "karen": "35", "Ani": "28", "kanach": "karmir"}
# b = {}
# for value in a.values():
#     b = value
#     print(b)


# 10. Write a script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are square of keys.
# Գրել ծրագիր, որը կստեղծի և կտպի dictionary, որի բանալիները [1,15] թվերն են, իսկ արժեքները դրանց քառակուսիները։

# d=dict()
# for x in range(1,15):
#     d[x]=x**2
# print(d)