import random

def make_map():
    game_map = []
    for i in range(9):
        game_map.append("#")
    return game_map

def print_map(map_self):

    print(map_self[0] + 'ㅣ' + map_self[1] + 'ㅣ' + map_self[2] )
    print('_______')
    print(map_self[3] + 'ㅣ' + map_self[4] + 'ㅣ' + map_self[5] )
    print('_______')
    print(map_self[6] + 'ㅣ' + map_self[7] + 'ㅣ' + map_self[8] )
    print('_______')

def cheak_win(map):
    cheak = False
    if map[0] == map[1] == map[2] and map[0] != '#':
        cheak = True
    if map[3] == map[4] == map[5] and map[3] != '#':
        cheak = True
    if map[6] == map[7] == map[8] and map[6] != '#':
        cheak = True
    if map[0] == map[3] == map[6] and map[0] != '#':
        cheak = True
    if map[1] == map[4] == map[7] and map[1] != '#':
        cheak = True
    if map[2] == map[5] == map[8] and map[2] != '#':
        cheak = True
    if map[0] == map[4] == map[8] and map[0] != '#':
        cheak = True
    if map[2] == map[4] == map[6] and map[2] != '#':
        cheak = True
    return cheak
a = "O"
b = "X"
turn = 0
game_map = make_map()
for i in range(9):
    if turn == 0:
        while True:
            num = int(input("Enter the poistion : "))
            if game_map[num] == "#":
                game_map[num] = a
                break
        turn = 1
    else:
        while True:
            num = random.randrange(0, 8)
            if game_map[num] == "#":
                game_map[num] = b
                break
        turn = 0
    print("__________________ again")
    print_map(game_map)
    game_win_cheak = cheak_win(game_map)

    if game_win_cheak:
        break

if not game_win_cheak:
    print("draw")