"""RECURSION"""

# 1. Write a recursive function to calculate the sum of reciprocals of powers of 2. Try increasing the n and see the
# magic.
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի երկրաչափական գումարը, որտեղ r = 1 / 2 է։ Փորձեք բացրձրացնել n-ի արժեքը հետաքրքիր
# արդյունք ստանալու համար։

def power(r, n):  # սա էլ է երկրորդ խնդիրը ոնց-որ
    if n == 0:
        return 1
    else:  # else կարող է չլինել, բայց սխալ չի
        return r * power(r, n-1)
print(power(5,2))


# 2. Write a recursive function to calculate n-th power of a.
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կհաշվի a-ի n աստիճանը։


def calc_power(x: int, num: int):
    if num == 0:
        return 1
    elif num == 1:
        return (x)
    else:
        return x * calc_power(x, num - 1)

#
# value = int(input("Enter value: "))
# power = int(input("Enter value: "))
# print(calc_power(value, power))





# 3. Write a recursive function that evaluates a mathematical expression. Example input - "5 + 6"
# Գրել ռեկուրսիվ ֆունկցիա, որը կհաշվի մաթեմատիկական արտահայտություն փոխանցված սթրինգի միջոցով։ Օրինակ՝ "5 + 6"


"""պահանջված տարբեռակը չի ստացվում որ "5 + 6" սարքի մենակ իրար կպածնա 
հաշվում երևի սպասեմ տնաինի վերլուծմաը, բայց կփորձեմ ելի"""

# def str_to_int_calc(n: int):
#     if n == "":
#         return 0
#     else:
#         return int(n[0]) + str_to_int_calc(n[1:])
# a = "455"
# print(str_to_int_calc(a))



# 4. Write a recursive function that reverses a string
# Գրել ֆունկցիա, որը ռեկուրսիվ կերպով կշրջի և կվերադարձնի փոխանցված սթրինգը։

def string_1(n: str):
    if len(n) == 0:
        return n
    else:
        return string_1(n[1:]) + n[0]


c = ('1, 2, 3, 4, 5, 6')
print(string_1(c))



# 5. Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved
# to the end of the string.
# Գրել ռեկուրսիվ ֆունկցիա, որը որպես արգումենտ կվերցնի սթրինգ և կվերադարձնի նոր սթրինգ, որտեղ օրիգինալ սթրինգում գտնվող
# բոլոր x-երը տեղափոխվել են սթրինգի ամենավերջը։


def end_X(string_x: str):
    if len(string_x)  == 1 or len(string_x) == 0:  # len(string_x) == 0-ն ավելորդ է։ Գործը դրան չի հասնի :)
        return string_x
    else:
        if string_x[0] == 'x':
            return end_X(string_x[1:]) + string_x[0]
        else:
            return string_x[0] + end_X(string_x[1:])

a = "xxrpxpe"
print(end_X(a))


"""OLD STUFF"""

# 6. Write a function that sorts a list in ascending. Additionally, the function may take a keyword argument that will
# reverse the sort (without recursion is fine).
# Գրել ֆունկցիա, որը կսորտավորի դրան փոխանցված լիստը աճման կարգով։ Կարելի է ֆունկցիային նաև ավելացնել kwarg, որը փոփոխելիս
# կկարողանանք լիստը սորտավորել նաև նվազման կարգով։

# Առանց .sort() կամ sorted()

# def int_ascending(*args):
#     for i in args:
#         a = sorted(args)
#         return a
#
# print(int_ascending(5,3,6,4,8,0))


# 7. Write a function that will take 4 arguments. First two are tuples and represent 2D coordinates of two circles.
# The others are the radii of our circles. The function must tell us whether one of the circles is inside the other, or
# do circles intersect, or are they far apart.
# Գրել ֆունկցիա, որը կվերցնի 4 արգումենտ։ Առաջին երկուսը tuple են, որոնք իրենցից ներկայացնելու են 2-չափ տարածության մեջ
# շրջանագծերի կենտրոնների կոորդինատներ։ Մյուս երկուսը լինելու են integer տիպի և ներկայացնելու են վերոնշյալ շրջանագծերի
# շառավիղները։ Ֆունկցիան պետք է տպի արդյո՞ք օղակները հատվում են, կամ մեկը մյուսի մեջ է, կամ իրարից հեռու են։



"""OPTIONAL"""

# 8. Write a program to combine two dictionaries adding values for common keys.
# Գրել ծրագիր, որը կմիացնի երկու dictionary։ Համընկնող բանալիների արժեքները պետք է գումարվեն։


d1 = {1: 100, 2: 200, 3: 300}
d2 = {4: 400, 5: 500, 3: 600}
d3 = dict(d1)
d3.update(d2)
for i, j in d1.items():
    for x, k in d2.items():
        if i == x:
            d3[i] = int(j) + int(k)

print(d3)



# 9. Write a program to create a dictionary from a string. The letters are the keys and the values are the counts of
# the corresponding letters.
# Սթրինգից ստեղծել dictionary: Սթրինգի տառերը հանդես են գալու որպես բանալիներ, իսկ սթրինգում դրանց քանակը որպես արժեքներ


string = 'abbsd'
d = {}
for i in string:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)

"""Լավ է, Սարգիս ջան"""