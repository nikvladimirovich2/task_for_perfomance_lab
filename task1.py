n = int(input())
m = int(input())
circ_array = m * [int(i) for i in range(1, n + 1)]
path = []
while len(circ_array) > 1:
    path.append(circ_array[0])
    del circ_array[0:m - 1]
    if circ_array[0] == path[0]:
        break
for j in path:
    print(j, end='')
input()