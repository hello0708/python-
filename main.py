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


map_self = make_map()
print_map(map_self)

a = 'O'

number = int(input("Enter the your position : "))

map_self[number] = a
print_map(map_self)






