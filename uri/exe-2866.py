rounds = input()
for round_index in range(int(rounds)):
    ciphered_message = input()
    plain_message = ''
    for letter in ciphered_message:
        if letter.islower():
            plain_message = letter + plain_message
    print(plain_message)
