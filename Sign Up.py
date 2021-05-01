f = open('ID_pwd', 'r')
liens = f.readlines()
total_id = []
for line in liens:
    id, pwd = line.split(",")
    total_id.append(id)
f.close()

f = open("ID_pwd", 'a')
id = input("enter the id : ")
pwd = input("end ther pwd : ")

if id not in total_id:
    f.write('\n' + id + ',' + pwd)
    f.close()


