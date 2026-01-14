''' 
Operators are used to perform operations on variables and values.

Python operators can be categorized into the following types:
1. Arithmetic operators +, -, *, /, %, 
    **-exponentiation for power
    //-floor division remove decimal part    

2. Assignment operators =, +=, -=, *=, /=, %=, **=, //=, &=, |=, ^=, >>=, <<=

3. Comparison operators ==, !=, >, <, >=, <=

4. Logical operators and, or, not

5. Identity operators is, is not

6. Membership operators in, not in

7. Bitwise operators & (bitwise AND), | (bitwise OR), ^ (bitwise XOR), ~ (bitwise NOT), << (left shift), >> (right shift)

'''

#Arithmetic Operator
print(10+5)
print(10-5)
print(10*3)
print(10/2)
print(10%2)
print(10**2)
print(10//2)

#Assignment Operator
a=10
a+=5
print(a)
a-=5
print(a)
a*=5
print(a)
a/=5
print(a)
a%=5
print(a)
a**=5
print(a)
a//=5
print(a)
# a&=5
# print(a)
# a|=5
# print(a)
# a^=5
# print(a)
# a>>=5
# print(a)
# a<<=5
# print(a)        


#Comparison Operator
a=10
b=5
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Logical Operator
print('Logical Operator')
print(a>=5 and b<=5)
print(a>=5 or b>100)
print(not a>5)

#Identity Operator
print('Identity Operator')
print(a is b)
print(a is not b)

#Membership Operator
my_list = [1,2,3,4,5]
my_list1 = [1,2,3]

print('Membership Operator')
print(my_list in my_list1)
print(10 not in my_list)   

#Bitwise Operator
print('Bitwise Operator')
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << b)
print(a >> b)