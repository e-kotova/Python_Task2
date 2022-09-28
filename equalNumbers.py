a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a != b and b != c and a != c:
    print("0")
elif a == b and b == c:
    print("3")
elif b != c and a == c:
    print("2")
elif a != b and b == c:
    print("2")
elif a != c and a == b:
    print("2")

