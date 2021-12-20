with open('C:\\Users\\user\\Desktop\\файл1.txt') as file:
    circle_coordinates = list()
    for line in file.readlines(): 
        circle_coordinates.extend(line.rstrip().split(' '))

with open('C:\\Users\\user\\Desktop\\файл2.txt') as file:
    point_coordinates = list()
    for line in file.readlines(): 
        point_coordinates.extend(line.rstrip().split(' '))

for i in range(0, len(point_coordinates) - 1, 2):
    if (float(point_coordinates[i]) - float(circle_coordinates[0])) ** 2 / float(circle_coordinates[2]) ** 2 + (float(point_coordinates[i + 1]) - float(circle_coordinates[1])) ** 2 / float(circle_coordinates[2]) ** 2 < 1:
        print(1)
    elif (float(point_coordinates[i]) - float(circle_coordinates[0])) ** 2 / float(circle_coordinates[2]) ** 2 + (float(point_coordinates[i + 1]) - float(circle_coordinates[1])) ** 2 / float(circle_coordinates[2]) ** 2 == 1:
        print(0)
    else:
        print(2)

input()
        