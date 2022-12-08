def add(*args):
    #print(args)
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3, 5, 7, 8))