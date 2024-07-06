while True:
    rounds = input()
    if rounds == '0':
        break
    ab = input().split()
    div_x, div_y = int(ab[0]), int(ab[1])
    for i in range(int(rounds)):
        ab = input().split(' ')
        x, y = int(ab[0]), int(ab[1])
        if x == div_x or y == div_y:
            print('divisa')
            continue
        response = 'N' if y > div_y else 'S'
        response += 'E' if x > div_x else 'O'
        print(response)
