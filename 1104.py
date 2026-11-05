# 리스트
my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print(my_list)
second_list = my_list[0:3]
print(second_list)
print(len(my_list), len(second_list))
for i in my_list:
    print(i)

# 딕셔너리
dict1 = {
    "x" : 1.0,
    "y" : 2.0
}

print(dict1["x"])
print(dict1.get("z", 0))
dict1["z"] = 3.0
dict1["x"] = 4.0
print(dict1["x"])
print(dict1["z"])

# 파일 읽기
nums = []

with open("distances.txt") as f:
    for line in f:
        nums.append(float(line))

with open("result.txt", "w") as f:
    f.write(str(sum(nums)))