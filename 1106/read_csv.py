import csv
from sensor import Sensor

my_dict = {}   # 임의로 만든 딕셔너리. 형식은 "front" : Sensor("front")가 될 것임

# csv 형식: "name": "front", "distance" : "0.5". 기존 딕셔너리의 키:밸류가 두개가 들어있는 구조.
# csv 에서 print("name") -> name에 해당하는 front 출력)
# 그냥 딕셔너리였으면 print("front") -> distance 출력
# 최종 구조 -> 이름: 객체, 객체는 여러 distance를 가짐
with open("sensors.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['name'] not in my_dict: # 내 임의 딕셔너리 안에 front가 없으면?
            s = Sensor(row['name']) # front란 이름으로 인스턴스 생성
        my_dict[row['name']] = s # front: s로 임의 딕셔너리 안에 키와 밸류를 넣는다.
        s.add(row['distance']) # 인스턴스 s의 속성 distance에 csv의 distance값을 넣는다.  ***csv에서 불러온 내용은 문자열이다.*** 형변환 안해주면 문자열로 객체 속성으로 들어가서 대소비교가 안된다.


for row in my_dict: # 딕셔너리의 키만 순회한다. 즉, row가 의미하는 바는 front, rear
    s = my_dict[row] # 인스턴스 (dict[front]가 의미하는 바가 front 키에 대응하는 밸류인 객체이므로)
    print(s.values)
    print(s.average())
    print(s.minimum())
    print(s.skipped)



