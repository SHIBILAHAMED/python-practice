def add(a,b):
    print (f"adding {a} + {b}")
    return a + b

def sub(a,b):
    print(f"subtracting {a} -{b}")
    return a - b

def multi(a,b):
    print (f"multiplying {a} *{b}")
    return a*b

def div(a,b):
    print(f"dividing {a}/{b}")
    return a/ b

print ("Let's do some math with just fuctions")

age = add(30,5)
height = sub(78,4)
weight = multi(90,2)
iq = div(100,2)

print (f"age :{age}, height: {height}, weight: {weight},IQ {iq}")

print( "here is a puzzle ")

what = add(age, sub(height, multi(weight,div(iq,2))))

print ("that becomes : ",what,"can you do itby hand ?")
