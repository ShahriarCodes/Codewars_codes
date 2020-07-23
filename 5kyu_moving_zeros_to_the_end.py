a = [False,1,0,1,2,[],{},None,True,False,0,1,3,"a",0,0,0,{}]
b = []
boolean = []

for i in a:
    if type(i) == bool:
        boolean.append(i)
    elif type(i) == int and i == 0:
        b.append(i)
        #a.remove(i)

print(a)
print(b)
print(boolean)

new = []

for i in range(0,len(a)-1):
    if a[i] != 0 or type(a[i])==bool:
        new.append(a[i])
print(new)

final = new + b

print(final)

def move_zeros(array):
    a = array[:]
    b = []
    for i in a:
        if type(i) == int and i == 0:
            b.append(i)

    new = []

    for i in range(0,len(a)):
        if a[i] != 0 or type(a[i])==bool:
            new.append(a[i])
    final = new + b
    return final

print(move_zeros(a))


test = [9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,9]

def move_zeros(array):
    a = array[:]
    b = []
    for i in a:
        if type(i) == float and i == 0.0:
            b.append(0)
        if type(i) == int and i == 0:
            b.append(i)

    new = []

    for i in range(0,len(a)):
        if a[i] != 0 or type(a[i])==bool:
            new.append(a[i])
    final = new + b
    return final
