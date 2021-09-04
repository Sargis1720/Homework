# 1. Enter your name, then find the sum of the ASCII values of the letters in your name. If that number is larger than
# 500, print "I've got a great name!", and "I've got a fancy name!" otherwise.

# s = input("Write your name and surname: ")
# b = ([ord(c) for c in s])
# result = sum(b)
# if result < 500:
#     print("I've got a great name")
# else:
#     print("I've got a fancy name!")


# 2. Ask the user for a movie title. If the title starts with a capital letter, print "Great title!", otherwise print
# "Titles start with capital letters...". If the input is not a string, print "Why are you doing this to me?".

# a = input("write your favorite name of film: ")
# if a.istitle():
#     print("Great title")
# elif a.isdigit():
#     print("Why are you doing this to me?")
# else:
#     print("Titles start with capital letters...")


# 3. Ask the user to input his/her age. If the user is older than 18, than tell them they're eligible to vote. If they
# are younger than 18, tell them how many years do they have to wait.

# a = int(input("Write your age places: "))
# if a > 18:
#     print("You eligible to vote")
# else:
#     print("You need to wait to vote", 18 - a, "year")


# 4. Write a program that will tell us whether a given year is a leap year or not.

#check_leap_year = int(input("Write your year of birth and check if the year is a leap year: "))
# if (check_leap_year % 4) == 0:
#    if check_leap_year % 100 == 0:
#        if check_leap_year % 400 == 0:
#            print(f"{check_leap_year} is a leap year")
#        else:
#            print(f"{check_leap_year} is not a leap year")
#    else:
#        print(f"{check_leap_year} is a leap year")
# else:
#    print(f"{check_leap_year} is not a leap year")

# 5. Using 'random' module, generate a random number between -1000 and 1000. If the number is positive, print positive.
# If it's negative, print negative along with the absolute value of the number.

# import random
# a = random.randint(-1000, 1000)
# if a < 0:
#     print(f"{a} number is negative")
# else:
#     print(f"{a} number is positive")