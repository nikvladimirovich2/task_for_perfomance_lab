with open('C:\\Users\\user\\Desktop\\file3.txt') as file:
    nums = list()
    for line in file.readlines(): 
        nums.extend(line.rstrip().split(' '))
nums = [int(c) for c in nums]
mean = sorted(nums)[len(nums) // 2]
count = 0
for i in nums:
    while i != mean:
        if i < mean:
            i += 1
            count += 1
        elif i > mean:
            i -= 1
            count += 1
print(count)
input()            