class Sensor:
    def __init__(self, name):
        self.name = name
        self.values=[]
        self.skipped = 0

    def add(self, value):
        try:
            self.values.append(float(value))
            return True
        except:
            self.skipped += 1
            return False

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


if __name__ == "__main__":
    s = Sensor("front")
    s.add(3.0)
    s.add(4.0)
    s.add(5.0)
    print(s.values)
    print(s.average())
    print(s.minimum())