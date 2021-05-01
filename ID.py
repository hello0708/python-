def login_check(input_id, input_pwd):
    f = open('id_pwd', 'r')
    lines = f.readlines()
    flag = False
    for line in lines:
        temp = line.split('/n')[0]
        id, pwd = temp.split(',')
        if id == input_id and pwd == input_pwd:
            flag = True
            break
    return flag

for i in range ( 5 ) :
    input_id = input("Enter the id : ")
    input_pwd = input("Enter the pwd : ")

    flag = login_check(input_id, input_pwd)

    if flag:
        print("succes")
        break
    else:
        print("fail")
