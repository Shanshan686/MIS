team = 'New England Patriots'
print(team[19])
for letter in team:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter+'u'+suffix)
    else:
        print(letter+suffix)
print(team[0:12])
