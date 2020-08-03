rounds = input()

for _round in range(int(rounds)):
    led_qtd_reference = {
        '1': 2,
        '2': 5,
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6,
        '0': 6
    }
    num = input()
    num = str(num)
    count = 0
    for number in num:
        count += led_qtd_reference[str(number)]

    print('{} leds'.format(count))
