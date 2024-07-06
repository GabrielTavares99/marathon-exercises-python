rounds = input()

for _round in range(int(rounds)):
    word = input()
    rotated = input()
    new_word = ''
    for letter in word:
        initial_position = ord(letter)
        end_position = initial_position - int(rotated)
        if end_position < 65:
            diff_back_rotate = 65 - end_position
            end_position = 90 - diff_back_rotate
            end_position += 1
        new_word += chr(end_position)
    print(new_word)
