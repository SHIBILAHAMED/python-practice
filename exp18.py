def print_two(*args):
    arg1,arg2,arg3 =args
    print (f"arg1 :{arg1},arg2 {arg2},arg3 {arg3}.")
    
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1},agr2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I got nothing")


print_two("shibil","ahamed","just checking")
print_two_again("shibil","ahamed")
print_one("first")
print_none()
