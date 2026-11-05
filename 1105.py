# 클래스
# self: 인스턴스 자기 자신. 글로벌 속성이나 함수가 아닌, 클래스에서 파생된 인스턴스 고유의 속성 또는 함수에 접근가능하게 함.
# __init__: 인스턴스 생성 시 자동으로 실행되는 함수. 인스턴스 생성 시 파라미터를 넣어 그 파라미터를 속성에 넣거나 함수를 실행할 수 있다.
class Sensor:
    def __init__(self, name):
        self.name = name
        self.values=[]

    def add(self, value):
        self.values.append(value)

    def minimum(self):
        if len(self.values) == 0:
            return None
        else:
            m = max(self.values)
            for i in self.values:
                if i < m:
                    m = i
            return m

    def average(self):
        if len(self.values) == 0:
            return None
        else:
            return (sum(self.values) / len(self.values))

front = Sensor("front")
rear = Sensor("rear")
print("front:" + str(front.values))
print("rear:" + str(rear.values))
print("front:" + str(front.average()))
print("front:" + str(front.minimum()))
print("rear:" + str(rear.average()))
print("rear:" + str(rear.minimum()))
front.add(2.0)
front.add(3.0)
front.add(4.0)
rear.add(10.0)
rear.add(13.0)
rear.add(15.0)
print("front:" + str(front.values))
print("rear:" + str(rear.values))
print("front:" + str(front.average()))
print("front:" + str(front.minimum()))
print("rear:" + str(rear.average()))
print("rear:" + str(rear.minimum()))

front.values=[]
with open("distances.txt") as f:
    for line in f:
        front.add(float(line))

print(front.values)