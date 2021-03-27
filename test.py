import random

def make_map():
    map = []
    for i in range(9):
        map.append('^')

    return map


def print_map(map_self):

    print(map_self[0] + 'ㅣ' + map_self[1] + 'ㅣ' + map_self[2] )
    print('_______')
    print(map_self[3] + 'ㅣ' + map_self[4] + 'ㅣ' + map_self[5] )
    print('_______')
    print(map_self[6] + 'ㅣ' + map_self[7] + 'ㅣ' + map_self[8] )
    print('_______')

def cheak_win(map):
    cheak = False

    if map_self[0] == map_self[1] == map_self[2]:
        check = True

    if a == map_self[3] == map_self[4] == map_self[5]:
        check = True

    if a == map_self[6] == map_self[7] == map_self[8]:
        check = True

    if a == map_self[0] == map_self[3] == map_self[6]:
        check = True

    if a == map_self[1] == map_self[4] == map_self[7]:
        check = True

    if a == map_self[2] == map_self[5] == map_self[8]:
        check = True

    if a == map_self[0] == map_self[4] == map_self[8]:
        check = True

    if a == map_self[2] == map_self[4] == map_self[6]:
        check = True


map_self = make_map()
print_map(map_self)

a = "O"
b = "x"
turn = 0

for i in range(9):

    if turn == 0:
        while True:
            num = int(input("Enter the your position : "))
            if map_self[num] == "^":
                map_self[num] = a
                break
        turn = 1

    else:
        while True:
            num = random.randrange(0, 8)
            if map_self[num] == "^":
                map_self[num] = b
                break
        turn = 0
    print("______________________ again")
    print_map(map_self)
    game_win_cheak = cheak_win(map_self)

    if game_win_cheak:
        break




