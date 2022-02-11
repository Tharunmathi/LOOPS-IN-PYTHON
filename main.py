# /////////////////////////////////////////"KEYWORDS","LITERALS","STRING SLICING","MODIFY STRING","IF-ELSE","FOR","ITERATORS"
# "GENERATORS"
#  True,False,None,and are some examples of literal keywords

def my_func(a, b): # def keyword is used to declare the functions
    c = a+b
    print(c)
my_func (10, 20)
a = 0
while a < 4:
  a += 1
  if a == 2:
    continue  # continue is used to continue
  print (a)
for i in range(5):
    if (i == 3):
        break
    print(i)
print("End of execution")
# these are some examples of keywords
#//////////////////////LITERALS/////////////////////////////////////////////////////////////////////////////////////////
print( "1.STRING LITERALS" )
text1 = 'hello' # single-line literals
print(text1)
text='hello\
user'          # i)adding blackslash in end of the statement;
print(text)
text=""" hello
user 
welcome"""
print(text)    #ii) using triple quotes;
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt  
ut labore et dolore magna aliqua."""
print(a)     #  MULTILINE STRING with double quotes;
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.''' # multiline string with single quotes;
print(a)
a = "Hello, World!"
print(a[1])  # strings are like arrays
for x in "banana":
  print (x)  # loop through string
a = "Hello, World!"
print(len(a))  # length of a string
txt = "The best things in life are free!"
print("free" in txt) # check string is present are not
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
txt = "The best things in life are free!"
print("expensive" not in txt)
# /////////////////////////////////////"STRING SLICING "////////////////////////////////////////////////////////////////
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[-5:-2])
# ////////////////////////////////"MODIFY STRING"///////////////////////////////////////////////////////////////////////
a = "Hello, World!"
print(a.upper())  # all letters in upper case
a = "Hello, World!"
print(a.lower()) # all letters in lower case
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))  # "Jello, World!"
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
a = "Hello"
b = "World"
c = a + b
print(c) # string concatenate with +
a = "Hello"
b = "World"
c = a + " " + b
print(c) # string concatenate with space
"""age = 36
txt = "My name is John, I am " + age # we cannot combine string and numbers
print(txt)"""
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  # instead of combining we use .format()
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print("2.NUMERIC LITERALS")
x = 0b10100  # Binary Literals
y = 100  # Decimal Literal
z = 0o215  # Octal Literal
u = 0x12d  # Hexadecimal Literal

# Float Literal
float_1 = 100.5
float_2 = 1.5e2

# Complex Literal
a = 5 + 3.14j

print(x, y, z, u)
print(float_1, float_2)
print(a, a.imag, a.real)
str = "They said, Hello what's going on?"
print(str)
# using triple quotes
print('''''They said, "What's there?"''')

# escaping single quotes
print('They said, "What\'s going on?"')

# escaping double quotes
print("They said, \"What's going on?\"")
# Using Curly braces
print("{} and {} both are the best friend".format("Devansh", "Abhishek"))

# Positional Argument
print("{1} and {0} best players ".format("Virat", "Rohit"))

# Keyword Argument
print("{a},{b},{c}".format(a="James", b="Peter", c="Ricky"))
# Write a Python program to calculate the length of a string.
a="Tharun"
print("The length of a string is:",len(a))
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
def strname( fname):
    if(len(fname)<2):
        return 0
    else:
        return fname[0:2]+fname[-2:]
print(strname("W3resource"))
# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$';
def strname( fname):
    if(len(fname)<2):
        return 0
    else:
        print(fname.replace("r","$"))
strname("restart")

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
def strname(string1):
    if "ing" not in string1:
        return string1 + "ing"
    elif "ing" in string1:
        return string1 + "ly"
    else:
        return string1


print(strname("abc"))
print(strname("string"))
def odd_values_string(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('abcdef'))
print(odd_values_string('python'))
# Write a Python script that takes input from the user and displays that input back in upper and lower cases.
"""a=input("enter the string :")
print(a.upper())
print(a.lower())
# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))
# Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
a=input("enter the string:")
print(a.upper())
print("3.BOOLEAN LITERALS")
x = (1 == True)
y = (2 == False)
z = (3 == True)
a = True + 10
b = False + 10

print("x is", x)
print("y is", y)
print("z is", z)
print("a:", a)
print("b:", b)
print("4.SPECIAL LITERALS")
var1 = 10
var2 = None
print(var1, var2)
print("5.LITERAL COLLECTION ")
list=['John',678,20.4,'Peter']
list1=[456,'Andrew']
print(list)
print(list + list1)
str1 = "first"
id(str1)
str1 = str1+ " Two"
id(str1)"""

# //////////////////////////////////"IF-ELSE STATEMENT//////////////////////////////////////////////////////////////////
"""num = int(input("enter the number:"))
if num%2 == 0:
    print("Number is even")
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
if(a>b and a>c):
    print("a is greater in among")
