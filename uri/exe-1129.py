alt = {
    '0': 'A',
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'E'
}
while True:
    rounds = int(input())
    if rounds == 0:
        break

    for _round in range(rounds):
        correct_found = False
        answer = input()
        alternatives = answer.strip().split(' ')
        response = '*'
        i = 0

        for str_alternative in alternatives:
            alternative = int(str_alternative)
            if alternative <= 127 and correct_found:
                response = '*'
                break
            if alternative <= 127:
                correct_found = True
                response = alt[str(i)]
            i += 1

        print(response)
