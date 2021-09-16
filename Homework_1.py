# 1. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a nested loop.
# Օգտագործելով ցիկլեր, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = [[x ** 2 for x in row] for row in a]
# print(b)



# 2. Create a 3x3 matrix that will contain the squares of the numbers from 1-9 using a list comprehension.
# Օգտագործելով comprehension, ստեղծել 3x3 մատրից, որը կպարունակի 1-9 թվերի քառակուսիները։

# a = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(3):
#     for j in range(3):
#         a[i][j] **= 2
#         print(a[i][j], end=" ")
#     print()



# 4. Count the number of 'b's in the given string. DO NOT use the count() method.
# Հաշվել տրված սթրինգում 'b'-երի քանակը։ Չօգտագործել count() մեթոդը։

# nonsense = 'Blinking blindly, brainy Bob brings beautiful beer bottles beneath blue butterflies billowing brilliantly.'
# b = 0
# for i in nonsense:
#     if i == 'b':
#         b += 1
# print(f'count b is {b}')



# 5. Write a program that will print the factorial of n.
# Գրել ծրագիր, որը կտպի n թվի ֆակտորիալը։

# n = int(input("Enter your factorial number: "))
# result = 1
# for i in range(2, n+1):
#     result *= i
# print(result)