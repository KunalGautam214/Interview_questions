# 1. Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return

arr = [64, 34, 25, 12, 22, 11, 90, 10]
bubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")

# 2. create list using comprehensive style
l = []
[l.append(i) for i in range(0, 10)]

# 3. create dict where key is numbere and value is square of that number ex: {1: 1, 2: 4}
d = {}
[d.setdefault(i, i*i) for i in range(0, 10)]

# 4. What is the output of the given code below
def addToList(val, list=[]):
    list.append(val)
    return list
list1 = addToList(1)
print(list1)
list2 = addToList(123, [])
print(list2)
list3 = addToList('a')
print(list3)
print(list1)

# 5. How to delete list in python
l = [1,2,3,4,5,6,7,8,9,10]
del l

# 6. Read a file and reverse the content of the file
with open('test.txt', 'r') as f:
    data = f.read()
r = data[::-1]

# 7. Read the file and count word of the file.
newdata = data.split(' ')
d = {}
for i in newdata:
    d.setdefault(i, i.count(i))

# 8. Write into the file
with open('newtext.txt', 'a') as f:
    f.write(r)

# 9. What is decorator?
# Class based decorator
class SmartDivide:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print('I am class decorator')
        if args[-1] == 0:
            print('Oops! cannot devide second arg is zero')
            return
        return self.func(*args, **kwargs)

# Function based decorator
def smart_divide(func):
    def inner(a, b):
        print('I am inner function')
        if b == 0:
            print('oops! cannot divide')
            return
        return func(a, b)
    return inner

@SmartDivide
# @smart_divide
def divide(a, b):
    return a / b
print(divide(2, 5))
print(divide(2, 0))

# 10. What is generator?
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b
x = fib(5)
for _ in range(0, 5):
    print(next(x))
for i in fib(5):
    print(i)

#Normal iterator function
class PowerTwo:
    def __init__(self, max):
        self.n = 0
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result
for x in PowerTwo(5):
    print(x)

#Power of 2 using generator function
def PowerTwoGenerator(max):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1

for x in PowerTwoGenerator(5):
    print(x)

# 11. Convert the string "123" into 123 without using any build in functions

# 12. How to get query parameter in django framework?
# request.GET

# 13. How to get body parameter(Payload) in django framework?
# request.data['fname']

# 14. What is slicing in python?
s = 'python coding prof=gramm'
ss = s[5:10]

# 15. Given an array, Find that Maximum difference between two elements such that larger element appears
# after the smaller number
l1 = [1, 3, 10, 6, 4, 8, 2]
largest = max(l1)
largest_index = l1.index(largest)
max_diff = 0
for index, value in enumerate(l1):
    if index < largest_index:
        difference = largest - value
        if difference > max_diff:
            max_diff = difference
print(max_diff)

# 16. Given an array of N integers, and a number sum, the task is to find the number of pairs of integers in the array
# whose sum is equal to sum
from itertools import combinations
def combinatio_sum(arr, sum1):
    length = len(arr)
    l = []
    for i in range(length):
        for subset in combinations(arr, i):
            if len(subset) == 2 and sum(subset) == sum1:
                print(subset)
                l.append(subset)
    return l
inp = [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1]
sum1 = 11
ll = combinatio_sum(inp, sum1)
print(len(ll))

# 17.
# input= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.20], ['Akriti', 41], ['Harsh', 39]]
# output: the second lowest mark getter :['Harry', 'Berry']
input= [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.20], ['Akriti', 41], ['Harsh', 39]]
ll = []
lowest_name, lowest_mark = input[0][0], input[0][1]
name, mark = 0, 0
for i in input:
    if i == 0:
        continue
    if lowest_mark < i[1]:
        name, mark = lowest_name, lowest_mark
        lowest_name, lowest_mark = i[0], i[1]
for i in input:
    if mark == i[1]:
        print(i[0], i[1])

# 18. Define a python class
class Employee:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(f'Hi {self.name}')
e = Employee('Python')
e.print_name()

# 19. Find the max element from list
l = [1,2,23,4,5]
t = (1,2,3,4,5)
max(l)

# 20. How to create a thread in python?
import threading
import requests
def run_url(url):
    res = requests.get(url)
for i in l:
    t = threading.Thread(target=run_url, args=(i,))
    t.start()
    t.join()

# 21. How the django works or what is the architecture of django framework?
# urls.py
# path('home', home)
# views.py
# def home(request):

# 22. Write a program to get desire output given below
# Input: H1e2l3l4o5w6o7r8l9d
# Output: Helloworld
# Input: Sda3m4pflgejttefxdt
# Output: sampletext
s = 'Sda3m4pflgejttefxdt'
new_s = ''
for i in range(0, len(s), 2):
    new_s += s[i]
print(new_s)

# 23. Traverse all the files in a given directory without using any predefined functions
import os
path = 'Downloads'
root, dirs, files = os.walk(path)

