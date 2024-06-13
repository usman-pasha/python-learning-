#  Arithmetic Operators

# operator   name                 Example
# +          Addition             10+20=30
# -          Subtractions         20-20=0
# *          Multiplications      10*20=200
# /          Divisions            20/10=2
# %          Modulus              22%10=2
# **         Exponent             4**2 =16
# //         Floor Division       9//2=4

a = 21
b = 10
# Addition
print ("a + b : ", a + b)
# Subtraction
print ("a - b : ", a - b)
# Multiplication
print ("a * b : ", a * b)
# Division
print ("a / b : ", a / b)
# Modulus
print ("a % b : ", a % b)
# Exponent
print ("a ** b : ", a ** b)
# Floor Division
print ("a // b : ", a // b)


#  comparison Operators

# operator     name                      Example
# ==          equal                     4 == 5 is not equal
# !=          Not Equal                 4!-5 is true
# >           grater than               4>5 is not true
# <           less then                 4<5 is true
# >=          grater than Equal t0      4>=5 is not true
# <=          less then equal to        4<=5 is true

a = 4
b = 5
# Equal
print ("a == b : ", a == b)
# Not Equal
print ("a != b : ", a != b)
# Greater Than
print ("a > b : ", a > b)
# Less Than
print ("a < b : ", a < b)
# Greater Than or Equal to
print ("a >= b : ", a >= b)
# Less Than or Equal to
print ("a <= b : ", a <= b)



#  Assignment Operators

# Assignment Operator
a = 10
# Addition Assignment
a += 5
print ("a += 5 : ", a)
# Subtraction Assignment
a -= 5
print ("a -= 5 : ", a)
# Multiplication Assignment
a *= 5
print ("a *= 5 : ", a)
# Division Assignment
a /= 5
print ("a /= 5 : ",a)
# Remainder Assignment
a %= 3
print ("a %= 3 : ", a)
# Exponent Assignment
a **= 2
print ("a **= 2 : ", a)
# Floor Division Assignment
a //= 3
print ("a //= 3 : ", a)

# operator     name                                         Example
# =            assignment operator                     a = 10
# +=           Addition assignment                     a += 5 (Same as a = a + 5)
# -=           subraction assignment                   a -= 5 (Same as a = a - 5)
# *=           Multiplication assign                   a *= 5 (Same as a = a * 5)
# /=           Division                                a /= 5 (Same as a = a / 5)
# %=           Remainder                               a %= 5 (Same as a = a % 5)
# **=          Exponent                                a **= 2 (Same as a = a ** 2)
# //=          floor division                          a //= 3 (Same as a = a // 3)


#  Logical Operators

# operator                          name                                                                   Example
# and Logical AND      If both of the operands are true then the condition becomes true.                a = 10
# or Logical OR        If any of the two operands is non-zero then the condition becomes true.          a += 5 (Same as a = a + 5)
# not Logical NOT      Used to reverse the logical state of its operand                                 a -= 5 (Same as a = a - 5)

x = 5
y = 10
if x > 3 and y < 15:
  print("Both x and y are within the specified range")

#  Membership Operators

# operator                          name                                                                                                     Example
# in           Evaluates to true if it finds a variable in the specified sequence and false otherwise.                x in y, here in results in a 1 if x is a member of sequence y.
# not in       Evaluates to true if it does not find a variable in the specified sequence and false otherwise         x not in y, here not in results in a 1 if x is not a member of sequence y.

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is a fruit!")
else:
    print("No, banana is not a fruit!")

fruits = ["apple", "banana", "cherry"]
if "banana" not in fruits:
    print("Yes, banana is a fruit!")
else:
    print("No, banana is not a fruit!")


#  Identity Operators

# operator                          name                                                                                                     Example
# is           Evaluates to true if the variables on either side of the operator point to the same object and false otherwise                x is y, here are results in 1 if id(x) equals id(y)
# is not       Evaluates to false if the variables on either side of the operator point to the same object and true otherwise         x is not y, there are no results in 1 if id(x) is not equal to id(y).

x = 10
y = 5
if x is y:
    print("x and y are the same object")
else:
    print("x and y are not the same object")
    
x = 10
y = 5
if x is not y:
    print("x and y are the same object")
else:
    print("x and y are not the same object")


#  Bitwise Operators

# Operator	  Name	                    Example
# &	Binary    AND	                Sets each bit to 1 if both bits are 1
# |	Binary    OR	                Sets each bit to 1 if one of the two bits is 1
# ^	Binary    XOR	                Sets each bit to 1 if only one of two bits is 1
# ~	Binary    Ones Complement	    Inverts all the bits
# ~	Binary    Ones Complement	    Inverts all the bits
# <<	      Binary Left Shift	    Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	      Binary Right Shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off


a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
# Binary AND
c = a & b # 12 = 0000 1100
print ("a & b : ", c)
# Binary OR
c = a | b # 61 = 0011 1101
print ("a | b : ", c)
# Binary XOR
c = a ^ b # 49 = 0011 0001
print ("a ^ b : ", c)
# Binary Ones Complement
c = ~a; # -61 = 1100 0011
print ("~a : ", c)
# Binary Left Shift
c = a << 2; # 240 = 1111 0000
print ("a << 2 : ", c)
# Binary Right Shift
c = a >> 2; # 15 = 0000 1111
print ("a >> 2 : ", c)