init = input()
init_split = init.split(" ")

init_1 = int(init_split[0])
init_2 = int(init_split[1])

nm = []
result = []

for a in range(init_1):
    nm_num = input()
    nm_num_sp = nm_num.split(" ")
    nm.append(nm_num_sp)

for b in range(init_1):
    nm_num_sec = input()
    nm_num_sec_sp = nm_num_sec.split(" ")
    nm_result = [int(x)+int(y) for x, y in zip(nm[b], nm_num_sec_sp)]
    result.append(nm_result)

for a in range(init_1):
    temp = ""
    for b in range(init_2):
        temp = temp+str(result[a][b])+" "
    print(temp.strip())