my_list = []
skip = 0
try:
    with open("distances.txt") as f:
        for line in f:
            try:
                my_list.append(float(line))
            except ValueError:
                skip += 1
    def average(a):
        return sum(a) / len(a)
    print("건너뛴 줄 수: " + str(skip))
    print("최솟값: " + str(min(my_list)))
    print("평균: " + str(average(my_list)))
except FileNotFoundError as e:
    print(e)



