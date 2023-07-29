# Python program to reverse a number

n = 12345
r = 0
while n > 0:
    r = r * 10 + n % 10
    n = n // 10
print(r)

n = 12345
rev = int(str(n)[::-1])
print(rev)


# Armstrong number program in python
# 153 : 1^3 + 5^3 + 3^3 = 153
# 371 : 3^3 + 7^3 + 1^3 = 371
# 407 : 4^3 + 0^3 + 7^3 = 407
# 1634 : 1^4 + 6^4 + 3^4 + 4^4 = 1634
# 8208 : 8^4 + 2^4 + 0^4 + 8^4 = 8208

n = 153
temp = n
s = 0
count = len(str(n))
while temp > 0:
    s += (temp % 10) ** count
    temp //= 10
if s == n:
    print('amrstrong number')
else:
    print('Not a amrstrong number')


list_of_digit = [int(d) for d in str(n)]
count = len(list_of_digit)
s = sum([d ** count for d in list_of_digit])
if s == n:
    print('amrstrong number')
else:
    print('Not a amrstrong number')


# Prime Number Program in Python
n = 8
flag = False
for i in range(2, n//2):
    if n % i == 0:
        flag = True
        break
if flag:
    print('Not a prime number')
else:
    print('Prime number')


# Fibonacci series program in python
f, s = 0, 1
r = f
for i in range(0, 20):
    r = f
    f = s
    s = r + s
    print(r)
print('completed')


# Python program for palindrome
n = 12321
temp = n
s = 0
while temp > 0:
    s = temp % 10 + s * 10
    temp //= 10
if s == n:
    print('palimdrom')
else:
    print('Not palimdrom')


# Python program to check number representation is in binary
n = 10011010
flag = False
while n > 0:
    t = n % 10
    n //= 10
    if t != 1 and t != 0:
        flag = True
        print('Number is not binary')
        break
if not flag:
    print('Number is binary')

# Write a program in Python to swap two numbers without using third variable?
a, b = 2, 5
print('a', a, 'b', b)
a = a + b
b = a - b
a = a - b
print('a', a, 'b', b)

# Python Program to find Prime numbers of given integer
n = 100
for i in range(2, n):
    fac = 0
    for j in range(2, (i//2 + 1)):
        if i % j == 0:
            fac += 1
            break
    if fac == 0:
        print(i)

# Perfect number program in Python with example 1+2+3 = 6
n = 6
temp = n
i = 1
s = 0
while i <= n // 2:
    if n % i == 0:
        s += i
    i += 1
if s == temp:
    print('Perfect number')
else:
    print('Not a perfect number')

# Python program to calculate the factorial using iterative approach
n = 6
fac = 1
for i in range(1, n + 1):
    fac = fac * i
print(fac)

# Python Program to find factorial of a number using recursion
def fac(n):
    if n == 1:
        return n
    else:
        return n * fac(n - 1)
print(fac(6))

# Python code to find l.c.m. of two numbers
n, m = 3, 7
greater = n if n > m else m
while True:
    if greater % n == 0 and greater % m == 0:
        lcm = greater
        break
    greater += 1
print(lcm)

# Python code to find h.c.f. of two numbers
n, m = 3, 7
least = n if n < m else m
hcf = 0
for i in range(1, least + 1):
    if n % i == 0 and m % i == 0:
        hcf = i

print(hcf) if hcf != 0 else print('No Hcf')

# Check Leap Year Using if else in Python
for i in range(0, 100000):
    if i % 4 == 0:
        if i % 100 == 0:
            if i % 400 == 0:
                print(i, 'leap year')
            else:
                pass
                # print(i, 'Not a leap year')
        else:
            print(i, 'leap year')
    else:
        pass
        # print(i, 'Not a leap year')

# Python program to remove character from string
s = 'Kunal Gautam'
r = 'a'
new_s = s.replace(r, '_')
print(new_s)
print(ord('a')) # ASCII values

# Python Program to count occurrence of characters in string
s = 'Kunal Gautam'
count_ch = 'a'
count = 0
for i in s:
    if i == 'a':
        count += 1
print('Total count of', count_ch, 'is', count)
print(s.count('a'))

# Anagram Program in Python
a = 'python'
b = 'thonpy'
if sorted(a) == sorted(b):
    print('anagram')
else:
    print('Not an anagram')

# String Palindrome program in python
a = 'madam'
if a == a[::-1]:
    print('palindrom')
else:
    print('Not palindrom')

# Python program to check given character is vowel or consonant
s = 'y'
if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('Vowel')
else:
    print('Not vowel')

# Python program to check given input is digit or not
i = 6
if 0 <= i <= 9:
    print('Digit')
else:
    print('Not digit')

# Replace string space with given character in Python
s = 'Kunal Gautam is my name'
r_ch = '#'
r = ''
for i in s:
    if i == ' ':
        i = r_ch
    r += i
print(r)

# Python Program to Convert lowercase vowel to uppercase
s = 'Kunal Gautam is my name'
v = 'aeiou'
for i in s:
    if i in v:
        U_i = i.upper()
        s = s.replace(i, U_i)
print(s)

# Python program to remove vowels from the string
s = 'Kunal Gautam is my name'
v = 'aeiou'
for i in s:
    if i in v:
        new_i = ''
        s = s.replace(i, new_i)
print(s)

# Python program to count vowels and consonants in the string
s = 'Kunal Gautam is my name'
v_count = 0
c_count = 0
v = 'aeiou'
for i in s:
    if i in v:
        v_count += 1
    else:
        c_count += 1
print('vowels count', v_count, 'consonent count', c_count)

# Print highest frequency Character in String in Python
s = 'Kunal Gautam is my name'
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(max(d.values()))
print(d)
new_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(new_d[0])

# Python Program to Replace First Vowel With ‘-‘ in String
s = 'Kunal Gautam is my name'
new_s = '-'
v = 'aeiou'
for i in s:
    if i in v:
        new_i = new_s
        s = s.replace(i, new_s, 1)
        break
print(s)

# Python program to Count alphabets, digits, special char in string
s = '%Kunal %%# Gautam is my name#1'
alpha = 0
digit = 0
special = 0
for i in s:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1
print('Alpha', alpha, 'digit', digit, 'special charater', special)

# Python Program to Separate Characters in a Given String
s = 'Kunal Gautam'
for i in s:
    print(i, sep='\n')
new_s = '\n'.join(s)
print(new_s)
list(map(lambda x: print(x, sep='\n'), s))

# Python Program to Remove Repeated Character from String
s = 'hello'
new_s = ''
for i in s:
    if i not in new_s:
        new_s += i
print(new_s)

# Python program to sort string character in ascending order
s = 'Kunal Gautam'
new_ss = ''.join(sorted(s))
print(sorted(s))
print(new_ss)


# to be continue
# Python Coding Questions on Array
# https://quescol.com/interview-preparation/python-coding-question