# 24. How to make a nested list to flat list?
# Input: ["Sam", [10987, [2.0, ["Hi", 39]], "Hello12345"], [[[56, 10.345678, ["He!!0"]]]]]
# 	Output <list>: ["Hi", "Sam", "Hello12345", 39, 56, 2.0, 10.345678]
l = ["Sam", [10987, [2.0, ["Hi", 39]], "Hello12345"], [[[56, 10.345678, ["He!!0"]]]]]
new_list = []
def flat_list(l):
    for n in l:
        if isinstance(n, int):
            new_list.append(n)
        elif isinstance(n, str):
            new_list.append(n)
        elif isinstance(n, float):
            new_list.append(n)
        elif isinstance(n, list):
            flat_list(n)
flat_list(l)
print(new_list)

# 25. How to sort a mixed element list using python?
def mixs(num):
    try:
        ele = int(num)
        return (1, ele)
    except ValueError:
        return (0, num)
test_list = ["Sam", 10987, 2.0, "Hi", 39, "Hello12345", 56, 10.345678, "He!!0"]
print("The original list : " + str(test_list))
test_list.sort(key=mixs)
print("List after mixed sorting : " + str(test_list))

# 26. Write a program to check Palindrom without using predefined functions
l = [1,2,3,2,1,0]
length = len(l)
flag = False
for index in range(0, length//2):
    if l[index] != l[length - index - 1]:
        flag = True
        break
if flag:
    print(False)
else:
    print(True)
#in one to check palindrome
print('palindrome', s == s[::-1])

# 27. Reverse each work of the sentence
s = 'Kunal Gautam'
l = s.split(' ')
new_l = []
for i in l:
    new_l.append(i[::-1])
print(' '.join(new_l))

# 28. Give two lists as input and find the common largest sub set of both the lists.
#     Program should handle dynamic input.
#     Print largest subset and it's length.
#     Ex: Input: l1 = [3, 4, 8, 12, 45, 6, 9, 2] and l2 = [1, 2, 3, 4, 5, 6, 7]
#     Output: [2, 3, 4, 6] and 4

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(l1)
print(l2)

s1 = set(l1)
s2 = set(l2)
common = s1.intersection(s2)
print(common, len(common))

# 29. What is shallow copy and deep copy in python?

# 30. Find all the gif string from the given string
my_str = ''' 123.123.123.123 - -
[26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248
"<A HREF="http://www.jafsoft.com/asctortf/">http://www.jafsoft.com/asctortf/</A>"
"Mozilla/4.05 (Macintosh; I; PPC)"123.123.123.231 - - [26/Apr/2000:00:23:47 -0400]
"GET /asctortf/ HTTP/1.0" 200 8130
"<A HREF="http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF">http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF</A>"
"Mozilla/4.05 (Macintosh; I; PPC)"123.123.123.452 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/5star2000.gif HTTP/1.0" 200 4005 "<A HREF="http://www.jafsoft.com/asctortf/">http://www.jafsoft.com/asctortf/</A>" "Mozilla/4.05 (Macintosh; I; PPC)"123.123.123.652 - - [26/Apr/2000:00:23:50 -0400] "GET /pics/5star.gif HTTP/1.0" 200 1031 "<A HREF="http://www.jafsoft.com/asctortf/">http://www.jafsoft.com/asctortf/</A>" "Mozilla/4.05 (Macintosh; I; PPC)"123.123.123.711 - - [26/Apr/2000:00:23:51 -0400] "GET /pics/a2hlogo.jpg HTTP/1.0" 200 4282 "<A HREF="http://www.jafsoft.com/asctortf/">http://www.jafsoft.com/asctortf/</A>" "Mozilla/4.05 (Macintosh; I; PPC)"123.123.123.911 - - [26/Apr/2000:00:23:51 -0400] "GET /cgi-bin/newcount?jafsof3&amp;width=4&amp;font=digital&amp;noshow HTTP/1.0" 200 36 "<A HREF="http://www.jafsoft.com/asctortf/">http://www.jafsoft.com/asctortf/</A>" "Mozilla/4.05 (Macintosh; I; PPC)" '''
n = my_str.split('/')
l = []
for i in n:
    if '.gif' in i:
        new_str = i.split(' ')
        l.append(new_str[0])
print(l)

# 31. Replace n with m in the given list
numbers = [5, 10, [15, [20, 25, [30, [35, 40], 45], 50, 55], 60], 65, 70]
n = 60
m = 80
def replace_numbers(nums, n, m):
    for idx, item in enumerate(nums):
        if isinstance(item, int):
            if item == n:
                nums[idx] = m
        elif isinstance(item, list):
            replace_numbers(item, n, m)

replace_numbers(numbers, n, m)
print(numbers)

# 32. How to get all, name=Rahul and first 10 records in django ORM query?
# Student.objects.all()
# Student.objects.filter(name='Rahul')
# Student.objects.all()[:10]

# 33. Inheritance in python
class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id
    def __str__(self):
        return self.emp_id
class Person(Employee):
    def __init__(self, emp_id, name):
        super().__init__(emp_id)
        self.name = name
e = Employee(12345)
print(e.emp_id)
p = Person(6789, 'Python')
print(p.name)

# 34. Find the minimum currency notes return to the customer.
# 2000, 500, 200, 100, 50, 20, 10, 5, 1
# Input: 5000
# Output: {2000: 2, 500: 2}
from collections import Counter
customer_note = 4999
currency_notes = [2000, 500, 200, 100, 50, 20, 10, 5, 1]
exchange = Counter()
i = 0
while customer_note != 0:
    if customer_note >= currency_notes[i]:
        exchange[currency_notes[i]] += 1
        customer_note -= currency_notes[i]
    elif customer_note < currency_notes[i]:
        i += 1
print(dict(exchange))

# 35. Create FIFO queue using python
def add_element(num, q):
    q.append(num)

def retrieve_element(q):
    return q.pop(0)

q = []
n = None
while True:
    n = int(input("Select options\n1. Add\n2. Retrieve\n3. Quit\n"))
    if n == 1:
        input_number = int(input("Enter number to add:"))
        add_element(input_number, q)
        print(q)
    elif n == 2:
        if len(q) <= 0:
            print("Queue underflow")
        else:
            pop_element = retrieve_element(q)
            print(pop_element)
    elif n == 3:
        print('Exiting from queue operations')
        break

# 36. What is map and filter functions in python?
def map_addition(n):
    return n + n
l = [1,2,3,4,5]
result = map(map_addition, l)
print(list(result))
result = map(lambda n: n * n, l)
print(list(result))
def odd_number(n):
    if n % 2 != 0:
        return n
result = filter(odd_number, l)
print(list(result))

# 37. What is multithreading and multiprocessing?
import threading
from multiprocessing import Process
def count_increment(n):
    for _ in range(0, 10):
        print('Number n : ', n)
        n += 1
# if __name__ == '__main__': put this line to run multiprocessing code
i = 0
print('Thread execution started')
t1 = threading.Thread(target=count_increment, args=(i,))
t2 = threading.Thread(target=count_increment, args=(i,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Thread execution completed')

print('Process started')
p1 = Process(target=count_increment, args=(i,))
p2 = Process(target=count_increment, args=(i,))
p1.start()
p2.start()
p1.join()
p2.join()
print('Process completed')

# 38. Count letter of the word.
# Input: ‘aaabbbccc’ output: ‘3a3b3c’
a = 'aaabbbccc'
b = ''
for i in a:
    c = a.count(i)
    if i not in b:
        b += str(c) + i
print(b)

# 38. Write a code to divide a list into 2 list in such a way that both list sum should be equal
# ex: [1, 2, 3, 2, 1], [5, 1, 3]
l = [1, 2, 3, 5, 1, 3, 2, 1]
total_sum = sum(l)
half_of_sum = total_sum // 2
list_1 = []
list_2 = []
index_pos = []
for idx, item in enumerate(l):
    if sum(list_1) < half_of_sum:
        list_1.append(item)
        index_pos.append(idx)
    if sum(list_1) > half_of_sum:
        list_1.pop()
        index_pos.pop()
    if sum(list_1) == half_of_sum:
        break

[list_2.append(item) for idx, item in enumerate(l) if idx not in index_pos]

print(list_1, list_2)
if sum(list_1) == sum(list_2):
    print(list_1, list_2)
else:
    print('Both list can not be divided in 2 list')

# 39. What is polymorphise, method overriding and method overloading?

# 40. Sort a list of dict based on age
emp_data = [{'name': 'kunal', 'id': 12345, 'salary': 1000, 'age': 21},
            {'name': 'gautam', 'id': 67890, 'salary': 2000, 'age': 20},
            {'name': 'kundan', 'id': 456732, 'salary': 3000, 'age': 22}]
emp = sorted(emp_data, key=lambda item: item['age'])
print(emp)

# 41. swap 2 number without using 3rd number
a, b = 2, 3
a = a + b
b = a - b
a = a - b
print(a, b)

# 41. How to authorize an user in django framework?

# 42. Write a custom decorator to authorize an user in django framework.

# 43. what is differance between append and extend function in python?

# 44. Find a second largest element from a list
l = [2, 1, 0, 9, 5, 6, 11, 10]
largest = sec_larget = l[0]
for item in l:
    if largest < item:
        sec_larget = largest
        largest = item
    elif item > sec_larget and largest != item:
        sec_larget = item
    elif largest == sec_larget and sec_larget != item:
        sec_larget = item
print(sec_larget)
print(largest)

# 45. Write a program of user defined exception in python
class UserDefindedException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg
try:
    raise UserDefindedException('value is non-zero')
except UserDefindedException as e:
    print(e.msg)

# 46. How to download the file from aws s3 bucket
# session.get_object(bucket_name='test', prefix='src/data/text.txt')

