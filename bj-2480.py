input = input()
input_split = input.split(" ")

a = int(input_split[0])
b = int(input_split[1])
c = int(input_split[2])

if a == b and b == c and c == a:
    print(10000 + 1000*a)
elif a != b and b != c and c != a:
    if a > b and a > c:
        print(a*100)
    elif b > c and b > a:
        print(b*100)
    elif c > b and c > a:
        print(c*100)
else:
    if a == b:
        print(1000 + a*100)
    elif b == c:
        print(1000 + b*100)
    elif c == a:
        print(1000 + c*100)