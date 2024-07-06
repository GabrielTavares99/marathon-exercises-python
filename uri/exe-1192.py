rounds = int(input())

for i in range(rounds):
    inp = input()
    items = list(inp)
    a = int(items[0])
    b = int(items[2])
    if a == b:
        print(a * b)
        continue
    if items[1].isupper():
        print(b - a)
        continue
    print(a + b)
