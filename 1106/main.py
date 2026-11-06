from sensor import Sensor

s = Sensor("front")
s.add(3.0)
s.add(4.0)
s.add(5.0)
print(s.values)