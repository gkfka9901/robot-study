import math
angle_min = -3.1415927410125732
angle_max = 3.1415927410125732
angle_increment = 0.017501909285783768
range_min = 0.05000000074505806
range_max = 12.0

n = round(((angle_max - angle_min) / 0.017501909285783768) + 1) # 간격이 359면 점은 360개
step_deg = math.degrees(angle_increment)

def angle_to_index(angle, angle_min, angle_increment):
    rad = math.radians(angle)
    i = round((rad - angle_min) / angle_increment) + 1
    return(i)

print(n, step_deg)
print(angle_to_index(-30, angle_min, angle_increment))
print(angle_to_index(30, angle_min, angle_increment))