if(b>c and b>a):
    print("b is greater in among")
if(c>a and c>b):
    print("c is greater in among")
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
if a > b: print("a is greater than b")
a = 2
b = 330
print("A") if a > b else print("B")
a = 330
b = 330
print("A") if a > b else print("EQUAL") if a == b else print("B")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
a = 33
b = 200

if b > a:
  pass    # pass statement
number = int(input("Enter the number?"))
if number==10:
    print("number is equals to 10")
elif number==50:
    print("number is equal to 50")
elif number==100:
    print("number is equal to 100")
else:
    print("number is not equal to 10, 50 or 100")
marks = int(input("Enter the marks? "))
if marks > 85 and marks <= 100:
   print("Congrats ! you scored grade A ...")
elif marks > 60 and marks <= 85:
   print("You scored grade B + ...")
elif marks > 40 and marks <= 60:
   print("You scored grade B ...")
elif (marks > 30 and marks <= 40):
   print("You scored grade C ...")  
else:
   print("Sorry you are fail ?")
# /////////////////////////////////"FOR LOOP STATEMENTS"////////////////////////////////////////////////////////////////
a=["apple","banana","cherry"]
for x in a:
    print(x)
for x in "banana":
  print(x)
list = [1,2,3,4,5,6,7,8,9,10]
n = 5
for i in list:
    c = n*i
    print(c)  
list = [10,30,23,43,65,12]
sum = 0
for i in list:
    sum = sum+i
print("The sum is:",sum)
for i in range(10):
    print(i, end=" ")
n = int(input("enter the number:"))
for i in range(1, 11):
    c = (n)*i
    print(n, "*", i, "=", c)
n = int(input("Enter the number "))
for i in range(2,n,2):
    print(i)  
list = ['Peter','Joseph','Ricky','Devansh']
for i in range(len(list)):
    print("Hello",list[i])
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
i = 0
str1 = 'javatpoint'

while i < len(str1):
    if str1[i] == 'a' or str1[i] == 't':
        i += 1
        continue
    print('Current Letter :', str1[i])
    i += 1 
# a program to print the 1st and last  two letters in a given string(W3RESOURCES)--->"OUTPUT:W3ES"
def stname(string1):
    if(len(string1)<2):
        return 0
    else:
       return string1[0:2]+string1[-2:]
print(stname("W3RESOURCES"))
# a program to get a string from a given string and change 'r' letter with "$" in restart
def strname(string1):
    b=string1[0]
    string1=string1.replace(b,'$')
    sring1=b+string1[1:]
    return string1
print(strname("restart"))
# a program to add 1st 2 letters in two strings under a common name;
def strname(string1,string2):
               a=string1[0:2]
               b=string2[0:2]
               return a + b
print(strname("arT","unh"))
# to add ing atlast of the string if not present;
def strname(string1):
     if "ing" not  in string1:
           return string1+"ing"
     elif "ing" in string1:
           return string1+"ly"
     else
         return string1
print(strname("abc"))
print(strname("string"))"""
# //////////////////////////////"ITERATORS"///////////////////////////////////////////////////////////////////////////
values = iter([1,2,3,4,5,6,7,8,9])
print(values.__next__())
print(values.__next__())
print(next(values))
print(values.__next__())
print(values.__next__())
print(values.__next__())
class TopTen:
    def __init__(self):
        self.nums = 1
    def __iter__(self):
        return self
    def __next__(self):
        val = self.nums
        self.nums+=1
        return val
values =TopTen()
"""print(values.__next__())
print(values.__next__())
print(values.__next__())
print(values.__next__())"""
for i in values:
    print(i)
    if i ==100:
        break
    else:
        continue
# ////////////////////////////////"GENERATORS"/////////////////////////////////////////////////////////////////////////
def topten():
    yield 1
    yield 2
    yield 3
    yield 4

values = topten()
"""print(values.__next__())
print(values.__next__())
print(values.__next__())
print(next(values))"""
for i in values:
    print(i)
def topten():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n = n+1

values = topten()
for i in values:
    print(i)
def simple():
    for i in range(10):
        if (i%2 == 0):
            yield i
for i in simple():
    print(i)

def multi_yield():
    str1 = "First string"
    yield str1
    str2 = "second string"
    yield str2
    str3 = "third string"
    yield str3

for i in multi_yield():
    print(i)



