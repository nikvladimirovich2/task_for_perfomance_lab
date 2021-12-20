import json

with open('C:\\Users\\user\\Downloads\\tasksNT\\tests.json', 'r') as file1:
    data_tests = json.load(file1)

with open('C:\\Users\\user\\Downloads\\tasksNT\\values.json', 'r') as file2:
    data_values = json.load(file2)

result = {**data_tests, **data_values}

with open('C:\\Users\\user\\Downloads\\tasksNT\\result.json', 'w') as file3:
    json.dump(result, file3, indent=2)

file1.close()
file2.close()
file3.close()
input()
