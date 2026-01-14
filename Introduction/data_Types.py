'''
Numeric Types: int- 100-200, float-1.26-21.0382, complex- 1+2j
Difference between int and float and complex is that int is a whole number, float is a decimal number and complex is a number with a real and imaginary part.

Sequence Types: list-[1,2,3,4,5], tuple-(1,2,3,4,5), range(1,10), string-"Hello World"
Difference between list tuple and range is that list is a mutable sequence type, tuple is an immutable sequence type and range is a sequence type that is an immutable sequence of numbers.

Mapping Type: dict-{"name":"ved", "age":21}
dict data types are used to store data values in key:value pairs.

Set Types: set-{1,2,3,4,5}, frozenset-{1,2,3,4,5}
diff b/w set and frozenset is that set is a mutable set type and frozenset is an immutable set type.

Boolean Type: bool
bool data types are used to store boolean values, True and False.

Binary Types: bytes, bytearray, memoryview 
bytes data types are used to store bytes values.
bytearray data types are used to store bytearray values.
memoryview data types are used to store memoryview values.

'''


a=12
b=1.2
c=1+2j
d=[1,2,3,4,5]
e=(1,2,3,4,5)
f=range(1,10)
g={"name":"ved", "age":21}
h={1,2,3,4,5}
i={1,2,3,4,5}
j=True
k=bytes(5)
l=bytearray(5)
m=memoryview(bytes(5))
n=None



my_list = [1,2,3,4,5]
print(my_list)
print(type(my_list))

my_tuple = (1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))

my_range = range(1,10)
print(my_range)
print(type(my_range))   

my_dict = {"name":"ved", "age":21}
print(my_dict)
print(type(my_dict))

my_set = {1,2,3,4,5}
print(my_set)
print(type(my_set))

my_frozenset = frozenset({1,2,3,4,5})
print(my_frozenset)
print(type(my_frozenset))

my_bool = True
print(my_bool)
print(type(my_bool))

my_bytes = bytes(5)
print(my_bytes)
print(type(my_bytes))

my_bytearray = bytearray(5)
print(my_bytearray)
print(type(my_bytearray))

my_memoryview = memoryview(bytes(5))
print(my_memoryview)
print(type(my_memoryview))

my_none = None
print(my_none)
print(type(my_none))    