'''
LEGB rule (order in which python checks for variables)
local = defined within a funtion
 Enclosing = nested functions...
  Global = explicitly defined at top / with keyword
   Built-in = pre assigned in python
'''

x = 'global_x'

def test():
    y = 'local_y'
    print(y)

# first thing, python is gonna check if theres a local variable called y
test()

def test():
    y = 'local_y'
    # print(y)
    print(x)

# no x in local scope -> checks elsewhere (no enclosing scope) -> global scope! and it finds it
test()

try:
    print(y)
except NameError:
    print('error! -> y is not defined in global scope dude')

def test():
    x='local_x'
    print(x)

test()
print(x)

print('now lets make x a global variable, but you shouldnt use this...  ')
def test():
    global x    # so now x is in the global scope, and we change its value
    # you dont really need to use this... actually
    x = 'local_x'
    print(x)


test()
print(x)

# import builtins
# print(dir(builtins))

print('nested functions... ')
def outer():
    x = 'outer_x'
    def inner():
        x = 'inner_x'
        print(x)
    inner()
    print(x)
outer()