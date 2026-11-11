import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data   # 센서 토픽용 QoS 설정
from sensor_msgs.msg import LaserScan
import math
import numpy as np

def angle_to_index(angle, angle_min, angle_increment):
    rad = math.radians(angle)
    i = round((rad - angle_min) / angle_increment)
    return(i)

class ScanListener(Node):
    def __init__(self):
        super().__init__('scan_listener')              # 노드 이름
        self.sub = self.create_subscription(
            LaserScan,                                 # 메시지 타입
            '/scan',                                   # 토픽 이름
            self.on_scan,                              # 메시지가 올 때마다 실행할 함수(콜백)
            qos_profile_sensor_data)                   # 라이다는 이 설정이 필요한 경우가 많아요


    def on_scan(self, msg):
        scan = np.array(msg.ranges)                       # 거리 배열
        n = len(scan)

        lo = angle_to_index(-30, msg.angle_min, msg.angle_increment)   # -30도의 인덱스: (각도 - msg.angle_min) / msg.angle_increment 를 반올림
        hi = angle_to_index(30)   # +30도의 인덱스
        front = scan[lo:hi + 1]                           # 전방 구간 (원래 인덱스 기준으로 먼저 자르기)

        valid = front[np.isfinite(front)]                 # 그다음에 inf 제거
        if 0.5 < valid:
            self.get_logger().warn("전방에 장애물이 감지되었습니다.")
            



def main():
    rclpy.init()                                       # ROS 통신 시작
    node = ScanListener()
    rclpy.spin(node)                                   # 메시지를 기다리며 계속 실행
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


