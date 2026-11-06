x = 30
print(x)

y = 3.0
print(y)

z = "Hello, World!"
print(z)

w = True
print(w)

distance = float(input("Enter the distance: "))

if (distance < 0.3) :
    print("stop")
elif (distance >= 0.3 and distance < 1.0) :
    print("slow")
else :
    print("go")

j = 0;
for i in range(11) :
    j += i
print (j)

# 더하기. 입력: a, b 출력: 둘의 합
def add (a, b) :
    return a + b
print(add(5, 10))

# 섭씨 -> 화씨. 입력: 섭씨, 출력: 화씨
def celsius_to_fahrenheit(c) :
    return (c * 9/5+32)
print(celsius_to_fahrenheit(30))

# 최댓값. 입력: list 출력: 최댓값
numbers = [1, 2, 3, 4, 5]
def maximum(list) :
    m = 0
    for i in list :
        if i > m :
            m = i
    return m
print(maximum(numbers))
